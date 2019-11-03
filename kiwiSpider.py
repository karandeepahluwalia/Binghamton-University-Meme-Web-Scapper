#!/usr/bin/env python
# coding: utf-8
#Property of Karandeep Ahluwalia
# In[3]:


import scrapy


# In[4]:


from scrapy.crawler import CrawlerProcess


# In[5]:


class kiwiCrawler(scrapy.Spider):
    name="kiwiSpider"
    start_urls=['https://kiwifarms.net']
    count=0
    def parse(self,response):
        with open('homepage.html', 'wb') as html_file:
            html_file.write(response.body)
        for link in response.xpath('//a/@href').extract():
            yield response.follow(url=link,callback=self.parse_follow)
    def parse_follow(self,response):
        self.count+=1
        if self.count<300:
            with open('page'+str(self.count)+'.html','wb') as file:
                file.write(response.body)
                for link in response.xpath('//a/@href').extract():
                    yield response.follow(url=link,callback=self.parse_follow)





# In[ ]:
