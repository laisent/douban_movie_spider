# -*- coding: utf-8 -*-
# @Time   : 2020/9/25 17:18
# @Author : laisent
"""
解析 url 模块
"""
from retrying import retry
from config import SPIDER_DEFAULT_HEADERS
import requests
import time


@retry(stop_max_attempt_number=3)
def _parse_url(url):
    """
    发送请求,获取响应
    :param url: 请求的 url 地址
    :return: 请求成功的html内容
    """
    response = requests.get(url, timeout=5, headers=SPIDER_DEFAULT_HEADERS)
    assert response.status_code == 200  # 断言 访问成功 不成功抛出异常
    return response.content.decode()


def parse_url(url):
    """
    解析 url 地址
    :param url: 请求的 url 地址
    :return: 请求成功的html内容
    """
    print("now parseing", url)
    try:
        time.sleep(0.4)
        html_str = _parse_url(url)
    except Exception as e:
        print(e)
        html_str = None
    return html_str
