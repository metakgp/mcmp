# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class ReverseItem(scrapy.Item):
    # define the fields for your item here like:
    name = Field()
    link = Field()
    field = Field()
    dept = Field()
    year = Field()
    email = Field()
    website = Field()
    image_src = Field()
