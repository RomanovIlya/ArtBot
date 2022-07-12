from icrawler.builtin import GoogleImageCrawler
import os

def google_img(search_name=''):
    crawler=GoogleImageCrawler(storage={'root_dir':'./img'})
    crawler.crawl(keyword=search_name,max_num=3)
