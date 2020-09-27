# -*- coding: utf-8 -*-
# @Time   : 2020/9/25 19:03
# @Author : laisent
"""
爬虫启动入口
"""
from spider.douban_spider import DoubanSpider

if __name__ == '__main__':
    douban_spider = DoubanSpider()
    douban_spider.run()
