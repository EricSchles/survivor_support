from requests import Session
import lxml.html
import time

def get_keywords():
    session = Session()
    r = session.get("https://www.crisistextline.org/referrals")
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
    
def get_links(keyword):
    keywords = get_keywords()
    with Session() as session:
        post = session.post(
            "https://www.crisistextline.org/referrals",
            data={"myInput": keyword}
        )
        r = session.get("https://www.crisistextline.org/referrals")
        html = lxml.html.fromstring(r.text)
        bad_links = get_bad_links(html)
    return get_good_links(html, bad_links)
        
def scrape_crisis_text_line():
    keywords = get_keywords()
    data = []
    source = "https://www.crisistextline.org/referrals"
    for keyword in keywords:
        time.sleep(100)
        links = get_links(keyword)
        for link in links:
            data.append((keyword, link, source))
    return data
    
