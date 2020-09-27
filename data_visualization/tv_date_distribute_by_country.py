# -*- coding: utf-8 -*-
# @Time   : 2020/9/27 16:04
# @Author : laisent
"""
绘制3分以上的不同国家电视剧随时间的变化情况
"""
from data_visualization.show_data import get_data_frame
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


def show_tv_date_distribute(rate=3):
    """
    通过不同国家电视剧随时间的变化情况绘制折线图
    :param rate:
    :return:
    """
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    fig = plt.figure(figsize=(16, 8))
    ax = plt.subplot()
    # 获取数据
    df = get_data_frame()
    # 为现存的每条数据作出统计,即让其数量为1,方便之后分组后的聚合 构建全为1的Series
    count_df = pd.DataFrame(np.ones(shape=(len(df), 1)), columns=["count"])
    df = df.join(count_df)
    # 去除没有时间的电视剧
    # new_df = df[pd.notnull(df["release_date"])]
    # 选择2000年之后的电视剧
    # new_df = df[df["release_date"] > "19991231"]
    # 选择3分以上的上市局
    new_df = df[df["rating_value"] >= rate]
    # 不同国家的电视剧的数量和时间的对应关系并不相同,需要先统一统计的时间,没有的时间段填充0
    date_start = new_df["release_date"].min()
    date_end = new_df["release_date"].max()
    date_period = pd.DataFrame(pd.date_range(date_start, date_end, freq="D", ), columns=["release_date"])
    # 定义绘图的颜色
    colors = ['red', 'green', 'blue', "cyan", "orange"]
    country_list = new_df["country"].unique().tolist()
    # 分组
    for country, grouped in new_df.groupby(by=["country"]):
        # 对不同的国家添加统一的时间段,并设置为index
        temp_grouped = grouped.merge(date_period, how="outer", on="release_date")
        temp_grouped = temp_grouped[["release_date", "count"]].set_index("release_date")
        # 对空白的时间段填充0
        temp_grouped = temp_grouped.fillna(0)
        temp_grouped = temp_grouped.resample("3M").sum()
        # print(temp_grouped.index)
        _x = range(len(temp_grouped.index))
        _y = temp_grouped["count"]
        # 绘制散点图,但是效果不明显
        # ax.scatter(_x, _y,
        #            c=colors[country_list.index(country)],
        #            alpha=0.5,
        #            label=country
        #            )
        # 绘制折线图
        ax.plot(_x, _y,
                c=colors[country_list.index(country)],
                alpha=0.5,
                label=country
                )
    # 添加图例
    plt.legend()
    # 设置xticklable时间格式
    xticklables = [i.strftime('%Y-%m-%d') for i in temp_grouped.index]
    # 设置x轴刻度
    plt.xticks(range(len(temp_grouped.index)), xticklables, rotation=45)
    plt.xlabel("时间")
    plt.ylabel("时间段内的数量合计")
    plt.title("不同国家3分以上的电视剧随时间的变化情况")
    plt.savefig("不同国家3分以上的电视剧随时间的变化情况.png")
    plt.show()
