#!/usr/bin/env python
# encoding: utf-8
# @author: miaoxiaochao
# @file: common_api.py
# @time: 2020/6/7 11:04 上午
#@desc:

import requests
import unittest
from   utils.config_utils import local_config

def get_access_token(grant_type,appid,secret):
    api_url = local_config.hosts+'/cgi-bin/token'
    get_param_data = {
        'grant_type': grant_type,
        'appid': appid,
        'secret': secret

    }
    response = requests.get(url= api_url,
                            params=get_param_data)
    return response

def get_access_token_value(self):
    response_obj=get_access_token('client_credential','wx116dfe67cf36b5db','4fa8e58c98667a8f5cdb1f397d0290d1')
    return response_obj.json()['access_token']

def create_user_tag(token_value,tag_name):
    api_url = local_config.hosts + '/cgi-bin/tags/create'
    get_param_data = {
        'access_token': token_value
    }
    data_info ={
                "tag":{"name":tag_name }
    }
    header_info ={
              'Content-Type':'application/json'
    }
    response = requests.post(url=api_url,
                            data=data_info,
                            params =get_param_data,
                            headers =header_info)
    return response



if __name__=='__main__':
    unittest.main()

