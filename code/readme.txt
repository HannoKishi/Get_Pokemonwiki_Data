url=https://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E4%BC%BD%E5%8B%92%E5%B0%94%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89
                                                宝可梦列表（按伽勒尔图鉴编号）
                                              宝可梦wiki官网  wiki.52poke.com
                                              
  目前宝可梦剑盾刚刚发行，这里利用python爬虫爬取了 伽勒尔图鉴

python爬虫环境需要 selenium包，Beautifulsoup包和相应浏览器的driver
这里我使用的是谷歌浏览器 下载了相应的chromedriver
网页解释器选用的是 lxml
1.get_myPokemon 用来爬取每个宝可梦的进化方法，这里需要进入每只的单独界面（由于有地区特性，进化的多种样，总体数目是超过400个）
2.get_Pokeman_onlynameAcha 用来爬取主界面的id+name+属性，这个比较简单，当前界面就可以完成
