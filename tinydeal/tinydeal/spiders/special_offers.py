# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.tinydeal.com']

    
    start_urls = ['https://www.tinydeal.com/specials.html']

    def parse(self, response):

        ratings_meaning = {
            's_star_5':'5',
            's_star_4':'4',
            's_star_3':'3',
            's_star_2':'2',
            's_star_1':'1',
            's_star_0':'0'
        }

        for product in response.xpath("//ul[@class='productlisting-ul']//li"):
            try :
                yield {
                    'title': product.xpath(".//a[@class='p_box_title']/text()").get(),
                    'url': response.urljoin(product.xpath(".//a[@class='p_box_title']/@href").get()),
                    'discounted_price': product.xpath(".//div[@class='p_box_price']/span[1]/text()").get(),
                    'original_price':product.xpath(".//div[@class='p_box_price']/span[2]/text()").get().rstrip(),
                    'rating_count':product.xpath(".//div[@class='p_box_star']/a/text()").get()[1:-1],
                    'rating_star':ratings_meaning.get(product.xpath(".//div[@class='p_box_star']/span/@class").get().partition(' ')[2])
                }
            except AttributeError:
                pass
        
        next_page = response.xpath("//a[@class='nextPage']/@href").get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)
