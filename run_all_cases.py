#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: run_all_cases.py
# @time: 2020/5/8 9:37 下午
import os
import time
import unittest
from utils.config_utils import local_config
import HTMLTestRunner

def get_testsuite(self):
    discover = unittest.defaultTestLoader.discover(start_dir='./testcases',
                                                   pattern='*_testcase.py',
                                                   top_level_dir='./testcases')
    all_suite = unittest.TestSuite()
    all_suite.addTest(discover)
    return all_suite


now = time.strftime('%Y_%m_%d_%H_%M_%S')
html_report = os.path.join(local_config.report_path, 'api_result_%s.html' % now)
file =open(html_report,'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                                 title='api测试',
                                                 description='接口测试描述',
                                                 tester='chaoge')
runner.run(get_testsuite)



if __name__ == '__main__':
    unittest.main()







