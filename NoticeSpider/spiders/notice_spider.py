# -*- coding: utf-8 -*-
import scrapy
from NoticeSpider.items import NoticespiderItem


class NoticeSpiderSpider(scrapy.Spider):
    name = 'notice_spider'
    allowed_domains = ['journal.whu.edu.cn']
    start_urls = ['http://www.journal.whu.edu.cn/notice/index']

    def parse(self, response):
        item = NoticespiderItem()
        items = []
        # 总共有20个li，也就是20个通知
        li_list = response.xpath("//div[@id='center_subcontent']/ul/li")
        for li in li_list:
            # 拼接成通知详情页地址
            detail_url = "http://www.journal.whu.edu.cn" + li.xpath("./a/@href").extract_first()
            items.append(item)
            for item in items:
                yield scrapy.Request(url=detail_url, meta={'meta_detail': item}, callback=self.parse_detail)

    def parse_detail(self, response):
        item = response.meta['meta_detail']
        item['title'] = response.xpath("//div[@id='news_title']/p/text()").extract_first()
        item['content'] = response.xpath("string(//div[@id='news_subcontent'])").extract_first()
        yield item
