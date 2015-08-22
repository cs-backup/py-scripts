import scrapy

from packt.items import PacktItem

#//a[@class='twelve-days-claim']/@href
class PacktSpider(scrapy.Spider):
    name = "packt"
    allowed_domains = ["packtpub.com"]
    start_urls = ["https://www.packtpub.com/packt/offers/free-learning/?utm_source=twitter&utm_medium=social&utm_campaign=FL20153"]

    def parse(self, response):
        item = PacktItem()
        item['bookTitle'] = response.xpath('//*[@id="deal-of-the-day"]/div/div/div[2]/div[2]/h2/text()').extract()
        item['endingTime'] = response.xpath('//*[@id="deal-of-the-day"]/div/div/div[2]/div[1]/span').extract()
        item['bookDescription'] = response.xpath('//*[@id="deal-of-the-day"]/div/div/div[2]/div[3]/text()').extract()
        yield item
        