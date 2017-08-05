# -*- coding:utf-8 -*-
"""
"""
__date__ = "05/08/2017"
__author__ = "zhaojm"

import json
import codecs


def load_json(json_path):
    fp = codecs.open(json_path, encoding="utf8", mode="r")
    json_str = json.load(fp)
    fp.close()
    return json_str
