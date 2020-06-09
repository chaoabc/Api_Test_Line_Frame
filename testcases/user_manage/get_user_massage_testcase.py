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


    def test_get_user_massage(self):
        respon02 =common_api.get_user_massage(common_api.get_access_token_value, 'otvxTs4dckWG7imySrJd6jSi0CWE','zh_CN ')
        self.assertEqual(respon02.json()['openid'],'otvxTs4dckWG7imySrJd6jSi0CWE')


    def test_geterr_user_massage(self):
        respon02 =common_api.get_user_massage(common_api.get_access_token_value, 'otvxTs4dckWG7imySrJd6jSi0E','zh_CN')
        self.assertEqual(respon02.json()['errcode'],'40013')




if __name__=='__main__':
    unittest.main()
