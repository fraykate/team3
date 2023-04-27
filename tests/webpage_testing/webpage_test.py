from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import unittest
import os


class Test_WebAccess(unittest.TestCase):
    def setUp(self):
        #Init Chrome Driver, install if not found
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        return

####Test for Access 4 Movie Search Results

    def test_webaccess_search_page(self):
        MOVIE_TITLES = ["Twilight", "Titanic", "Se7ven"]
        EXPECTED_RESULTS = ["Twilight", "Titanic", "Movie Not Found"]
        i = 0
        for movie in MOVIE_TITLES:
            #Navigate to search page
            self.driver.get("https://whatchawatchin.onrender.com/search/?")
            #Find the search bar
            element = self.driver.find_elements(By.NAME,"movie_name")
            #Type "Twilight" and hit Return
            element[0].send_keys(movie)
            element[0].send_keys(Keys.RETURN)
            #Print Title of resulting html page
            print(self.driver.title)
            self.assertEqual(self.driver.title, EXPECTED_RESULTS[i], "Incorrect Movie_Detail Page")
            i+=1

    def tearDown(self):
        try:
            self.driver.quit()
        except:
            "Driver quit failure"

if __name__ == '__main__':
    unittest.main()