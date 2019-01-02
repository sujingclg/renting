# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AnjukeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    house_type = scrapy.Field()
    area = scrapy.Field()
    floor = scrapy.Field()
    seller = scrapy.Field()
    address = scrapy.Field()
    street = scrapy.Field()
