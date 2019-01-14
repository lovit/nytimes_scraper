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