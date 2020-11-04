import scrapy
from ..items import Douban250Item

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']

    start = 0
    end = '&filter='
    url = 'https://movie.douban.com/top250?start='
    start_urls = [url + str(start) + end]

    def parse(self, response):
        item = Douban250Item()
        lists = response.xpath('//li/div[@class="item"]')
        for list in lists:
            item['title'] = list.xpath('./div[@class="info"]/div[@class="hd"]/a/span[@class="title"]/text()').get()
            item['other'] = list.xpath('./div[@class="info"]/div[@class="hd"]/a/span[@class="other"]/text()').get()
            item['info'] = list.xpath('./div[@class="info"]/div[@class="bd"]/p/text()').get()
            item['score'] = list.xpath('./div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').get()
            item['detail_href'] = list.xpath('./div[@class="pic"]/a/@href').get()
            item['img_url'] = list.xpath('./div[@class="pic"]/a/img/@src').get()
            yield item

        if self.start <= 255:
            self.start += 25
            yield scrapy.Request(self.url + str(self.start) + self.end, callback=self.parse)


