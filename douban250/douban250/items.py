# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Douban250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field() #标题
    other = scrapy.Field() #别名
    info = scrapy.Field()  #演员信息
    score = scrapy.Field() #评分
    # tags = scrapy.Field()  #标签
    detail_href = scrapy.Field()  #链接
    img_url = scrapy.Field() #图片地址