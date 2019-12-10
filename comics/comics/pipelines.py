from .mongodb import collection

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
