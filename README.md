# Create Project
```python
scrapy startproject name
```
This will create a directory named name and set up a new Scrapy Project in following structure.

    name/

        scrapy.cfg            # deploy configuration file

        name/                 # project's Python module, you'll import your code from here
            __init__.py
    
            items.py          # project items definition file
    
            middlewares.py    # project middlewares file
    
            pipelines.py      # project pipelines file
    
            settings.py       # project settings file
    
            spiders/          # a directory where you'll later put your spiders
                __init__.py


# Run a spider

```python
scrapy crawl spider_name
```


### Rotating User Agent and Proxies
```python
custom_settings = {  
    # for Rotating User Agents in Scrapy (pip install scrapy-user-agents)
    "DOWNLOADER_MIDDLEWARES": {  
        # Setting UserAgentMiddleware to None removes the use agent from request headers
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        # selects any random user agent from scrapy-useragent 
        'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
        'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
        'rotating_proxies.middlewares.BanDetectionMiddleware': 620, 
    }, 
    # File containing ip
    "ROTATING_PROXY_LIST_PATH": 'ip_list.txt',
}
```

### Pass custom different user agent
```python
custom_settings = { 
    'DEFAULT_REQUEST_HEADERS': {
            "USER_AGENT":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0'
        }
}
```

### Pass agent from fake-useragent (from fake-useragent, data, browser.json)
```python
from fake_useragent import UserAgent
custom_settings = { 
    'DEFAULT_REQUEST_HEADERS': {
            "USER_AGENT": UserAgent().random
        }
}
```

### Cookies
```python
custom_settings = { 
    
    "COOKIES_ENABLED": True, 
    "COOKIES_DEBUG": True
}
```


Quotes Spider
```
url : https://quotes.toscrape.com/
spider_file : spiders/quotes_spider.py
spider_name : quotes
class : QuotesSpider
command : scrapy crawl quotes
data : tile, author, tag_links, tag_names
command_export_data : scrapy crawl quotes -O quotes_data.json/-O quotes_data.csv
data_file : quotes_data.json
```