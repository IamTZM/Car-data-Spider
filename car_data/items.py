# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CarDataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 品牌
    car_brand = scrapy.Field()
    # 车系
    car_name = scrapy.Field()
    # 车型
    car_type = scrapy.Field()
    # 车身结构(几厢)
    car_struct = scrapy.Field()
    # 评分
    car_score = scrapy.Field()
    # 动力
    car_power = scrapy.Field()
    # 年款
    car_yearstyle = scrapy.Field()
    # 指导价
    car_guide_price = scrapy.Field()
    