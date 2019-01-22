import argparse
import datetime
from dateutil import parser as date_parser
import os
import time
from nytimes_scraper import get_urls_from_search_front
from nytimes_scraper import parse_page
from nytimes_scraper import save


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', type=str, default='korea', help='Single term')
    parser.add_argument('--begin_date', type=str, default='2018/01/01', help='datetime YYYY/mm/dd')
    parser.add_argument('--end_date', type=str, default='2019/01/10', help='datetime YYYY/mm/dd')
    parser.add_argument('--directory', type=str, default='./output/', help='Output directory')
    parser.add_argument('--sleep', type=float, default=10, help='Sleep time for each submission (post)')
    parser.add_argument('--debug', dest='DEBUG', action='store_true')

    args = parser.parse_args()
    query = args.query
    begin_date = args.begin_date
    end_date = args.end_date
    directory = args.directory
    sleep = args.sleep
    DEBUG = args.DEBUG

    directory = directory + '/' + query

    # check output directory
    if not os.path.exists(directory):
        os.makedirs(directory)

    bdt = date_parser.parse(begin_date)
    edt = date_parser.parse(end_date)
    dt = date_parser.parse(begin_date)

    while dt <= edt:
        date = dt.strftime("%Y%m%d")
        urls = get_urls_from_search_front(query, date)

        if not urls:
            print('Not found article on {}'.format(date))
            time.sleep(sleep)
            continue

        if DEBUG:
            urls = urls[:3]

        n = len(urls)
        for i, url in enumerate(urls):
            json_obj = parse_page(url)
            save(json_obj, date, directory)
            time.sleep(sleep)
            print('\rscraping {} / {} articles on {}'.format(i+1, n, date), end='')
        print('\rscraping {} / {} articles on {}'.format(i+1, n, date))

        dt += datetime.timedelta(days=1)
    print('done')

if __name__ == '__main__':
    main()