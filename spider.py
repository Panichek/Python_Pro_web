'''
Виконати парсинг ресурсу  за допомогою scrapy https://quotes.toscrape.com/
Дістати всі тексти і їх авторів
(на всіх сторінках)
'''
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"
    start_urls = (
        'http://quotes.toscrape.com/',
    )

    def parse(self, response):
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            author = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()

            yield {'Text': text,
                   'Author': author}

        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)
