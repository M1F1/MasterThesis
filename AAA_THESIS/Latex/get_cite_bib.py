import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import json
import pyperclip

def replace_article_id_with_label(exported_citation, label):
    return re.sub(r'^(@ARTICLE{)(.*),', r'\1{},'.format(label), exported_citation)

if __name__ == "__main__":
    browser = webdriver.Firefox()
    browser.maximize_window()

    with open('urls.json') as f:
        urls = json.load(f)
    print(urls)

    # for label, url1 in urls.items():
    label = 'FixMatch'
    url1 = urls[label]

    browser.get(url1)
    element = browser.find_element_by_link_text('NASA ADS')

    url2 = link = element.get_attribute('href')
    browser.get(url2)

    export_citation_element=browser.find_element_by_css_selector(
        "div#left-column > div:nth-child(1) > nav:nth-child(1) > a:nth-child(10)"
    )
    browser.execute_script("arguments[0].click();", export_citation_element)

    element = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Copy to Clipboard')]"))
    ).click()

    bibtext = pyperclip.paste()
    replaced_bibtext_label = replace_article_id_with_label(bibtext, label)
    # check if exist if not create
    with open('literature.bib') as bib:
        # append in the end
    

    

