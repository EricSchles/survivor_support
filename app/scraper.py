import lxml.html
import time
import code
import random
import requests

def get_link(html_obj):
    links = [elem for elem in html_obj.getchildren()[0].iterlinks()]
    return links[0][2]

def get_keyword(html_obj):
    return html_obj.getchildren()[0].text_content().strip()

def scrape_crisis_text_line():
    data = []
    source = "https://www.crisistextline.org/referrals"
    response = requests.get(source)
    html = lxml.html.fromstring(response.text)
    keyword = ''
    for table_row in html.xpath("//tr"):
        if table_row.getchildren()[0].values() == "sname":
            keyword = get_keyword(table_row)
        else:
            link = get_link(table_row)
            data.append((keyword, link, source))
    return data


    
