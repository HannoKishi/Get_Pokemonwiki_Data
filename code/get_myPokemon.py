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

def find_names(driver):
    a=driver.find_elements_by_xpath("//div[@id='mw-content-text']//img")
    b=driver.find_elements_by_xpath("//div[@id='mw-content-text']//span")
    a.extend(b)
    return a

def find_charas(driver):
    return driver.find_elements_by_xpath("//div[@id='mw-content-text']/div/table/tbody//a[contains(@title,'（属性）')]")

####### 进入每个页面
def each_pokemon(i,driver,f,m):
    names=find_names(driver)
    if i<m:
        name_cache=names[i].get_attribute('alt')
    else:
        name_cache=names[i].get_attribute('title')
    names[i].click()
    current_html=driver.page_source #当前html
    soup=BeautifulSoup(current_html,'lxml') #用当前的 html 创建beautifulsoup4 对象
    tag_self=soup.select("a[class='mw-selflink selflink']")
    ## 判断谁是真正的selflink
    #real_tag=None
    real_tag=[]
    if len(tag_self)==0:
        pass
    else:
        for tag in tag_self:
            pattern=re.compile('^roundy.*')
            #print(tag.parent['class'][0])  ##神他妈复合class 我傻了
            if tag.parent.get('class')==None:
                pass
            elif pattern.match(tag.parent['class'][0]):
                real_tag.append(tag)
                #break
    if len(real_tag)==0:
        f.write(name_cache+'\n')
        #print(name_cache)
    else:
        for tag in real_tag:
            name=tag.string
            print(name)
            cha=search_name_cha(tag)  #返回属性字符串
            little=search_little_name(tag)
            evo=search_evo(tag)       #返回进化字符串
            all_string=name+little+' '+cha+' '+evo
        #f=open('get_myPokemon.txt','a',encoding='utf-8')
            f.write(all_string+'\n')
        #f.close()
    driver.back()                  #后退窗口


def search_name_cha(tag_self):
    cha=tag_self.find_next_siblings('span')
    s=[]
    for x in cha:
        s1=x.string.strip()
        #s1=x.a.get_text().strip()
        s.append(s1)
    outstring=""
    for y in s:
        outstring=outstring+'+'+y
    #print(s)
    print(outstring[1:])
    return outstring[1:]

def search_little_name(tag_self):
    little_name=tag_self.find_next_siblings('small')  #小名字区域特性
    #print('###')
    #print(little_name)
    s=[]
    out=''
    if len(little_name)==0:
        return out
    else:
        for x in little_name:
            print(x.string.strip())
            s.append(x.string.strip())
    for y in s:
        out=out+'+'+y
    return out[1:]

def search_evo(tag_self):
    tag_table=tag_self.find_parent('table')
    evolution=tag_table.parent.parent.select("td[class='textblack']")
    out_put_list=[]
    for x in evolution:
        ## 这里 x 存在没有a的情况
        find_a=x.find_all('a')
        if find_a:
            s=x.a.get('title')+x.get_text()
        else:
            s=x.get_text()
        s=s.replace('\n','')
        s=s.replace('→','')
        out_put_list.append(s)
    #print(out_put_list)
    output=''
    for y in out_put_list:
        output=output+'+'+y
    #print(output[1:])
    return output[1:]
        

### main code
driver2=open_web(url)
img_nums=len(driver2.find_elements_by_xpath("//div[@id='mw-content-text']//img"))
con_nums=len(driver2.find_elements_by_xpath("//div[@id='mw-content-text']//span"))
#names=find_names(driver2)
f=open('get_myPokemon.txt','a',encoding='utf-8')
for i in range(0,img_nums+con_nums):
    each_pokemon(i,driver2,f,img_nums)
#each_pokemon(42,driver2,f,img_nums)
print('### finish ###')
f.close()

