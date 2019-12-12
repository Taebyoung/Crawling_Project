import scrapy
import time
from comics.items import ComicsItem
from scrapy.pipelines.images import ImagesPipeline

class ComicsSpider(scrapy.Spider):
    name = "Comics"
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES' : {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
        }
    }
    
    def __init__(self, pages=1, **kwargs):
        self.start_url = "https://gall.dcinside.com/board/lists/?id=comic_new2&page={}&exception_mode=recommend".format(pages)
        super().__init__(**kwargs)
        
    def start_requests(self):
        url = self.start_url
        yield scrapy.Request(url, callback=self.parse)
        
    def parse(self, response):
        links = response.xpath('//*[@class="ub-content us-post"]/td[2]/a[1]/@href').extract()
        links = list(map(response.urljoin, links))
        for link in links:
            yield scrapy.Request(link, callback=self.page_parse)
    
    def page_parse(self, response):
        item = ComicsItem()
        #title = response.xpath('//*[@class="gallview_head clear ub-content"]/h3/span[2]/text()').extract_first()
        item["title"] = response.xpath('//*[@class="gallview_head clear ub-content"]/h3/span[2]/text()').extract_first()
        item["date"] = response.xpath('//*[@class="gall_date"]/text()').extract_first()
        item["views"] = response.xpath('//*[@class="fr"]/span[1]/text()').extract_first()[3:]
        item["recommend"] = response.xpath('//*[@class="gall_reply_num"]/text()').extract_first()[3:]
        item["link"] = response.url
            
        try:
            try:
                # for DB
                item["img_link"] = response.xpath('//*[@style="overflow:hidden;"]/p/img/@src').extract()[0]
                item["img_count"] = len(response.xpath('//*[@style="overflow:hidden;"]/p/img/@src').extract())
                item["image_urls"] = response.xpath('//*[@style="overflow:hidden;"]/p/img/@src').extract()
                               
                #for Images
                #images = []
                #img_urls = response.xpath('//*[@style="overflow:hidden;"]/p/img/@src').extract()
                #img_count = len(response.xpath('//*[@style="overflow:hidden;"]/p/img/@src').extract())
                
                #img_names = [ title + "_" + str(n) for n in range(img_count)]
                #for image_url, image_name in zip(img_urls, img_names):
                #    images.append({'url': image_url, 'name': image_name})
                #
                #item["image_urls"] = images
            except:
                pass
        
            try:
                # for DB
                item["img_link"] = response.xpath('//*[@style="overflow:hidden;"]/a/@href').extract()[0]
                item["img_count"] = len(response.xpath('//*[@style="overflow:hidden;"]/a/@href').extract())
                item["image_urls"] = response.xpath('//*[@style="overflow:hidden;"]/a/@href').extract()
                               
                # for Images
                #images = []
                #img_urls = response.xpath('//*[@style="overflow:hidden;"]/a/@href').extract()
                #img_count = len(response.xpath('//*[@style="overflow:hidden;"]/a/@href').extract())
                #
                #img_names = [ title + "_" + str(n) for n in range(img_count)]
                #for image_url, image_name in zip(img_urls, img_names):
                #    images.append({'url': image_url, 'name': image_name})
                #
                #item["image_urls"] = images
            except:
                pass
        except:
            item["img_count"] = "0"
            item["img_link"] = ""
        
        time.sleep(1) # 게시물 check 딜레이
        
        yield item
