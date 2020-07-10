from scrapy import Spider
from scrapy.selector import Selector

from googlenews.items import GooglenewsItem


class GnewsSpider(Spider):

    name = "googlenews"
    allowed_domains = ["google.com"]
    start_urls = [
        "https://www.google.com/search?q=site:bloomberg.com&tbs=sbd:1,qdr:h&tbm=nws&sxsrf=ALeKk03o_L4QOpDVk8ZNaNdfPJBUKk2rYA:1592577159637&source=lnt&sa=X&ved=0ahUKEwiXroKfjI7qAhVHasAKHcXCAwoQpwUIJA&biw=1551&bih=1017&dpr=0.9"
    ]

    # def parse(self, response):
    #     headlines = Selector(response).xpath(
    #         '//*[@id="main"]/div[4]/div/div[1]')
    #     for headline in headlines:
    #         item = GooglenewsItem()
    #         item['title'] = headline.xpath(
    #             'a/h3/div/text()').extract()[0]
    #         item['url'] = headline.xpath(
    #             'a/@href').extract()[0]
    #         yield item

    def parse(self, response):
        headlines = Selector(response).xpath(
            '//*[@id="main"]/div').getall()
        for headline in headlines:
            item = GooglenewsItem()
            item['title'] = headline.xpath(
                'a/h3/div/text()').extract()[0]
            item['url'] = headline.xpath(
                'a/@href').extract()[0]
            yield item
