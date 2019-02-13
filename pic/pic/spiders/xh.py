# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from pic.items import PicItem

class XhSpider(CrawlSpider):
    name = 'xh'
    # 限制爬虫只在该域名下爬
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/list-1-1.html']
    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        # Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        # Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
        # callback不要使用默认的parse
        Rule(LinkExtractor(allow=('list-1-(\d)+\.html', )), callback='parse_item', follow=True),

    )
    def parse_item(self, response):
        allPics = response.xpath('//div[@class="img"]/a')
        for pic in allPics:
            item = PicItem()
            item['name'] = pic.xpath('./img/@alt').extract_first()
            item['addr'] = response.urljoin(pic.xpath('./img/@src').extract_first())
            print item['name']
            print item['addr']
            # 返回爬取到的数据
            yield item
        #
        # # 获取所有的地址链接
        # for url in response.xpath("//a/@href"):
        #     yield response.follow(url,callback=self.parse)
