# -*- coding: utf-8 -*-
import scrapy
from pic.items import PicItem


class XhSpider(scrapy.Spider):
    name = 'xh'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/list-1-1.html']

    def parse(self, response):
        allPics = response.xpath('//div[@class="img"]/a')
        for pic in allPics:
            item = PicItem()
            item['name'] = pic.xpath('./img/@alt').extract_first()
            item['addr'] = response.urljoin(pic.xpath('./img/@src').extract_first())
            print item['name']
            print item['addr']
            # 返回爬取到的数据
            yield item

        # 获取所有的地址链接
        for url in response.xpath("//a/@href"):
            yield response.follow(url,callback=self.parse)



