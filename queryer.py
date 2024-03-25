#!/usr/bin/env python3
import requests
import json
__author__ = "Corsin Camichel"
__copyright__ = "Copyright 2020, Corsin Camichel"
__license__ = "Creative Commons Attribution-ShareAlike 4.0 International License."
__version__ = "1.0"
__email__ = "cocaman@gmail.com"


def query_malware(query_type='tag', query_string='TrickBot', limit=10,verbose=False):
    """
    查询bazzar上的样本信息
    :param query_type:tag/signature 对应标签和签名
    标签tag可以存在多个用于描述样本，signature通常只有一个，即恶意软件的家族
    :param query_string: 具体要查询的字段，可参考
    https://bazaar.abuse.ch/api/ 和 https://bazaar.abuse.ch/browse/
    :param limit: 返回数据的数量，最大1000
    :param verbose: 是否打查询信息
    :return:
    """
    sha256_list=[]
    if query_type == "tag":
        data = {
            'query': 'get_taginfo',
            'tag': '' + query_string + '',
            'limit': limit
        }
    else:
        data = {
            'query': 'get_siginfo',
            'signature': '' + query_string + '',
            'limit': limit
        }

    response = requests.post('https://mb-api.abuse.ch/api/v1/', data=data, timeout=15)
    json_response = response.content.decode("utf-8", "ignore")
    json_response=json.loads(json_response).get('data',[])

    if verbose:
        print(json_response)

    for each_sample in json_response:
        sha256_list.append(each_sample.get("sha256_hash",""))
    return sha256_list


if __name__ == "__main__":
    print(query_malware(query_type='tag', query_string='TrickBot', limit=10,verbose=False))
