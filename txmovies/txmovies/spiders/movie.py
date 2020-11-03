import scrapy
from ..items import TxmoviesItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['https://v.qq.com']
    start_urls = ['https://v.qq.com/channel/movie?listpage=1&channel=movie&sort=18&_all=1']

    def parse(self, response):
        items = TxmoviesItem()
        lists = response.xpath('//div[@class="list_item"]')   # 每个电影列表
        for i in lists:
            items['video_title'] = i.xpath('./a/@title').get() # list_item 下的a标签的title属性
            items['figure_desc'] = i.xpath('./div/div/@title').get() # 主演
            items['figure_count'] = i.xpath('./div[@class="figure_count"]/text()').get() # 播放次数
            yield items
