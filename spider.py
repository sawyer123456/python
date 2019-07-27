# -*- coding:UTF-8 -*-
'''
单进程
下载妹子图片
'''
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os
from selenium import webdriver

if __name__ =='__main__':
    list_urls=[]
    url="http://www.5442.com/tag/rosi.html"

    options = webdriver.ChromeOptions()
    options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver=webdriver.Chrome(chrome_options=options)
    driver.get(url)
    html=driver.page_source
    driver.close()
   # print(html)
    bf=BeautifulSoup(html,'lxml')
    target_urls=bf.find_all(name="div",class_='libox')
    for each in target_urls:
        print(each.a.get('href'))
        list_urls.append(each.a.get('href'))

    print(len(list_urls))

    for each_img in list_urls:

        target_url =each_img
        options = webdriver.ChromeOptions()
        options.add_argument(
            'user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19",')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        pdriver = webdriver.Chrome(chrome_options=options)
        pdriver.get(target_url)
        img_html = pdriver.page_source
        pdriver.close()
        pbf=BeautifulSoup(img_html,'lxml')
        piurls=pbf.find_all(name='p',align='center')
        ppbf=BeautifulSoup(str(piurls),'lxml')
        purls=ppbf.find_all(name='img')
        if 'images' not in os.listdir():
            os.makedirs('images')
        for each in purls:
            img_url=each.get('src')
            img_filename='D:电影/images/'+each.get('alt')+'.jpg'
            print("正在下载",img_url)
            urlretrieve(url=img_url,filename=img_filename)
