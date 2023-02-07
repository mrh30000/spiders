"""

selenium 去操作驱动然后控制浏览器

"""
from selenium import webdriver
import csv
import time
f = open('./python_2.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '职位',
    '地区',
    '公司',
    '薪资待遇',
    '学历经验',
    '公司领域',
    '详情页',
])
# csv_writer.writeheader(query,city)
# driver = webdriver.Edge()
driver = webdriver.Chrome(executable_path='../chromedriver.exe')


def get_info(query,city):
    driver.get(f'https://www.zhipin.com/job_detail/?query={query}&city={city}&industry=&position=')
    # //*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[2]/ul
    time.sleep(10)
    lis = driver.find_elements_by_xpath('//div[@class="search-job-result"]/ul/li')

    # lis = driver.find_elements_by_css_selector('.search-job-result .job-list-box li')
    # print(lis)
    for li in lis:
        title = li.find_element_by_xpath('./div[1]/a/div[1]/span[1]').text # 获取a标签里面文本数据
        href = li.find_element_by_xpath('./div[1]/a').get_attribute('href') # 详情页
        area = li.find_element_by_xpath('./div[1]/a/div[1]/span[2]').text  # 地区
        company_name = li.find_element_by_xpath('./div[1]/div[1]/div[2]/h3/a').text  # 公司
        money = li.find_element_by_xpath('./div[1]/a/div[2]/span').text # 薪资
        info = li.find_element_by_xpath('./div[1]/a[1]/div[2]/ul[1]/li[2]').text # 学历经验
        company_type = li.find_element_by_xpath('./div[1]/div[1]/div[2]/ul[1]/li[1]').text # 公司领域
        dit = {
            '职位': title,
            '地区': area,
            '公司': company_name,
            '薪资待遇': money,
            '学历经验': info,
            '公司领域': company_type,
            '详情页': href,
        }
        csv_writer.writerow(dit)
    #     print(title, area, company_name, money, info, company_type, href)

def main():
    for _ in range(10):
        get_info('python','101280100')
        driver.find_element_by_xpath('//div[@class="options-pages"]/a[10]').click()
    f.close()