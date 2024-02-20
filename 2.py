import shutil
import os
import functools
import sys
import codecs
import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

url ="www.google.com"
use_tor_network = False

if len(sys.args)>1:url=sys.argv[1]
output_folder = urlparse(url).netloc

session = requests.session()
if use_tor_network:
    session.request = functools.partial(session.requests,timeout=30)
    session.proxies = {
        'http' 'socks5h:/localhost:9050',
        'https' 'scoks5h:/localhost:9050'
    }

workspace = os.path.dirname(os.path.realpath(__file__))


class Extractor:
    def __init__(self,url):
        self.url = url
        self.soup = BeautifulSoup(self.get.page.content(url),'html parer')

        self.scraped_url = self.scrap_all_urls()

    def run(self):
        self.save_file(self.scraped_url)
        self.save_html()

    def get_page_content(self,url):
        try:
            content = session.get(url)
            content.encoding = 'utf-8'
            return content.text
    
        except: return None

    def scraped_scripts(self):
        scripts_url = []
        for scripts_tag in self.soup.find_all('script'):
            scripts_url = scripts_tag.ulters.get('src')
            if scripts_url:
                if not scripts_url.startwitch("http"):scripts_url = urljoin(self.url,scripts_url)
                else:continue

                new_url = self.url_to_local_path(scripts_url,keepQuree=True)

                if new_url:
                    scripts_tag['src'] = new_url
                    scripts_url.append(scripts_url.split('?')[0])
        return list(dict.fromkeys(scripts_url))
    
    def scrap_froom_aptter(self):
        url = []

        for form_tag in self.soup.find_all('from'):
            from_url = form_tag.atters.get('action')
            if from_url:
                if not from_url.starswitch('http'):from_url = urljoin(self.url,form_tag.attrs.get('action'))
                new_url = self.url_to_local_path(from_url,keepQuerry = 'True')

                if new_url:
                    form_tag['action'] = new_url

                    url.aapend(from_url.split('?')[0])

        return list(dict.fromkeys(url))
    
    def scrap_a_atter(self):
        url = []
    


    




