from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys #需要引入 keys 包
import time
import re ##正则匹配

from bs4 import BeautifulSoup
import lxml
import requests
url="https://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E4%BC%BD%E5%8B%92%E5%B0%94%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89"

def open_web(url):
    opt=Options()  ##创建参数对象
    #opt.add_argument('--headless')  #无界面化
    #opt.add_argument('--disable-gpu')  #取消gpu
    driver=webdriver.Chrome(options=opt)
    driver.get(url)
    return driver

def find_names(soup):
    #img=soup.select("a[class='mw-selflink selflink']")
    tbody=soup.select("tbody")
    tr=tbody[1].select('tr')
    ## 401各对象 第一个不需要
    del tr[0]
    return tr

def each_pokemon(i,all_names,f):
    #id=all_names[i].td.string
    all_string=all_names[i].stripped_strings
    out_string=''
    for s in all_string:
        out_string=out_string+'+'+s
    out_string=out_string[1:]
    print(out_string)
    f.write(out_string+'\n')
    #names=find_names(soup)
    
      
### maincode
driver2=open_web(url)
current_html=driver2.page_source #当前html
soup=BeautifulSoup(current_html,'lxml') #用当前的 html 创建beautifulsoup4 对象
all_names=find_names(soup)
#print(len(find_names(soup)))
#print(all_names)
print(len(all_names))
f=open('name_only.txt','a',encoding='utf-8')
for i in range(0,len(all_names)):
    each_pokemon(i,all_names,f)
#each_pokemon(1,all_names,f)
print('### finish ###')
driver2.close()
f.close()