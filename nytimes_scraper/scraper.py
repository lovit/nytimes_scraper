from .utils import get_soup

def get_urls_from_search_front(query, date):
    base = 'https://www.nytimes.com/search?query={0}&sort=newest&startDate={1}&endDate={1}'
    search_url = base.format(query, date)
    soup = get_soup(search_url)
    urls = []
    for li in soup.select('li[data-testid=search-bodega-result] a'):
        url = 'https://www.nytimes.com{}'.format(li.attrs['href'])
        urls.append(url)
    return urls