from time import perf_counter
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def InitWebDriver(pathfile):
    return webdriver.Chrome(pathfile)
def Open(driver, link):
    driver.get(link)
    driver.find_element_by_link_text('Xem Anime').click()
def GetLink(driver):
    try:
        link = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="player"]/div[2]/div[3]/video'))
        )
        return link.get_attribute('src')
    except:
        try:
            Next_ep(driver)
            link = GetLink(driver)
            return link
        except:
            return 'Đã xảy ra sự cố trong lúc chương trình đang chạy'

def Next_ep(driver):
    next_ep = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/div[1]/div/div[3]/a[3]')
    next_ep.click()

if __name__ == '__main__':
    start_task = perf_counter()
    path = "C:\Program Files (x86)\chromedriver.exe"
    
    link = input("Nhập địa chỉ website: ")
    number_ep = int(input("Bạn muốn lấy link mấy tập?\nNhập số tập: "))

    driver = InitWebDriver(path)
    Open(driver,link)
    sleep(2)

    with open('Link_download_phim.txt', mode='a+') as file:
        for _ in range(number_ep):
            Link = GetLink(driver)
            print(Link)
            file.write(f'{Link}\n')
            Next_ep(driver)
            sleep(2)
    driver.quit()
    finish_task = perf_counter()
    print(f'\n\n\n\n\nChương trình kết thúc với thời gian là {round(finish_task - start_task,3)}')
    print('Chương trình đã kết thúc. hãy vào xem kết quả nào')
    