# -*- coding: utf-8 -*-
# import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from douban.items import DoubanItem

class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/小说']

    rules = [
        Rule(LinkExtractor(allow=("subject/\d+[/]$")), callback='parse_item'),
        Rule(LinkExtractor(allow=("tag/小说[^/]+$", )), follow=True),
        #Rule(sle(allow=("/tag/$", )), follow=True),
        # Rule(LinkExtractor(allow=('list-1-(\d)+\.html',)), callback='parse_item', follow=True),
    ]

    def parse_item(self, response):
        item = DoubanItem()
        self.get_name(item,response)
        self.get_score(item,response)
        self.get_votes(item,response)
        self.get_author(item,response)
        self.get_publisher(item,response)
        # show
        self.show(item)
        yield item

    def show(self,item):
        for itm in item:
            self.log("%s"%item[itm])

    def get_name(self, meta, response):
        regx = '//title/text()'
        data = response.xpath(regx).getall()
        if data:
            meta['name'] = data[0][:-5].strip()
        return meta

    def get_score(self, meta, response):
        regx = '//strong[@property="v:average"]/text()'
        data = response.xpath(regx).getall()
        if data:
            score = data[0].strip()
            if score:
                meta['douban_score'] = score
        return meta

    def get_votes(self, meta, response):
        regx = '//span[@property="v:votes"]/text()'
        data = response.xpath(regx).getall()
        if data:
            votes = data[0].strip()
            if votes:
                meta['douban_votes'] = votes
        return meta

    def get_author(self, meta, response):
        regx = u'//*[@id="info"]/a[1]/text()'
        authors = response.xpath(regx).getall()
        if authors:
            meta['authors'] = '/'.join((i.strip() for i in authors))
        return meta

    def get_publisher(self, meta, response):
        regx = u'//text()[preceding-sibling::span[text()="出版社:"]][following-sibling::br]'
        data = response.xpath(regx).getall()
        if data:
            meta['publisher'] = data[0]
        return meta