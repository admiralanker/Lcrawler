'''
光IDE安装scrapy不行，还需要在项目所在目录安装
安装：pip install scrapy
'''

import scrapy

html = scrapy.Request('http://stockpage.10jqka.com.cn/600004/company/#detail')
print(html)

'''
创建scrapy工程
scrapy startproject spider_name
'''

