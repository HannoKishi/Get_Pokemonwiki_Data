# Get_Pokemonwiki_Data
           Use Python Reptile technique to get Pokemon_wiki Data      
-----------------------------------------------------------------------
这里使用的是selenium包与beatifulsoup4       
浏览器使用的Chrome（python调用selenium要安装相应版本chromedriver）      
网站   url=https://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E4%BC%BD%E5%8B%92%E5%B0%94%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89
        
分别爬取了      
           '宝可梦名字+属性+进化方法（get_myPokemon.txt）'           
           'id+宝可梦名字+属性(name_only.txt) '                 
          
这里进化方法由于要点进每只宝可梦界面，而且进化方法表格多样化，效果一般                 
仅此做一个爬取wiki模板           
具体环境根据csdn博客文章可以配置            
