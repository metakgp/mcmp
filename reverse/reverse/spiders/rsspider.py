from scrapy.spider import Spider
from scrapy.selector import Selector
from reverse.items import ReverseItem
from scrapy.http import Request
import pickle



"""

### Scrapy code for scraping the list of all departments and schools :
### Usage:
### scrapy crawl reverse -o departments.json -t json

class MySpider(Spider):
    name = "reverse"
    allowed_domains = ["www.iitkgp.ac.in"]
    start_urls = ["http://www.iitkgp.ac.in/commdir3/various.php?division=3"]
    
    def parse(self, response):
        sel = Selector(response)
        titles = sel.xpath('//*/table')
        item = ReverseItem()
        item["title"] = titles.xpath('.//*/a/@href').extract()
        item["field"] = titles.xpath('.//*/a/text()').extract()

        return item 
        
"""

"""

### Scrapy code for scraping the list of all professors from various departments
### Usage
### scrapy crawl reverse -o professor.json -t json

class MySpider(Spider):
    name = "reverse"
    allowed_domains = ["www.iitkgp.ac.in"]
    deplinks = open("deplinks.pkl", 'rb')

    start_urls = pickle.load(deplinks)
    
    def parse(self, response):
        sel = Selector(response)
        titles = sel.xpath('//*/table')
        item = ReverseItem()
        items = []

        for title in titles:
            item["title"] = title.xpath('.//*/a/@href').extract()
            item["field"] = title.xpath('.//*/a/text()').extract()
            items.append(item)
        return items
"""

### Scrapy code for scraping the research areas of the various professors
### Usage :
### scrapy crawl reverse -o research_areas.json -t json

class MySpider(Spider):
    name = "reverse"
    allowed_domains = ["www.iitkgp.ac.in"]
    proflinks = open("proflinks.pkl", 'rb')

    start_urls = pickle.load(proflinks)
    items = []

    def parse(self, response):
        sel = Selector(response)
        items = []
        titles = sel.xpath('//*[@id="contents"]/fieldset')
        item = ReverseItem()
        item["title"] = response.url
        item["field"] = titles[2].xpath('.//ul/li/text()').extract()
        item["name"] = str((titles[0].xpath("string((.//table/tr/td[2]//text())[1])").extract())[0])
        items.append(item)
        return items




