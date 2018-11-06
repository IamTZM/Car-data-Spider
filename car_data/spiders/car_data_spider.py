# -*- coding: utf-8 -*-
import scrapy
from car_data.items import CarDataItem
from car_data.pathlist import pathlist


class CarDataSpiderSpider(scrapy.Spider):
    name = 'car_data_spider'
    allowed_domains = ['car.autohome.com.cn']
    # 入口URL
    start_urls = ['https://car.autohome.com.cn/price/brand-117.html', 'https://car.autohome.com.cn/price/brand-276.html', 'https://car.autohome.com.cn/price/brand-34.html', 'https://car.autohome.com.cn/price/brand-35.html', 'https://car.autohome.com.cn/price/brand-33.html', 'https://car.autohome.com.cn/price/brand-140.html', 'https://car.autohome.com.cn/price/brand-120.html', 'https://car.autohome.com.cn/price/brand-15.html', 'https://car.autohome.com.cn/price/brand-231.html', 'https://car.autohome.com.cn/price/brand-40.html', 'https://car.autohome.com.cn/price/brand-27.html', 'https://car.autohome.com.cn/price/brand-333.html', 'https://car.autohome.com.cn/price/brand-79.html', 'https://car.autohome.com.cn/price/brand-301.html', 'https://car.autohome.com.cn/price/brand-203.html', 'https://car.autohome.com.cn/price/brand-173.html', 'https://car.autohome.com.cn/price/brand-143.html', 'https://car.autohome.com.cn/price/brand-208.html', 'https://car.autohome.com.cn/price/brand-154.html', 'https://car.autohome.com.cn/price/brand-36.html', 'https://car.autohome.com.cn/price/brand-95.html', 'https://car.autohome.com.cn/price/brand-14.html', 'https://car.autohome.com.cn/price/brand-271.html', 'https://car.autohome.com.cn/price/brand-75.html', 'https://car.autohome.com.cn/price/brand-13.html', 'https://car.autohome.com.cn/price/brand-38.html', 'https://car.autohome.com.cn/price/brand-39.html', 'https://car.autohome.com.cn/price/brand-37.html', 'https://car.autohome.com.cn/price/brand-76.html', 'https://car.autohome.com.cn/price/brand-299.html', 'https://car.autohome.com.cn/price/brand-163.html', 'https://car.autohome.com.cn/price/brand-294.html', 'https://car.autohome.com.cn/price/brand-77.html', 'https://car.autohome.com.cn/price/brand-196.html', 'https://car.autohome.com.cn/price/brand-169.html', 'https://car.autohome.com.cn/price/brand-341.html', 'https://car.autohome.com.cn/price/brand-92.html', 'https://car.autohome.com.cn/price/brand-1.html', 'https://car.autohome.com.cn/price/brand-41.html', 'https://car.autohome.com.cn/price/brand-280.html', 'https://car.autohome.com.cn/price/brand-32.html', 'https://car.autohome.com.cn/price/brand-326.html', 'https://car.autohome.com.cn/price/brand-187.html', 'https://car.autohome.com.cn/price/brand-259.html', 'https://car.autohome.com.cn/price/brand-113.html', 'https://car.autohome.com.cn/price/brand-165.html', 'https://car.autohome.com.cn/price/brand-142.html', 'https://car.autohome.com.cn/price/brand-81.html', 'https://car.autohome.com.cn/price/brand-42.html', 'https://car.autohome.com.cn/price/brand-11.html', 'https://car.autohome.com.cn/price/brand-3.html', 'https://car.autohome.com.cn/price/brand-141.html', 'https://car.autohome.com.cn/price/brand-197.html', 'https://car.autohome.com.cn/price/brand-8.html', 'https://car.autohome.com.cn/price/brand-96.html', 'https://car.autohome.com.cn/price/brand-282.html', 'https://car.autohome.com.cn/price/brand-112.html', 'https://car.autohome.com.cn/price/brand-152.html', 'https://car.autohome.com.cn/price/brand-116.html', 'https://car.autohome.com.cn/price/brand-82.html', 'https://car.autohome.com.cn/price/brand-108.html', 'https://car.autohome.com.cn/price/brand-329.html', 'https://car.autohome.com.cn/price/brand-313.html', 'https://car.autohome.com.cn/price/brand-304.html', 'https://car.autohome.com.cn/price/brand-24.html', 'https://car.autohome.com.cn/price/brand-181.html', 'https://car.autohome.com.cn/price/brand-150.html', 'https://car.autohome.com.cn/price/brand-86.html', 'https://car.autohome.com.cn/price/brand-267.html', 'https://car.autohome.com.cn/price/brand-43.html', 'https://car.autohome.com.cn/price/brand-164.html', 'https://car.autohome.com.cn/price/brand-91.html', 'https://car.autohome.com.cn/price/brand-336.html', 'https://car.autohome.com.cn/price/brand-245.html', 'https://car.autohome.com.cn/price/brand-85.html', 'https://car.autohome.com.cn/price/brand-184.html', 'https://car.autohome.com.cn/price/brand-220.html', 'https://car.autohome.com.cn/price/brand-87.html', 'https://car.autohome.com.cn/price/brand-260.html', 'https://car.autohome.com.cn/price/brand-97.html', 'https://car.autohome.com.cn/price/brand-188.html', 'https://car.autohome.com.cn/price/brand-46.html', 'https://car.autohome.com.cn/price/brand-25.html', 'https://car.autohome.com.cn/price/brand-84.html', 'https://car.autohome.com.cn/price/brand-119.html', 'https://car.autohome.com.cn/price/brand-210.html', 'https://car.autohome.com.cn/price/brand-270.html', 'https://car.autohome.com.cn/price/brand-44.html', 'https://car.autohome.com.cn/price/brand-319.html', 'https://car.autohome.com.cn/price/brand-83.html', 'https://car.autohome.com.cn/price/brand-145.html', 'https://car.autohome.com.cn/price/brand-175.html', 'https://car.autohome.com.cn/price/brand-151.html', 'https://car.autohome.com.cn/price/brand-297.html', 'https://car.autohome.com.cn/price/brand-109.html', 'https://car.autohome.com.cn/price/brand-156.html', 'https://car.autohome.com.cn/price/brand-224.html', 'https://car.autohome.com.cn/price/brand-199.html', 'https://car.autohome.com.cn/price/brand-101.html', 'https://car.autohome.com.cn/price/brand-47.html', 'https://car.autohome.com.cn/price/brand-214.html', 'https://car.autohome.com.cn/price/brand-100.html', 'https://car.autohome.com.cn/price/brand-9.html',
                  'https://car.autohome.com.cn/price/brand-335.html', 'https://car.autohome.com.cn/price/brand-241.html', 'https://car.autohome.com.cn/price/brand-118.html', 'https://car.autohome.com.cn/price/brand-48.html', 'https://car.autohome.com.cn/price/brand-54.html', 'https://car.autohome.com.cn/price/brand-52.html', 'https://car.autohome.com.cn/price/brand-10.html', 'https://car.autohome.com.cn/price/brand-124.html', 'https://car.autohome.com.cn/price/brand-345.html', 'https://car.autohome.com.cn/price/brand-80.html', 'https://car.autohome.com.cn/price/brand-89.html', 'https://car.autohome.com.cn/price/brand-78.html', 'https://car.autohome.com.cn/price/brand-51.html', 'https://car.autohome.com.cn/price/brand-53.html', 'https://car.autohome.com.cn/price/brand-318.html', 'https://car.autohome.com.cn/price/brand-279.html', 'https://car.autohome.com.cn/price/brand-343.html', 'https://car.autohome.com.cn/price/brand-204.html', 'https://car.autohome.com.cn/price/brand-88.html', 'https://car.autohome.com.cn/price/brand-49.html', 'https://car.autohome.com.cn/price/brand-50.html', 'https://car.autohome.com.cn/price/brand-346.html', 'https://car.autohome.com.cn/price/brand-56.html', 'https://car.autohome.com.cn/price/brand-58.html', 'https://car.autohome.com.cn/price/brand-57.html', 'https://car.autohome.com.cn/price/brand-55.html', 'https://car.autohome.com.cn/price/brand-129.html', 'https://car.autohome.com.cn/price/brand-20.html', 'https://car.autohome.com.cn/price/brand-168.html', 'https://car.autohome.com.cn/price/brand-295.html', 'https://car.autohome.com.cn/price/brand-334.html', 'https://car.autohome.com.cn/price/brand-130.html', 'https://car.autohome.com.cn/price/brand-213.html', 'https://car.autohome.com.cn/price/brand-60.html', 'https://car.autohome.com.cn/price/brand-59.html', 'https://car.autohome.com.cn/price/brand-331.html', 'https://car.autohome.com.cn/price/brand-146.html', 'https://car.autohome.com.cn/price/brand-332.html', 'https://car.autohome.com.cn/price/brand-308.html', 'https://car.autohome.com.cn/price/brand-61.html', 'https://car.autohome.com.cn/price/brand-26.html', 'https://car.autohome.com.cn/price/brand-122.html', 'https://car.autohome.com.cn/price/brand-62.html', 'https://car.autohome.com.cn/price/brand-235.html', 'https://car.autohome.com.cn/price/brand-222.html', 'https://car.autohome.com.cn/price/brand-312.html', 'https://car.autohome.com.cn/price/brand-219.html', 'https://car.autohome.com.cn/price/brand-63.html', 'https://car.autohome.com.cn/price/brand-19.html', 'https://car.autohome.com.cn/price/brand-337.html', 'https://car.autohome.com.cn/price/brand-174.html', 'https://car.autohome.com.cn/price/brand-296.html', 'https://car.autohome.com.cn/price/brand-103.html', 'https://car.autohome.com.cn/price/brand-45.html', 'https://car.autohome.com.cn/price/brand-269.html', 'https://car.autohome.com.cn/price/brand-64.html', 'https://car.autohome.com.cn/price/brand-205.html', 'https://car.autohome.com.cn/price/brand-68.html', 'https://car.autohome.com.cn/price/brand-149.html', 'https://car.autohome.com.cn/price/brand-155.html', 'https://car.autohome.com.cn/price/brand-66.html', 'https://car.autohome.com.cn/price/brand-90.html', 'https://car.autohome.com.cn/price/brand-69.html', 'https://car.autohome.com.cn/price/brand-162.html', 'https://car.autohome.com.cn/price/brand-65.html', 'https://car.autohome.com.cn/price/brand-238.html', 'https://car.autohome.com.cn/price/brand-67.html', 'https://car.autohome.com.cn/price/brand-202.html', 'https://car.autohome.com.cn/price/brand-133.html', 'https://car.autohome.com.cn/price/brand-161.html', 'https://car.autohome.com.cn/price/brand-283.html', 'https://car.autohome.com.cn/price/brand-102.html', 'https://car.autohome.com.cn/price/brand-291.html', 'https://car.autohome.com.cn/price/brand-99.html', 'https://car.autohome.com.cn/price/brand-192.html', 'https://car.autohome.com.cn/price/brand-284.html', 'https://car.autohome.com.cn/price/brand-70.html', 'https://car.autohome.com.cn/price/brand-114.html', 'https://car.autohome.com.cn/price/brand-167.html', 'https://car.autohome.com.cn/price/brand-98.html', 'https://car.autohome.com.cn/price/brand-12.html', 'https://car.autohome.com.cn/price/brand-275.html', 'https://car.autohome.com.cn/price/brand-185.html', 'https://car.autohome.com.cn/price/brand-324.html', 'https://car.autohome.com.cn/price/brand-306.html', 'https://car.autohome.com.cn/price/brand-71.html', 'https://car.autohome.com.cn/price/brand-72.html', 'https://car.autohome.com.cn/price/brand-111.html', 'https://car.autohome.com.cn/price/brand-110.html', 'https://car.autohome.com.cn/price/brand-144.html', 'https://car.autohome.com.cn/price/brand-73.html', 'https://car.autohome.com.cn/price/brand-93.html', 'https://car.autohome.com.cn/price/brand-298.html', 'https://car.autohome.com.cn/price/brand-263.html', 'https://car.autohome.com.cn/price/brand-232.html', 'https://car.autohome.com.cn/price/brand-307.html', 'https://car.autohome.com.cn/price/brand-286.html', 'https://car.autohome.com.cn/price/brand-317.html', 'https://car.autohome.com.cn/price/brand-182.html', 'https://car.autohome.com.cn/price/brand-206.html', 'https://car.autohome.com.cn/price/brand-22.html', 'https://car.autohome.com.cn/price/brand-74.html', 'https://car.autohome.com.cn/price/brand-94.html']

    def parse(self, response):
        # 获取主要信息列表
        car_list = response.xpath("//div[@id='brandtab-1']/div")
        # print(len(car_list))
        # 当前品牌
        current_car_brand = ''
        # 当前车系
        current_car_name = ''
        # 当前车型
        current_car_type = ''
        # 当前结构
        current_car_struct = ''
        # 当前评分
        current_car_score = ''
        # 当前动力
        current_car_power = ''

        for i_item in car_list:
            # 导入items文件
            data_item = CarDataItem()

            # 如果当前元素对应的是品牌信息
            if i_item.xpath("./@class").extract_first() == 'brand-title':
                # 设置当前品牌
                current_car_brand = i_item.xpath(
                    "./a/h3/text()").extract_first()
                # 进入下一循环
                continue

            # 如果当前元素对应的是当前品牌中各车系的详细信息
            if i_item.xpath("./@class").extract_first() == 'list-cont':
                # 设置当前车系
                current_car_name = i_item.xpath(
                    ".//div[@class='list-cont-main']/div[@class='main-title']/a/text()").extract_first()
                # 设置当前车型
                current_car_type = i_item.xpath(
                    ".//div[@class='list-cont-main']/div[@class='main-lever']//ul/li[1]/span[@class='info-gray']/text()").extract_first()
                # 设置当前结构，因为结构可能有多种，所以需要特殊处理
                current_car_struct = i_item.xpath(
                    ".//div[@class='list-cont-main']/div[@class='main-lever']//ul/li[2]/a/text()").extract()
                # current_car_struct = all_car_struct[0]
                # struct_count = len(all_car_struct)
                # if struct_count > 1:
                #     for i in range(struct_count - 1):
                #         current_car_struct = current_car_struct + '/' + all_car_struct[i + 1]
                # 设置当前评分
                current_car_score = i_item.xpath(
                    ".//div[@class='score-cont']//span/text()").extract_first()
                # 进入下一循环
                continue

            # 如果当前元素对应的是展开内容
            if i_item.xpath("./@class").extract_first() == 'intervalcont fn-hide':
                all_powers = i_item.xpath("./div[@class='interval01']")
                # print(len(all_powers))
                for i_power in all_powers:
                    current_car_power = i_power.xpath(
                        "./div/div/span/text()").extract_first()
                    all_yearstyle = i_power.xpath("./ul/li")
                    for i_yearstyle in all_yearstyle:
                        data_item['car_yearstyle'] = i_yearstyle.xpath(
                            ".//p/a/text()").extract_first()
                        data_item['car_guide_price'] = i_yearstyle.xpath(
                            "./div[@class='interval01-list-guidance']/div/text()").extract_first()
                        data_item['car_brand'] = current_car_brand
                        data_item['car_name'] = current_car_name
                        data_item['car_type'] = current_car_type
                        data_item['car_struct'] = current_car_struct
                        if len(data_item['car_struct']) == 0:
                            data_item['car_struct'].append('新能源')
                        data_item['car_score'] = current_car_score
                        data_item['car_power'] = current_car_power
                        yield data_item

        # 解析下一页
        next_link = response.xpath(
            "//div[@class='page']/a[@class='page-item-next']/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://car.autohome.com.cn" + next_link, callback=self.parse)
