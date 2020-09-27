# -*- coding: utf-8 -*-
# @Time   : 2020/9/25 12:19
# @Author : laisent
"""
豆瓣电视剧爬虫模块
"""
from spider.parse import parse_url
from spider.save import mongo_client
import json


class DoubanSpider(object):
    """
    爬取豆瓣电视剧信息
    """

    def __init__(self):
        """
        初始化模块
        """
        self.url_temp = "https://m.douban.com/rexxar/api/v2/subject_collection/{}/items?start={}&count=18"
        self.start_urls_temp = [
            {
                "tv_category": "chinese",
                "tv_url_parameter": "tv_domestic",
                "total_num": None
            },
            {
                "tv_category": "american",
                "tv_url_parameter": "tv_american",
                "total_num": None
            },
            {
                "tv_category": "korean",
                "tv_url_parameter": "tv_korean",
                "total": None
            },
            {
                "tv_category": "japanese",
                "tv_url_parameter": "tv_japanese",
                "total": None
            },
        ]

    def get_start_urls(self):
        """
        设置开始的url,获取初始的访问地址列表
        :return: items 初始访问地址列表
        """
        items = list()
        for item in self.start_urls_temp:
            item["parse_url"] = self.url_temp.format(item["tv_url_parameter"], 0)  # 构建初始url
            items.append(item)
        return items

    def get_content_list(self, html_str, item):
        """
        获取请求里面的每个电视剧的信息
        :param html_str: url解析后的html字符串
        :param item: 该电视剧的分类信息列表
        :return:
            content_list: 电视剧详细信息列表
            next_page_url: 下一个要请求的url地址
        """
        data = json.loads(html_str)
        if item.get("total") is None:
            item["total"] = data["total"]
        subject_collection_items = data["subject_collection_items"]
        content_list = []
        for item_temp in subject_collection_items:
            print(item_temp)
            item_temp.update(item)
            content_list.append(item_temp)
        now_page_start = data["start"]  # 当前url启动的时候的offsite
        if now_page_start < item["total"]:
            next_page_url = self.url_temp.format(item["tv_url_parameter"], now_page_start + 18)
        else:
            next_page_url = None
        return content_list, next_page_url

    def run(self):
        """
        主逻辑
        :return:
        """
        items = self.get_start_urls()
        print(items)
        for item in items:
            next_page_url = item["parse_url"]
            while next_page_url is not None:
                html_str = parse_url(next_page_url)
                print(html_str)
                content_list, next_page_url = self.get_content_list(html_str, item)
                mongo_client.save_to_db(content_list)


if __name__ == '__main__':
    douban_spider = DoubanSpider()
    douban_spider.run()
