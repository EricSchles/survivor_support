import lxml.html
import time
import code
import random
import requests

def get_link(html_obj):
    links = [elem for elem in html_obj.getchildren()[0].iterlinks()]
    return links[0][2]
    
def get_keyword(html_obj, keyword):
    #code.interact(local=locals())
    try:
        if html_obj.getchildren()[0].values()[0] == "sname":
            return html_obj.getchildren()[0].text_content().strip(), True
        else:
            return keyword, False
    except:
        return keyword, False
    
def scrape_crisis_text_line():
    data = []
    source = "https://www.crisistextline.org/referrals"
    response = requests.get(source)
    html = lxml.html.fromstring(response.text)
    keyword = ''
    for table_row in html.xpath("//tr"):
        keyword, new_keyword = get_keyword(table_row, keyword)
        if not new_keyword:
            try:
                link = get_link(table_row)
                data.append((link, keyword, source))
            except:
                continue
    return data


    
