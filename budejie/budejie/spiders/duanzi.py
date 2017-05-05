import scrapy

class Duanzi(scrapy.Spider):
    name = 'duanzi'

    def start_requests(self):
        urls = ['http://www.budejie.com/text/']

        for url in urls:
            request = scrapy.Request(url=url, callback=self.parse)
            yield request

    def parse(self, response):
        txtList = [i for i in response.css('div.j-r-list-c-desc')]
        txtList = [' '.join(i.css('a::text').extract()) for i in txtList]
        txts = '\n\n'.join(txtList)
        with open('duanzi.txt', 'w', encoding='utf8') as f:
            f.write(txts)
