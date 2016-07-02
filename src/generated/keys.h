#pragma once

enum {
	KEY_REQUEST_ERROR,
	KEY_REQUEST_PLAY_PAUSE,
	KEY_REQUEST_VOLUME_INCREMENT,
	KEY_REQUEST_VOLUME_DECREMENT,
	KEY_REQUEST_VOLUME_MIN,
	KEY_REQUEST_VOLUME_MAX,
	KEY_REQUEST_FORWARD_SHORT,
	KEY_REQUEST_FORWARD_LONG,
	KEY_REQUEST_BACKWARD_SHORT,
	KEY_REQUEST_BACKWARD_LONG,
	KEY_REQUEST_UP,
	KEY_REQUEST_DOWN,
	KEY_REQUEST_RIGHT,
	KEY_REQUEST_LEFT,
	KEY_REQUEST_SELECT,
	KEY_REQUEST_BACK,
	KEY_REQUEST_OK,
	KEY_REQUEST_MUTE,
	KEY_REQUEST_HOME,
	KEY_REQUEST_SETUP,
	KEY_REQUEST_POWER,
	KEY_REQUEST_OPTION,
	KEY_REQUEST_STOP,
	KEY_REQUEST_NEXT,
	KEY_REQUEST_PREV,
	KEY_REQUEST_FORWARD,
	KEY_REQUEST_REWIND,
	KEY_REQUEST_CLIENTS,
	KEY_REQUEST_REFRESH,
};
enum {
	KEY_TYPE_ERROR,
	KEY_TYPE_PLAYERS,
	KEY_TYPE_PLEX,
	KEY_TYPE_VLC,
	KEY_TYPE_XBMC,
	KEY_TYPE_WDTV,
};
enum {
	KEY_METHOD_ERROR,
	KEY_METHOD_SIZE,
	KEY_METHOD_DATA,
	KEY_METHOD_STATUS,
	KEY_METHOD_PLEX,
	KEY_METHOD_VLC,
	KEY_METHOD_XBMC,
	KEY_METHOD_WDTV,
	KEY_METHOD_REQUESTPLAYERS,
	KEY_METHOD_READY,
};
enum {
	KEY_PERSIST_LAST_USED_PLAYER,
	KEY_PERSIST_PLEX_CONTROLLING_TYPE,
	KEY_PERSIST_VLC_CONTROLLING_TYPE,
	KEY_PERSIST_XBMC_CONTROLLING_TYPE,
	KEY_PERSIST_WDTV_CONTROLLING_TYPE,
};