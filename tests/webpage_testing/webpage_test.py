from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

MOVIE_TITLES = ["Twilight", "Titanic", "Se7ven"]
EXPECTED_RESULTS = ["Twilight", "Titanic", "Movie Not Found"]
i = 0
#Init Chrome Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for movie in MOVIE_TITLES:
    #Navigate to search page
    driver.get("https://whatchawatchin.onrender.com/search/?")
    #Find the search bar
    element = driver.find_elements(By.NAME,"movie_name")
    #Type "Twilight" and hit Return
    element[0].send_keys(movie)
    element[0].send_keys(Keys.RETURN)
    #Print Title of resulting page
    print(driver.title)
    assert(driver.title, EXPECTED_RESULTS[i])
    i+=1