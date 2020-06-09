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

    def test_set_user_mark(self):
        respon02 =common_api.set_user_mark(common_api.get_access_token_value, 'oDF3iY9ffA-hqb2vVvbr7qxf6A0Q','xiaochao')
        self.assertEqual(respon02.json()['errmsg'],'ok')

    def test_set_erruser_mark(self):
        respon02 =common_api.set_user_mark(common_api.get_access_token_value, 'oDF3iY9f2vVvbr7qxf6A0Q','xiaochao')
        self.assertEqual(respon02.json()['errcode'],'40013')




if __name__=='__main__':
    unittest.main()
