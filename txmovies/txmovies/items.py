# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TxmoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    video_title = scrapy.Field()  # 电影名
    figure_desc = scrapy.Field()  # 主演人员
    figure_count = scrapy.Field() # 播放次数
    video_tags = scrapy.Field()   # 标签
    video_sum = scrapy.Field()    # 简介
    video_href = scrapy.Field()   # 播放链接
    video_pic = scrapy.Field()    # 电影头图
