# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrappingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class QuotesItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    tag_names = scrapy.Field()
    tag_links = scrapy.Field()
    price = scrapy.Field()
