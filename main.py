from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

visited_urls = []

driver = webdriver.Chrome()
urls = ['http://lib.ru/']

while urls:
    url = urls.pop(0)
    visited_urls.append(url)
    print(f"Visiting URL: {url}")
    driver.get(url)
    sleep(2)

    try:
        # Попробуем найти и записать содержимое <pre> элемента, если оно есть
        pre_elements = driver.find_elements(By.XPATH, '//pre')
        if pre_elements:
            for pre in pre_elements:
                print("Found <pre> element, writing to texts.txt.")
                with open('texts.txt', 'a', encoding='utf-8') as f:
                    f.write(pre.text)
                    print(pre.text)
        else:
            print("No <pre> elements found, looking for <a> links.")

        elements = driver.find_elements(By.XPATH, '//a')
        for element in elements:
            href = element.get_attribute('href')
            if href is None:
                print("Skipping an element with no href.")
                continue
            if '#' in href:
                print("Skipping an anchor link.")
                continue
            if 'http' in href and 'http://lib.ru/' not in href:
                print("Skipping an external link.")
                continue
            if 'http' not in href:
                if url[-1] == '/':
                    href = url + href
                else:
                    href = 'http://lib.ru/' + href
            if href in visited_urls:
                print(f"Skipping already visited URL: {href}")
                continue
            print(f"Adding URL to visit: {href}")
            urls.append(href)
            urls = list(set(urls))
    except Exception as e:
        print(f"An error occurred: {e}")

print("Scraping complete")
driver.quit()
