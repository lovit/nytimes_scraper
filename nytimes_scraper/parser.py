from .utils import get_soup

def parse_title(soup):
    return soup.select('h1[itemprop=headline]')[0].text

def parse_author(soup):
    return soup.select('p[itemprop^=author]')[0].text

def parse_date(soup):
    return soup.select('ul[class^=css-zh8slb]')[0].text

def parse_content(soup):
    return '\n'.join(p.text for p in soup.select('section[name=articleBody] p'))

def parse_page(url):
    soup = get_soup(url)
    funcs = [
        ('title', parse_title),
        ('author', parse_author),
        ('date', parse_date),
        ('content', parse_content)
    ]

    json_obj = {}
    for key, func in funcs:
        try:
            json_obj[key] = func(soup)
        except:
            continue
        json_obj['url'] = url
    return json_obj
