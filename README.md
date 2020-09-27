# 豆瓣电视剧爬虫

## 简介

​		爬取豆瓣电视剧分类下的 国产剧，英美剧，日剧，韩剧接口数据，保存到本地MongoDB数据库。读取MongoDB内容，筛选出有用的信息，使用pandas模块接受并分析，最后通过matplotlib显示并保存到本地。

## 目录结构

## 目录结构

- data_visualization:数据可视化模块
  - data_foramat.py:从数据库提取文件，格式化数据
  - show_data.py:分析四个国家电视剧的平均分
  - tag_count.py:不同分类的电视剧数量的统计
  - tv_date_distribute.py:绘制3分以上的电视剧时间的分布的散点图
  - tv_date_distribute_by_country.py:绘制3分以上的不同国家电视剧随时间的变化情况
- spider:爬虫模块
  - douban_spider.py:豆瓣电视剧爬虫模块
  - parse.py:解析 url 模块
  - save.py:保存数据到本地MongoDB数据库

- config.py:配置文件
- data_visualization.sh:可视化脚本
- spider_shell.sh:启动爬虫脚本

- start_spider.py:启动爬虫文件
- test.py:测试可视化模块文件
- requirements.txt:需求模块

## 执行流程

- ./spider_shell.sh  (启动脚本，爬取电视剧信息并且保存到本地数据库)
- ./data_visualization.sh   (使用pandas处理数据并且通过图形显示出来)

  
