from selenium import webdriver
from time import sleep

def InitWebDriver(Path):
    return webdriver.Chrome(executable_path=Path)

def OpenWeb(driver,link):
    driver.get(link)

def Clicking(driver,text):
    element = driver.find_element_by_link_text(text)
    return element
if __name__ == '__main__':

    Path = "C:\Program Files (x86)\chromedriver.exe"
    link = "https://www.youtube.com/watch?v=2Tuo5u39qM8&t=605s"
    text = '10:05'

    driver = InitWebDriver(Path)
    OpenWeb(driver,link)
    while True:
        driver.refresh()
        sleep(154)
        