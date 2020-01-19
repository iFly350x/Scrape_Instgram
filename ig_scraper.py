import bs4 as inspect
import time
import urllib.request
import os
from selenium import webdriver
import json

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)
print(chrome_options.binary_location)

DICT_KEYS = ('POSTS', 'Followers', 'Following')
def start_serach():
    global followers
    instgram_src = "https://www.instagram.com/"
    profile_src = 'victorhellomyname'
    full_source = f"{instgram_src}{profile_src}/"
    driver.get(full_source)
    time.sleep(1)
    content = driver.page_source.encode('utf-8').strip()
    soup = inspect.BeautifulSoup(content, 'html.parser')
    final_list = dict()
    for numbers, k in zip(soup.find_all('span', class_='g47SY'), DICT_KEYS):
        final_list[k] = int(numbers.text)
    json_file = json.dumps(final_list)
    print(json_file)

start_serach()
