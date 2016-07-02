#!/usr/bin/env python
# -*- coding: ascii -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
#
"""extracts from wscript....
This is no longer a nice waf script,
it is a copy/paste nightmare of the rules for generating files
with a minimal runner that happens to work on Windows so that
the generated files can be put into CloudPebble.net for a build.

If you are looking for a bright side; pep-8 code for the non-rule stuff :-)
"""

import os
import json
import shutil

def generate_appinfo_h(task):
	src = task.inputs[0].abspath()
	target = task.outputs[0].abspath()
	appinfo = json.load(open(src))
	f = open(target, 'w')
	f.write('#pragma once\n\n')
	f.write('#define VERSION_LABEL "{0}"\n'.format(appinfo['versionLabel']))
	f.write('#define UUID "{0}"\n'.format(appinfo['uuid']))
	for key in appinfo['appKeys']:
		f.write('#define APP_KEY_{0} {1}\n'.format(key.upper(), appinfo['appKeys'][key]))
	f.close()

def generate_keys_h(task):
	src = task.inputs[0].abspath()
	target = task.outputs[0].abspath()
	keys = json.load(open(src))
	f = open(target, 'w')
	f.write('#pragma once\n\n')
	for key in keys:
		f.write('enum {\n')
		for key2 in keys[key]:
			f.write('\tKEY_{0}_{1},\n'.format(key, key2))
		f.write('};\n')
	f.close()

def generate_keys_js(task):
	src = task.inputs[0].abspath()
	target = task.outputs[0].abspath()
	keys = json.load(open(src))
	f = open(target, 'w')
	for key in keys:
		f.write('var {0} = {{'.format(key))
		i = 0
		for key2 in keys[key]:
			if i > 0: f.write(',')
			f.write('\n\t{0}: {1}'.format(key2, i))
			i += 1
		f.write('\n};\n')
	f.close()



class FakeTask(object):
    pass

class FakePath(object):
    def __init__(self, name):
        self.name = name
    def abspath(self):
        return os.path.abspath(self.name)

def ctx(rule, source, target):
    """Fake waf ctx, not even a class!"""
    print (rule, source, target)
    remove_prefix = '../'
    if target.startswith(remove_prefix):
        target = target[len(remove_prefix):]
    target_dirname = os.path.dirname(target)
    print target_dirname
    if not os.path.exists(target_dirname):
        print 'need to make'
        os.mkdir(target_dirname)
    task = FakeTask()
    task.inputs = [FakePath(source)]
    task.outputs = [FakePath(target)]
    rule(task)

# Generate appinfo.h
ctx(rule=generate_appinfo_h, source='appinfo.json', target='../src/generated/appinfo.h')

# Generate keys.h
ctx(rule=generate_keys_h, source='src/keys.json', target='../src/generated/keys.h')

# Generate keys.js
ctx(rule=generate_keys_js, source='src/keys.json', target='../src/js/src/generated/keys.js')
