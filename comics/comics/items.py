
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ComicsItem(scrapy.Item):
    # define the fields for your item here like:
    # mongo-db
    title = scrapy.Field()
    date = scrapy.Field()
    views = scrapy.Field()
    recommend = scrapy.Field()
    link = scrapy.Field()
    img_count = scrapy.Field()
    img_link = scrapy.Field()
    
    # downloads
    image_urls = scrapy.Field()
    images = scrapy.Field()
