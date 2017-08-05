# -*- coding:utf-8 -*-
"""
"""
__date__ = "05/08/2017"
__author__ = "zhaojm"

from chat.entity import file_util


def load(cfg_path):
    startup_cfg = file_util.load_json(cfg_path + "server/startup.json")

    servers_cfg = file_util.load_json(cfg_path + "server/servers.json")

    config = {
        "startup": startup_cfg,
        "servers": servers_cfg
    }

    return config


def load_webmgr_cfg(cfg_path):
    return file_util.load_json(cfg_path + "server/webmgr.json")
