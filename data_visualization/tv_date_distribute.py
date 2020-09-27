# -*- coding: utf-8 -*-
# @Time   : 2020/9/27 1:25
# @Author : laisent
"""
绘制3分以上的电视剧时间的分布的散点图
"""
from data_visualization.show_data import get_data_frame
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


def _show_tv_date_distribute(rate):
    """
    获取数据,设置时间索引,降采样
    :param rate: 最低分数
    :return: 筛选后的数据
    """
    # 获取数据
    df = get_data_frame()
    # 为现存的每条数据作出统计,即让其数量为1,方便之后分组后的聚合 创建全为1的DataFrame
    count_df = pd.DataFrame(np.ones(shape=(len(df), 1)), columns=["count"])
    df = df.join(count_df)
    # 去除没有时间的电视剧
    # new_df = df[pd.notnull(df["release_date"])]
    # 选择大于3分的电视剧
    new_df = df[df["rating_value"] >= rate]
    # 设置日期为索引
    new_df = new_df.set_index("release_date")
    # 只选择据中的count列
    new_df = new_df["count"]
    # 调整统计时间的范围,实现重新采样
    new_df = new_df.resample("5D").sum()
    return new_df


def show_tv_date_distribute(rate=3):
    """
    绘制散点图
    :param rate:
    :return:
    """
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    df = _show_tv_date_distribute(rate)
    df = pd.DataFrame(df, columns=["count"])
    fig = plt.figure(figsize=(16, 8))
    ax = plt.subplot()
    _x = range(len(df.index))
    _y = df["count"]

    ax.scatter(_x, _y, c="green", alpha=0.7, edgecolors='none')

    # 设置xticklable时间格式
    xticklables = [i.strftime('%Y-%m-%d') for i in df.index]
    # 设置x轴刻度
    plt.xticks(range(len(df.index)), xticklables, rotation=45)
    plt.xlabel("时间")
    plt.ylabel("时间段内的数量合计")
    plt.title("3分以上的电视剧时间的分布散点图")
    plt.savefig("3分以上的电视剧时间的分布散点图.png")

    plt.show()
