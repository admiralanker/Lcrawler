'''
什么是BeautifulSoup?
是一个可以从html或者是xml文字中提取数据的一个Python库

pip install beautifulsoup4  # 目前4是最新版，之前的版本已结不维护了


'''

from bs4 import BeautifulSoup

html_doc = "600004.html"
html_file = open(html_doc,"r",encoding='utf-8')
html_handle = html_file.read()
soup = BeautifulSoup(html_handle,'html.parser')
# print(soup)

# 获取html文档头
# print(soup.head)

#获取p标签
# print(soup.p)

#获取节点中的属性
# print(soup.p.attrs)

# ps = soup.find_all('p')
# print(ps)

# id = 'quotedata'

# result = soup.find_all(id = 'quotedata')
# print(result)

# 按CSS来搜索
jobs = soup.find_all('strong',class_='hltip fl')
print(jobs)
