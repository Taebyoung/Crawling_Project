
# Scrapy settings for comics project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'comics'

SPIDER_MODULES = ['comics.spiders']
NEWSPIDER_MODULE = 'comics.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'comics (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


# Configure item pipelines
ITEM_PIPELINES = {
    'comics.pipelines.ComicsPipeline': 300,
    'scrapy.pipelines.images.ImagesPipeline': 1
}

# Configure download
IMAGES_STORE = 'images'

# 다운로드 딜레이
DOWNLOAD_DELAY = 1 
