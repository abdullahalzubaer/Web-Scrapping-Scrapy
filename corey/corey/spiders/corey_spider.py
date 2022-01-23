import scrapy

# For the first page
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


# For all the page

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
'''
