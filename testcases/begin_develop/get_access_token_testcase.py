#!/usr/bin/env python
# encoding: utf-8
# @author: miaoxiaochao
# @file: create_tag_testcase.py
# @time: 2020/6/7 11:12 上午
#@desc:
import requests
import unittest
from utils.config_utils import local_config
from utils  import common_api

class APITest(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts =local_config.hosts
    def tearDown(self) -> None:
        pass

    def test_token(self):
        response01 = common_api.get_access_token('client_credential', 'wx116dfe67cf36b5db', '4fa8e58c98667a8f5cdb1f397d0290d1')
        # self.assertEqual(response01.content.decode('utf-8').__contains__('access_token'), True)
        self.assertEqual(response01.json()['expires_in'],7200)

if __name__=='__main__':
    unittest.main()
