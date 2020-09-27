# -*- coding: utf-8 -*-
# @Time   : 2020/9/26 20:26
# @Author : laisent
"""
不同分类的电视剧数量的统计
"""
from data_visualization.show_data import get_data_frame
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


def show_tag_count():
    """
    统计不同分类的电视剧数量
    :return:
    """
    # 设置图形大小
    plt.figure(figsize=(10, 8), dpi=80)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    df = get_data_frame()
    # 去除暂时无分类的数据
    df = df[~df["tag"].isin(["未知"])]
    df_tag = df[["country", "rating_value", "tag"]]

    # 切割组成集合,tags是一个带集合的列表
    tags = [set(x.split(" ")) for x in df_tag["tag"]]
    # 把所有的tag组成一个集合
    tags = set.union(*tags)
    # 设置一个(len(df_tag), len(tags))的全是0元素的二维数组 (行, 列)
    dummies = pd.DataFrame(np.zeros((len(df_tag), len(tags))), columns=tags)

    for i, tag in enumerate(df_tag["tag"]):
        # 对应位置改为 1
        dummies.loc[i, tag.split(" ")] = 1
    # df_new = df_tag.join(dummies.add_prefix("tag_")) #添加join之后字段的前缀
    # # 清除后 更改index 利于合并
    # df_tag.index = pd.Series(np.arange(len(df_tag)))
    df_new = df_tag.join(dummies)
    # print(df_new.columns)
    tag_list = df_new.columns[4:]
    tag_count = []
    for tag in tag_list:
        tag_count.append([tag, df_new[tag].sum()])
    # 排序,让柱状图按照顺序显示
    tag_count.sort(key=lambda x: x[1], reverse=True)
    ax = plt.subplot()
    # 画竖着的直方图
    # ax.bar(range(len(tag_list)), count, width=0.5, align="center",)
    # plt.xticks(range(len(tag_list)), tag_list,rotation=90,fontproperties=myfont)
    # 画横着的直方图
    ax.barh(range(len(tag_count)), [i[1] for i in tag_count], align="center", color='#EE7600', ecolor='black')
    plt.yticks(range(len(tag_count)), [i[0] for i in tag_count])

    plt.ylabel("分类")
    # y轴值
    plt.xlabel("数量")
    # 图的标题
    plt.title("不同分类电视剧的数量统计")
    plt.savefig("不同分类电视剧的数量统计.jpg")
    plt.show()
