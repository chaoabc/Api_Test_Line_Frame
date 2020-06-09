#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: run_all_cases.py
# @time: 2020/5/8 9:37 下午
import os
import time
import unittest
# import HTMLTestRunner
from utils  import HTMLTestReportCN
from utils.config_utils import local_config

def get_testsuite():
    discover = unittest.defaultTestLoader.discover(start_dir='./testcases',
                                                   pattern='*_testcase.py',
                                                   top_level_dir='./testcases')
    all_suite = unittest.TestSuite()
    all_suite.addTest(discover)
    return all_suite


# 生成报表方式一
# now = time.strftime('%Y_%m_%d_%H_%M_%S')
# html_report = os.path.join(local_config.report_path, 'api_result_%s.html' % now)
# file =open(html_report,'wb')
# runner = HTMLTestRunner.HTMLTestRunner(stream=file,
#                                        title='api测试',
#                                        description='接口测试描述',
#                                         )
# runner.run(get_testsuite())
# file.close()

# 生成报表方式二

report_dir = HTMLTestReportCN.ReportDirectory(local_config.report_path+'/')
report_dir.create_dir('api测试')
dir_path = HTMLTestReportCN.GlobalMsg.get_value('dir_path')
report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
fp = open(report_path,'wb')
runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                         title='api测试',
                                         description='接口测试描述',
                                         tester='xiaochao')
runner.run(get_testsuite())
fp.close()






