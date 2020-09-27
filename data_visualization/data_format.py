# -*- coding: utf-8 -*-
# @Time   : 2020/9/26 0:00
# @Author : laisent
"""
格式化数据
"""
from config import MONGO_PORT, MONGO_HOST, MONGO_DB, MONGO_COLLECTION
from pymongo import MongoClient


def choose_date():
    """
    筛选出MongoDB中有用的数据
    :return: 提取后的有用数据
    """
    client = MongoClient(host=MONGO_HOST, port=MONGO_PORT)
    collection = client[MONGO_DB][MONGO_COLLECTION]
    db_data = collection.find()
    data_list = list()

    for data in db_data:
        item = dict()
        # 国家
        item["country"] = data["tv_category"]
        # 电视剧的名字
        item["title"] = data["title"]
        # 导演
        item["directors"] = "_".join(data["directors"])
        # 演员
        item["actors"] = "_".join(data["actors"])
        # 提取时间 'year': '2020'  'release_date': '09.16'
        temp_date = data["release_date"].split(".")
        item["release_date"] = "{}-{}-{}".format(data["year"], temp_date[0], temp_date[1])
        # 提取分类tag
        tv_info = data["info"].split("/")[1].strip()
        item["tag"] = tv_info if len(tv_info) > 0 else "未知"

        if data["rating"] is not None:
            # 打分的人数
            item["rating_count"] = data["rating"]["count"]
            # 分数
            item["rating_value"] = data["rating"]["value"]
        else:
            # 打分的人数
            item["rating_count"] = "未知"
            # 分数
            item["rating_value"] = "未知"
        data_list.append(item)

    return data_list
