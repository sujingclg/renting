# -*- coding: utf-8 -*-
import scrapy
from renting.items import AnjukeItem


class AnjukeSpider(scrapy.Spider):
    name = 'anjuke'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://bj.zu.anjuke.com/fangyuan/chaoyang/x1/']
    # allowed_domains = ['httpbin.org']
    # start_urls = ['http://httpbin.org/get']

    def parse(self, response):
        houses = response.css('div#list-content>div.zu-itemmod')
        for house in houses:
            item = AnjukeItem()
            zu_info = house.css('.zu-info')
            item['title'] = zu_info.css('h3 a::attr(title)').extract_first()
            item['href'] = zu_info.css('h3 a::attr(href)').extract_first()
            details_tag = zu_info.css('.details-item.tag::text').extract()
            item['house_type'] = details_tag[0].strip()
            item['area'] = details_tag[1]
            item['floor'] = details_tag[2]
            item['seller'] = details_tag[3].strip()
            item['address'] = zu_info.css('address a::text').extract_first()
            item['street'] = zu_info.css('address::text').extract()[1].strip()
            yield item

