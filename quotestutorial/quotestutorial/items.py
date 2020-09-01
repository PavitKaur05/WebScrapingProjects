# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

#Extracted Data-> Temporary Containers-> Databases/File Systems
import scrapy


class QuotestutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    author=scrapy.Field()
    tags=scrapy.Field()