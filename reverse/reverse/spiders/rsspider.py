from scrapy.spider import Spider
from scrapy.selector import Selector
from reverse.items import ReverseItem
from scrapy.http import Request
import pickle
import re



# class MySpider(Spider):
#     """
#     Scrapy code for scraping the list of all departments and schools :
#     Usage:
#     scrapy crawl reverse -o departments.json -t json
#     """
#
#     name = "reverse"
#     allowed_domains = ["www.iitkgp.ac.in"]
#     start_urls = ["http://www.iitkgp.ac.in/commdir3/various.php?division=3"]
#
#     def parse(self, response):
#         sel = Selector(response)
#         titles = sel.xpath('//*/table')
#         item = ReverseItem()
#         item["title"] = titles.xpath('.//*/a/@href').extract()
#         item["field"] = titles.xpath('.//*/a/text()').extract()
#
#         return item
#
#
# class MySpider(Spider):
#     """
#     Scrapy code for scraping the list of all professors from various departments
#     Usage
#     scrapy crawl reverse -o professor.json -t json
#
#     """
#     name = "reverse"
#     allowed_domains = ["www.iitkgp.ac.in"]
#     deplinks = open("deplinks.pkl", 'rb')
#
#     start_urls = pickle.load(deplinks)
#
#     def parse(self, response):
#         sel = Selector(response)
#         titles = sel.xpath('//*/table')
#         item = ReverseItem()
#         items = []
#
#         for title in titles:
#             item["title"] = title.xpath('.//*/a/@href').extract()
#             item["field"] = title.xpath('.//*/a/text()').extract()
#             items.append(item)
#         return items


class MySpider(Spider):
    """
    Scrapy code for scraping the research areas of the various professors
    Usage :
    scrapy crawl reverse -o research_areas.json -t json
    """

    name = "reverse"
    allowed_domains = ["www.iitkgp.ac.in"]
    proflinks = open("proflinks.pkl", 'rb')

    start_urls = pickle.load(proflinks)
    items = []

    def parse(self, response):

        sel = Selector(response)
        titles = sel.xpath('//*[@id="contents"]/fieldset')
        items = []
        item = ReverseItem()
        item["link"] = response.url
        item["field"] = titles[2].xpath('.//ul/li/text()').extract()

        header_txt = titles[0].xpath("string((.//table/tr/td[2]))")[0].extract()
        re_year = re.compile('\d{4,4}')  # Match four digits
        re_dept = re.compile('Professor,[\s\w&]*')
        item["year"] = re_year.findall(header_txt)[0]
        item["dept"] = re_dept.findall(header_txt)[0].split('\n')[0].lstrip('Professor,').lstrip().rstrip()

        name = str((titles[0].xpath("string((.//table/tr/td[2]//text())[1])").extract())[0])
        item["name"] = name.lstrip().rstrip()
        items.append(item)

        item["image_src"] = "http://iitkgp.ac.in" + sel.xpath('//table//img/@src').extract_first()

        info_items = titles[1].xpath('//td/text()').extract()
        if "email" in info_items:
            item["email"] = info_items[info_items.index('email')+1].strip().replace(' ', '')
        else:
            item["email"] = ""

        if "Personal web page" in info_items:
            item["website"] = titles[1].xpath('//td//a/@href').extract_first()
        else:
            item["website"] = ""

        return items
