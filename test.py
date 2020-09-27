# -*- coding: utf-8 -*-
# @Time   : 2020/9/26 0:52
# @Author : laisent
'''
测试模块
'''
# from data_visualization.data_format import choose_date
# df = choose_date()
# print(df)
from data_visualization.show_data import plot_four_country_ave_rating_value
from data_visualization.tag_count import show_tag_count
from data_visualization.tv_date_distribute import show_tv_date_distribute

plot_four_country_ave_rating_value()
show_tag_count()
show_tv_date_distribute()

from data_visualization.tv_date_distribute_by_country import show_tv_date_distribute
show_tv_date_distribute()
