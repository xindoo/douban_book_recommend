import scrapy

class DmozSpider(scrapy.Spider):
    urlset = set()
    name = "douban"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "https://www.douban.com/people/xindoo/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
        friendhtml = response.xpath(".//div[@id='friend']")
        friendurls = friendhtml.xpath(".//dl")
        for urlhtml in friendurls:
            url = urlhtml.xpath(".//a/@href").extract()[0]
            print url
            if url not in self.urlset:
                print url
                self.urlset.add(url)
                yield scrapy.Request(url, callback=self.parse)
