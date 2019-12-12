from .mongodb import collection
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


# mongo_db 설정
class ComicsPipeline(object):

    def process_item(self, item, spider):
        
        data = {
            "title": item["title"], 
            "date": item["date"],
            "views": item["views"], 
            "recommend": item["recommend"],
            "link": item["link"],
            "img_count": item["img_count"],
            "img_link": item["img_link"],
               }
        collection.insert(data)
        return item

# image download
class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(url=image_url, headers={'Referer':item['link']})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item
