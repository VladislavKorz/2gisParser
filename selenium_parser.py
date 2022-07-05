from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

s = Service(executable_path='C:/Users/Professional/Desktop/Py Jobs/parser/chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get('https://2gis.ru/tomsk/search/Аптеки/firm/70000001007252625/84.967864%2C56.460078')

html = driver.page_source

soup = BeautifulSoup(html)

# element = driver.find_element_by_class_name("_1h3cgic")

# element.click()


# for tag in soup.find_all('div',class_='_14uxmys'): 
#     url_more = tag.select_one('a').get('href')
#     print()
#     print()
#     print(url_more)

for tag in soup.find_all('h1', class_='_d9xbeh'): # Название компании ГОТОВО
    # print()
    name_company = tag.text
    # print(data_1)
    # print()

for tag in soup.find_all('div', class_='_18zamfw'): #ЧАСЫ РАБОТЫ ГОТОВО
        # print()
    hours_job = tag.text
        # print(data_2)
        # print()

for tag in soup.find_all('div',class_='_49kxlr'): # САЙТ ГОТОВО
    site = tag.text
    # print(data_3)

for tag in soup.find_all('div',class_='_b0ke8'): # ТЕЛЕФОН ГОТОВО
    number = tag.select_one('a').get('href')
    number = number.replace('tel:','')

for tag in soup.find_all('div',class_='_6amp0g3'): # ВК ГОТОВО
    vk = tag.select_one('a').get('href')

for tag in soup.find_all('div',class_='_14uxmys'): # ТГ ГОТОВО
    tg = tag.select_one('a').get('href')

dict_parser = {
        'Название компании' : name_company,
        'ЧАСЫ РАБОТЫ' : hours_job,
        'САЙТ' : site,
        'номер' : number,
        'Вконтакте' : vk,
        'ТГ' : tg,
    }
print(dict_parser)


# for tag in soup.find_all('div',class_='_14uxmys'):
#     data = tag.select_one('a').get('href')
# print(data)


    