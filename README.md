# New York Times scraper

## Usage

To parse a page

```python
from nytimes_scraper import parse_page

url = 'https://www.nytimes.com/2018/12/19/world/asia/north-korea-travel-ban-us.html'
parse_page(url)
```

It returns json format scraped news

```
{'author': 'By Choe Sang-Hun',
 'content': 'SEOUL, South Korea — The United States plans to review its ban ...,
 'date': 'Dec. 19, 2018',
 'title': 'U.S. Will Review Travel Ban on North Korea, Envoy Says'
}
```

Scrap from search result front page

```python
from nytimes_scraper import get_urls_from_search_front
from nytimes_scraper import save

directory = './output/korea/'
query = 'korea'
date = '20190103'
urls = get_urls_from_search_front(query, date)

for url in urls:
    json_obj = parse_page(url)
    save(json_obj, date, directory)
```