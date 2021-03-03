
import os
import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def InitWebDriver(path,Link):
    global driver
    driver = webdriver.Chrome(executable_path=path)
    driver.get(Link)

def GetLink(driver):
    xpath = '//*[@id="player"]/div[2]/div[3]/video'
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,xpath))
    )
    return element.get_attribute('src')

def Next(driver):
    xpath = '/html/body/div[5]/div[2]/div[1]/div[1]/div/div[3]/a[3]'
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,xpath))
    )
    element.click()
def Check(driver):
    xpath = '/html/body/div[5]/div[2]/div[1]/div[1]/div/div[3]/a[3]'
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,xpath))
    )
    agr = element.get_attribute('onclick')
    if agr == "nextEpisodeHand('');":
        return True
    else:
        return False

def SeverFa(driver):
    id = 'clicksv'
    element = WebDriverWait(driver,60).until(
        EC.presence_of_element_located((By.ID,id))
    )
    element.find_element_by_id('sv2').click()
def SeverFe(driver):
    id = 'clicksv'
    element = WebDriverWait(driver,60).until(
        EC.presence_of_element_located((By.ID,id))
    )
    element.find_element_by_id('sv4').click()

def CheckLink(LinkFilm):
    pattern = re.compile('blob:https://anime47.com/')
    result = pattern.search(LinkFilm)
    if result:
        return True
    else:
        return False

def MainSession(driver):
    return driver.current_window_handle

if __name__ == '__main__':
    os.system('cls')
    print("WELLCOME!!!")
    print('''_______________¶¶¶¶____________¶¶¶¶
_____________¶¶¶¶¶¶¶__________¶¶¶¶¶¶¶
_________________¶¶¶_________¶¶¶
________¶¶¶¶_____¶¶¶_________¶¶¶_____¶¶¶¶
______¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶
____¶¶¶¶¶¶¶¶¶¶___¶¶¶¶11111111¶¶¶¶___¶¶¶¶¶_¶¶¶¶¶
__¶¶¶¶¶___¶¶¶¶__¶¶¶¶¶111111111¶¶¶¶__¶¶¶¶_____¶¶¶¶
_¶¶¶_______¶¶¶¶¶¶¶¶¶¶¶1111111¶¶¶¶¶¶¶¶¶¶_________¶¶
_¶¶_________¶¶¶1¶¶¶¶¶¶¶11111¶¶¶¶¶1¶¶¶¶__________¶¶
____________¶¶¶1¶¶¶¶¶¶¶¶111¶¶¶¶¶¶¶1¶¶¶
________¶¶¶__¶11¶¶¶¶¶¶¶1111¶¶¶¶¶¶¶11¶__¶¶¶¶
_______¶¶¶¶¶¶¶11¶¶¶¶¶¶1111111¶¶¶¶¶1¶¶¶¶¶¶¶¶¶
______¶¶¶¶¶¶¶¶¶1¶¶¶¶1111111111¶¶¶¶1¶¶¶¶¶¶¶¶¶¶¶
_____¶¶¶¶_¶¶¶¶¶11¶¶¶11111111111¶¶11¶¶¶¶¶__¶¶¶¶¶
___¶¶¶¶¶____¶¶¶¶1¶¶111111111111¶¶1¶¶¶_______¶¶¶¶
__¶¶¶¶____¶¶¶¶¶¶¶¶¶¶1111111111¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶
_¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111¶¶¶¶¶¶¶¶¶¶¶¶¶¶______¶¶
¶¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶
_______¶¶¶¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______¶¶¶¶
_______¶¶¶¶________¶¶¶¶¶¶¶¶¶¶¶¶________¶¶¶¶¶
______¶¶¶¶_________¶¶¶¶¶¶¶¶¶¶¶¶¶________¶¶¶¶
______¶¶¶_________¶¶¶¶__¶¶¶__¶¶¶_________¶¶¶¶
_____¶¶¶__________¶¶¶_O_¶¶¶_O_¶¶¶_________¶¶¶
_____¶¶___________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________¶¶¶
____¶¶_____________¶¶_¶¶¶¶¶¶¶_¶¶____________¶¶
____¶_______________¶¶¶_____¶¶¶_____________¶
____¶________________¶¶_____¶¶_____________¶
_____¶____________________________________¶''')
    error_list=[]
    loop=1
    path = "C:\Program Files (x86)\chromedriver.exe"
    sleep(3)
    NameAnime = input('Enter your anime: ')
    os.system('cls')
    print("WAIT A MOMENT!!!")
    print('''__________________________¶¶_______________
__________________¶¶____¶¶_________________
__________¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶______________
______¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________________
__¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶_____¶¶___¶¶¶¶________
__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶¶¶¶______
____¶¶¶¶¶¶__¶¶____¶¶¶¶¶¶_________¶¶¶¶¶¶____
____¶¶______¶¶¶¶______¶¶¶¶¶¶___¶¶¶¶¶¶¶¶____
____________¶¶________¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶__
________¶¶__¶¶________¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶__
__________¶¶________¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶
________________¶¶¶¶¶¶¶¶¶¶_¶¶____¶¶¶¶__¶¶¶¶
________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶____¶¶¶¶¶¶¶¶
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶__¶¶¶__¶¶¶¶____¶¶¶¶¶¶__¶¶
¶¶__¶¶¶¶¶¶¶¶____¶¶__¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶__¶¶
¶__¶¶¶¶¶¶¶¶____________¶¶__¶¶¶¶¶¶¶¶¶¶¶¶___¶
___¶¶¶¶¶¶____¶¶¶¶________¶¶__________¶¶____
__¶¶¶¶¶¶_______¶¶¶¶____________________¶¶__
__¶¶¶¶¶¶¶_______¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____
__¶¶¶¶¶¶¶¶______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______
___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____
_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________¶¶¶¶¶¶¶¶__
_______¶¶¶¶¶¶¶¶¶¶¶¶¶_________¶¶____¶¶¶¶¶¶__
_________¶¶¶¶¶¶____________¶¶¶¶¶¶__¶¶¶¶¶¶¶¶
___________¶¶____________¶¶¶¶¶¶____¶¶¶¶¶¶¶¶
__________________________¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶
_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___¶
_____¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶______
___¶¶¶¶______________¶¶¶¶¶¶______¶¶________
___¶¶__¶¶______________¶¶__________________
_¶¶__¶¶____________________________________
___¶¶___________¶¶__¶¶¶¶¶¶¶¶¶¶¶¶___________
___¶¶___¶¶¶______¶¶__¶¶¶¶_______¶¶_________
_¶¶____¶¶¶¶¶¶¶__¶¶¶¶¶¶_________¶¶¶_________
_¶¶¶¶__¶¶__¶¶¶¶¶¶¶¶¶_________¶¶¶¶__________
_¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶_____________________
___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶___________________
_____¶¶¶¶¶¶¶¶¶¶¶___________________________
______________¶¶___________________________''')
    sleep(3)
    texts = '''*✲*´*。.❄¯*✲。❄。*¨`*✲´*。❄¨`*✲。❄。*`*
*╔════════════ ༺❀༻❤༺❀༻ ════════════╗*
*♥*❄¯*✲❄♫♪♩░B░E░A░U░T░I░F░U░L░ ♫♫♪❄¯*✲❄
*╚════════════ ༺❀༻❤༺❀༻ ════════════╝*
*✲*´*。.❄¯*✲。❄。*¨`*✲´*。❄¨`*✲。❄。*`*'''
    InitWebDriver(path=path,Link=NameAnime)
    MainWindow = MainSession(driver)
    with open('link_download.txt', mode='w+') as fjob:
        while True:
            try:
                link = GetLink(driver)
                check_link = CheckLink(link)
                if CheckLink == False:
                    fjob.write(link+'\n')
                    result = Check(driver)
                    print(link+'\n')
                    if result == True:
                        break
                    else:
                        Next(driver)
                        loop+=1
                        driver.switch_to.window(MainWindow)
                else:
                    try:
                        SeverFa(driver)
                        link = GetLink(driver)
                        fjob.write(link+'\n')
                        result = Check(driver)
                        print(link+'\n')
                        if result == True:
                            break
                        else:
                            Next(driver)
                            loop+=1

                            driver.switch_to.window(MainWindow)
                    except:
                        SeverFe(driver)
                        link = GetLink(driver)
                        fjob.write(link+'\n')
                        result = Check(driver)
                        print(link+'\n')
                        if result == True:
                            break
                        else:
                            Next(driver)
                            loop+=1

                            driver.switch_to.window(MainWindow)
            except:
                try:
                    SeverFa(driver)
                    link = GetLink(driver)
                    fjob.write(link+'\n')
                    result = Check(driver)
                    print(link+'\n')
                    if result == True:
                        break
                    else:
                        Next(driver)
                        loop+=1
                        driver.switch_to.window(MainWindow)
                        
                except:
                    try:
                        SeverFe(driver)
                        link = GetLink(driver)
                        fjob.write(link+'\n')
                        result = Check(driver)
                        print(link+'\n')
                        if result == True:
                            break
                        else:
                            Next(driver)
                            loop+=1

                            driver.switch_to.window(MainWindow)
                            
                    except:
                        error_list.append(loop)
                        loop+=1
                        result = Check(driver)
                        if result == True:
                            break
                        else:
                            Next(driver)
                            loop+=1

                            driver.switch_to.window(MainWindow)
    driver.quit()
    sleep(3)
    print('''░▄▀▄▀▀▀▀▄▀▄░░░░░░░░░
░█░░░░░░░░▀▄░░░░░░▄░
█░░▀░░▀░░░░░▀▄▄░░█░█
█░▄░█▀░▄░░░░░░░▀▀░░█
█░░▀▀▀▀░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░█
░█░░▄▄░░▄▄▄▄░░▄▄░░█░
░█░▄▀█░▄▀░░█░▄▀█░▄▀░
░░▀░░░▀░░░░░▀░░░▀░░░''')
    print("We Done!!!")
    if error_list:
        print("Các tập lỗi là:"+str(error_list))
    else:
        print("Không có tập nào bị lỗi.Tất cả đã được tải hết")
    for text in texts:
        print(text,end='',flush=False)
        sleep(0.05)

