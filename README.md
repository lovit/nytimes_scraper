# New York Times scraper

Not available to retrieve all search results, only articles in front search result page.

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

With script file

```
python searching_a_query.py --query korea --begin_date 2018/01/01 --end_date 2019/01/10 --directory ./output --sleep 10 --debug
```