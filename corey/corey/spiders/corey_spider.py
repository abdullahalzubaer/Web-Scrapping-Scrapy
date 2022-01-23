import itertools

import scrapy

# For the first page (did by myself)
'''
class CoreySpdier(scrapy.Spider):
    name = "corey"
    start_urls = ["https://coreyms.com/"]

    def parse(self, response):
        for k in response.css("header.entry-header"):
            yield {'Title': k.css('a::text').get(),
                   'Time': k.css('time::text').get(),
                   'Author': k.css('span::text').get()
                   }

'''


# For all the page (did by myself)
# '''
class CoreySpdier(scrapy.Spider):
    name = "corey"
    start_urls = ["https://coreyms.com/"]

    def parse(self, response):
        for k in response.css("header.entry-header"):
            yield {'Title': k.css('a::text').get(),
                   'Time': k.css('time::text').get(),
                   'Author': k.css('span::text').get()
                   }

        next_page = response.css('li.pagination-next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            # < li

            # class ="pagination-next" > < a href="https://coreyms.com/page/2" > Next Page » < / a > < / li >


# '''

'''
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            
'''

'''
For corey MS homepage

0. To get the title
Here I have hierarchy
main_post = response.css("header.entry-header")[0]

main_post.css('a::text').get()
>>>Will provide the title

main_post.css('time::text').get()
>>> Will provide the time

main_post.css('span::text').get()
>>> Will provide the author

1. To ge the title (stupid way)
Here i am accessing individual thing separately (no hierarchy)

post_title = response.css("a.entry-title-link")[0]
post_title.css('a::text').get()
>>> Will provide the title

post_date = response.css("time.entry-time")[0]
post_date.css('time::text').get()
>>> Will provide date of creation

post_author = response.css("a.entry-author-link")[0]
post_author.css('span::text').get()
>>> will provide the author
'''
