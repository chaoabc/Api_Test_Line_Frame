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


    def test_create_user_tag(self):
        token_id =common_api.get_access_token_value()
        respon02 =common_api.create_user_tag(token_id, 'uu')
        self.assertEqual(respon02.json()['tags']['name'],'uu')


    # def test_create_repeat_user_tag(self):
    #     respon02 =common_api.create_user_tag(common_api.get_access_token_value, 'uu')
    #     self.assertEqual(respon02.json()['tags']['errcode'],'45157')
    #
    # def test_create_username_overlength_tag(self):
    #     respon02 =common_api.create_user_tag(common_api.get_access_token_value, 'asdasdddddeedddasdsd3ew问问是范德萨发生大的超过30个uu')
    #     self.assertEqual(respon02.json()['tags']['errcode'],'45158')
    #


if __name__=='__main__':
    unittest.main()
