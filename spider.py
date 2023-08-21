'''
Виконати парсинг ресурсу  за допомогою scrapy https://quotes.toscrape.com/
Дістати всі тексти і їх авторів
(на всіх сторінках)
'''
import scrapy


class StoreSpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://quotes.toscrape.com']


def parse(self, response):
    for link in response.css("div.quote"):
        yield response.follow(link, self.parse_page)

    for next_page in response.css("div.quote"):
        yield response.follow(next_page, self.parse)


def parse_page(self, response):
    yield {"text": response.css("span.text::text").get().strip(),
           "author": response.css("span.small.author::author").get().strip()}
