'''
A simple script to extract all the lessons from a specific course in Udemy and save to a TXT File

author: erickfabiani123@gmail.com (DevX3)
date: 2020-08-02
'''
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pathlib import Path
from utils import wait_selector
from time import sleep
import os

class Udemy:
    def __init__(self, url, output_file = None):

        self.lessons = []
        self.output_file = os.path.join(Path().home(), 'Desktop', 'course.txt') if output_file == None else output_file

        self.url = url

        # INIT 0 - Create Web Browser
        self._create_browser()
        # INIT 1 - Access Page
        self._access_course_page()
        # INIT 2 - Scroll Down to get visible all modules
        self._scroll_down_page()
        # INIT 3 - If the course have too many modules, we need to click in a button to see all of them
        self._click_curriculum_show_more()
        # INIT 4 - Click to expand all modules section
        self._expand_all_modules()
        # INIT 5 - Extract the lessons from modules
        self._extract_modules()
        # INIT 6 - Save info in a txt file
        self._save()
        # INIT 7 - Close WebBrowser!
        self.close()

    def _create_browser(self):
        print('starting a browser...')
        options = Options()
        options.headless = True
        self.webdriver = webdriver.Firefox(options=options, executable_path="geckodriver.exe")

    def _access_course_page(self):
        try:
            print(f"Acessing {self.url}...")
            self.webdriver.get(self.url)
        except Exception as e:
            print(e)

    def _scroll_down_page(self):
        # Scroll page to curriculum's course
        self.webdriver.execute_script('window.scrollTo(0, 1800);')
        sleep(1)

    def _click_curriculum_show_more(self):
        ''' button: curriculum--show-more--2tshH '''
        showMoreBtn = wait_selector( self.webdriver, '//button[contains(@class, "curriculum--show-more")]' )
        if showMoreBtn is not None:
            showMoreBtn.click()

    def _expand_all_modules(self):
        expandLink = wait_selector( self.webdriver, '//*[@data-purpose="expand-toggle"]' )
        if expandLink is not None:
            expandLink.click()

    def _extract_modules(self):
        print("Getting all modules...")
        modules = wait_selector(self.webdriver, '//*[contains(@class, "section--panel--")]', 'many')
        for i, module in enumerate(modules):
            self._extract_lessons_from_module((i, module))

    def _extract_lessons_from_module(self, module):
        moduleIndex, module = module
        try:
            lessons = module.find_elements_by_xpath('.//ul[contains(@class, "section--lecture-list--")]/li')

            for lesson in lessons:
                title = lesson.find_element_by_xpath(
                    './/div[contains(@class, "section--lecture-title-and-description")]/span').text
                time = lesson.find_element_by_xpath('.//span[contains(@class, "section--lecture-content")]').text
                self.lessons.append(self._mount_lessons(moduleIndex + 1, title, time))

        except Exception as e:
            print(e)

    def _mount_lessons(self, index, title, lesson_time):
        print(f"Mounting {index} - {title} ({lesson_time})")
        return '[MÓDULO {index}] {title} ({lesson_time})'.format( index=index, title=title, lesson_time=lesson_time )

    def _save(self):
        print("it's time to save in output file!")
        try:
            with open(self.output_file, 'w+') as f:
                for lesson in self.lessons:
                    f.write(f"{lesson}\n")
        except Exception as e:
            print(e)
        finally:
            print("Done!")

    def close(self):
        self.webdriver.quit()

if __name__ == '__main__':
    Udemy('https://www.udemy.com/course/python-3-do-zero-ao-avancado/')