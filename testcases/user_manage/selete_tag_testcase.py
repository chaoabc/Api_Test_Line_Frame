#!/usr/bin/env python
# encoding: utf-8
# @author: miaoxiaochao
# @file: create_tag_testcase.py
# @time: 2020/6/7 11:12 上午
#@desc:
import requests
import unittest
from utils.config_utils import local_config
from utils import common_api

class APITest(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts =local_config.hosts
    def tearDown(self) -> None:
        pass

    def test_selete_user_tag(self):
        respon02 =common_api.selete_user_tag(common_api.get_access_token_value)
        self.assertEqual(respon02.json()['tags'][0]['name'],'星标组')



if __name__=='__main__':
    unittest.main()
