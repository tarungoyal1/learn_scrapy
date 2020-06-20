# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['http://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        page_title = response.xpath('//h1/text()').get()

        countries = response.xpath('//td/a')

        for country in countries:
            country_title = country.xpath('.//text()').get()
            country_link = country.xpath('.//@href').get()

            # yield {
            #     'title':title,
            #     'country_link':country_link
            # }


            yield response.follow(url=country_link, callback=self.parse_country, meta={'country_name':country_title})
            
            #remember this will follow only this link, it will not do recursively which is called crawling.

    def parse_country(self, response):
        name = response.request.meta['country_name']

        #let's get historical population data of each country
        table_rows = response.xpath("//h2[contains(text(), 'historical')]/following::table[position()=1]//tbody/tr")

        for row in table_rows:
            year = row.xpath('.//td[1]/text()').get()
            number = row.xpath('.//td/strong/text()').get()

            yield {
                'name':name,
                'year':year,
                'population':number
            }
    
