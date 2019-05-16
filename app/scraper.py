from requests import Session
import lxml.html
import time
import random
from lxml.html import fromstring
import requests
import traceback

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

def get_request_with_proxy(url):
    proxies = get_proxies()
    for proxy in proxies:
        try:
            return requests.get(url, proxies={"http": proxy, "https": proxy})
        except:
            pass
        
def get_keywords():
    r = get_request_with_proxy("https://www.crisistextline.org/referrals")
    html = lxml.html.fromstring(r.text)
    return html.xpath("//tr/th")

def get_link(html_obj):
    links = []
    for elem in html_obj.iterlinks():
        links.append(elem[2])
    return links

def get_bad_links(html):
    results = html.xpath("//tr[@style='display: none:']/td/a")
    links = []
    for result in results:
        links += get_link(result)
    links = list(set(links))
    return links

def get_good_links(html, bad_links):
    results = html.xpath("//tr/td/a")
    links = []
    for result in results:
        tmp_links = get_link(result)
        for link in tmp_links:
            if link not in bad_links:
                links += link
    links = list(set(links))
    return links

def get_links_with_proxy(keyword):
    proxies = get_proxies()
    for proxy in proxies:
        try:
            return get_links(keyword, proxy)
        except:
            pass

def get_links(keyword, proxy):
    with Session() as session:
        post = session.post(
            "https://www.crisistextline.org/referrals",
            data={"myInput": keyword},
            proxies={"http": proxy, "https": proxy}
        )
        r = session.get(
            "https://www.crisistextline.org/referrals",
            proxies={"http": proxy, "https": proxy}
        )
        html = lxml.html.fromstring(r.text)
        bad_links = get_bad_links(html)
    return get_good_links(html, bad_links)
        
def scrape_crisis_text_line():
    keywords = get_keywords()
    data = []
    source = "https://www.crisistextline.org/referrals"
    for keyword in keywords:
        time.sleep(random.randint(300, 875))
        links = get_links_with_proxy(keyword)
        for link in links:
            data.append((keyword, link, source))
    return data
    
