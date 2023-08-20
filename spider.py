'''
Виконати парсинг ресурсу  за допомогою scrapy https://quotes.toscrape.com/
Дістати всі тексти і їх авторів
(на всіх сторінках)
'''
import scrapy


class StoreSpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['https://quotes.toscrape.com']


def parse(self, response):
    for link in response.css("div.quote"):
        yield response.follow(link, self.parse_page)

    for next_page in response.css("div.quote"):
        yield response.follow(next_page, self.parse)


def parse_page(self, response):
    yield {"text": response.css("span.autor::text").get().strip(),
           "author": response.css("span.small::text").get().strip()}


'''
    def parse(self, response):
        for quote in response.css("div.qute"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("span small::text").get(),
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
'''
