# -*- coding: utf-8 -*-
import scrapy


class NewDelhiRentSpider(scrapy.Spider):
    name = 'new_delhi_rent'
    allowed_domains = ['www.99acres.com']
    start_urls = ['https://www.99acres.com/search/property/rent/residential-all/new-delhi?search_type=QS&refSection=GNB&search_location=NRI&lstAcn=NR_R&lstAcnId=-1&src=CLUSTER&preference=R&selected_tab=4&city=1&res_com=R&property_type=R&isvoicesearch=N&keyword=new%20delhi&strEntityMap=IiI%3D&refine_results=Y&Refine_Localities=Refine%20Localities&action=%2Fdo%2Fquicksearch%2Fsearch&searchform=1&price_min=null&price_max=null']

    def parse(self, response):
        response.xpath('')
