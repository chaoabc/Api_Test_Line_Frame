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

def get_access_token_value():
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


def delete_user_tag(token_value, tag_id):
    api_url = local_config.hosts + '/cgi-bin/tags/delete'
    get_param_data = {
        'access_token': token_value
    }
    data_info = {
        "tag": {"name": tag_id}
    }
    header_info = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url=api_url,
                             data=data_info,
                             params=get_param_data,
                             headers=header_info)
    return response

def update_user_tag(token_value, tag_id,tag_name):
    api_url = local_config.hosts + '/cgi-bin/tags/update'
    get_param_data = {
        'access_token': token_value
    }
    data_info = {
        "tag": {
            "id" : tag_id,
            "name": tag_name
        }
    }
    header_info = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url=api_url,

                             data=data_info,
                             params=get_param_data,
                             headers=header_info)
    return response


def selete_user_tag(token_value):
    api_url = local_config.hosts+'/cgi-bin/tags/get'
    get_param_data = {
        'access_token': token_value
    }
    response = requests.get(url= api_url,
                            params=get_param_data)
    return response

def set_user_mark(token_value, openid,remark):
    api_url = local_config.hosts + '/cgi-bin/user/info/updateremark'
    get_param_data = {
        'access_token': token_value
    }
    data_info = {
        "tag": {
            "openid" : openid,
            "remark": remark
        }
    }
    header_info = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url=api_url,
                             data=data_info,
                             params=get_param_data,
                             headers=header_info)
    return response


def get_user_massage(token_value,openid,lang):
    api_url = local_config.hosts+'/cgi-bin/user/info'
    get_param_data = {
        'access_token': token_value,
        'openid': openid,
        'lang': lang

    }
    response = requests.get(url= api_url,
                            params=get_param_data)
    return response



def get_p_user_massage(token_value,openid1,lang1,openid2,lang2):
    api_url = local_config.hosts+'/cgi-bin/user/info'
    get_param_data = {
        'access_token': token_value
    }
    data_info ={"user_list": [
                {
                    "openid": openid1,
                    "lang": lang1
                },
                {
                    "openid": openid2,
                    "lang": lang2
                }
            ]
    }

    response = requests.post(url= api_url,
                             data=data_info,
                             params=get_param_data)
    return response

if __name__=='__main__':
    unittest.main()


