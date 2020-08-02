from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_selector(browser, selector, collection = 'one'):
    try:
        if collection is 'one':
            element = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, selector))
            )
        elif collection is 'many':
            element = WebDriverWait(browser, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, selector))
            )
    except Exception as e:
        print(e)
        element = None
    finally:
        return element