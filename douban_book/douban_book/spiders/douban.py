import scrapy

class DmozSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "https://book.douban.com/people/xindoo/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
