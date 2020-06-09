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

    def test_update_user_tag(self):
        respon02 =common_api.update_user_tag(common_api.get_access_token_value, '109','109标签')
        self.assertEqual(respon02.json()['errmsg'],'ok')

    def test_update_repeat_user_tag(self):
        respon02 =common_api.update_user_tag(common_api.get_access_token_value, '109')
        self.assertEqual(respon02.json()['tags']['errcode'],'45157')


    def test_cant_update_user_tag(self):
        respon =common_api.update_user_tag(common_api.get_access_token_value, '2')
        self.assertEqual(respon.json()['errcode'],'45058')



if __name__=='__main__':
    unittest.main()
