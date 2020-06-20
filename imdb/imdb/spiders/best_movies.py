# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['www.imdb.com']
    start_urls = ['https://www.imdb.com/search/title/?groups=top_250']

    # you can add as many rules as you want but order that they are written in matters.
    # the second rule we have added here is for pagination
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']//a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//a[@class='lister-page-next next-page'][1]"))
    )


    # since we are restricting to only one xpath expression for our LinExtractor we passed a single string as value of 
    # 'restrict_xpaths' arguement else we'd have passed an tuple for multiple expression if we had more than one expression
    # for example:

    # rules = (
    #     Rule(LinkExtractor(restrict_xpaths=(xpath1, xpath2, xpath3, ..)), callback='parse_item', follow=True),
    # )


    def parse_item(self, response):
        # note: response will be of each url link that was followed not the from start_url, so write down selectors below for that page.
        item = {} 

        item['title'] = response.xpath("//div[@class='title_wrapper']/h1/text()").get()
        item['year']  = response.xpath("//span[@id='titleYear']/a/text()").get()
        item['duration']  = response.xpath("normalize-space(//time[1]/text())").get()
        item['genre']  = response.xpath("//div[@class='subtext']/a[1]/text()").get()
        item['rating']  = response.xpath("//span[@itemprop='ratingValue']/text()").get()
        item['rating_count']  = response.xpath("//span[@itemprop='ratingCount']/text()").get()
        yield item
