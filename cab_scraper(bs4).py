from bs4 import BeautifulSoup
from selenium import webdriver
import time
import signal

# The file is not used anymore but I didn't want to get rid of my hard work
driver = None
url = 'https://embed.liveviewgps.com/embed.aspx?id=UTDALLAS'
DEBUG = False
CAB_NAMES = [u'Rutford North',
             u'Rutford South',
             u'McDermott',
             u'Canyon Creek',
             u'Phase 4-7',
             u'Commons',
             u'Phase 1-3']


def setup():
    global driver
    driver = webdriver.PhantomJS()


def get_page():
    if DEBUG:
        with open('test_output.html') as f:
            return f.read()
    global driver
    driver.get(url)
    time.sleep(10)
    html_source = driver.page_source
    return html_source


def analyze_page():
    html_source = get_page()
    soup = BeautifulSoup(html_source, "html.parser")
    all_info = soup.find_all("div", class_="infofirst")
    analyze_info(all_info)


def analyze_info(all_info):
    for info in all_info:
        cab_name = info.h1.text.strip()
        if cab_name in CAB_NAMES:
            print 'Cab: %s' % cab_name

            cab_ul = info.ul
            list_items = cab_ul.find_all('li')
            print 'Cab Info: '
            for list_item in list_items:
                item_content = list_item.text.strip()
                item_content = item_content.replace('\n', '')
                print '\t' + item_content

            print '\n'


def cleanup_driver():
    global driver
    driver.service.process.send_signal(signal.SIGTERM)
    driver.quit()


setup()
analyze_page()
cleanup_driver()
