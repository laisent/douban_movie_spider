# -*- coding: utf-8 -*-
# @Time   : 2020/9/26 15:49
# @Author : laisent
"""
分析四个国家电视剧的平均分
"""
from data_visualization.data_format import choose_date
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


def get_data_frame():
    """
    从数据库获取数据,并且把release_date变成时间格式
    :return:
    """
    temp_df = pd.DataFrame(choose_date())
    # 去除暂时无评分的数据
    temp_df = temp_df[~temp_df["rating_value"].isin(["未知"])]
    # 清除后 更改index 利于合并
    temp_df.index = pd.Series(np.arange(len(temp_df)))
    temp_df["release_date"] = pd.to_datetime(temp_df["release_date"])
    return temp_df


def plot_four_country_ave_rating_value():
    """
    绘制四个国家电视剧的平均分
    :return:
    """
    # 设置图形大小
    plt.figure(figsize=(20, 10), dpi=80)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    ax = plt.subplot()
    df = get_data_frame()
    df_country_rating = df[["country", "rating_value"]]
    # 修改类型
    df_country_rating["rating_value"] = df_country_rating["rating_value"].astype("float")
    # 根据国家分组,并且获取平均值
    grouped_rating = df_country_rating.groupby("country").mean()
    y = grouped_rating["rating_value"]
    x = np.arange(len(grouped_rating.index))
    ax.bar(x, y, width=0.5, align="center")
    plt.xticks(x, grouped_rating.index)
    # x轴的值
    plt.xlabel("国家")
    # y轴值
    plt.ylabel("平均分")
    # 图的标题
    plt.title("豆瓣电视剧平均分统计")
    plt.savefig("各个国家豆瓣电视剧平均分统计.png")
    plt.show()

