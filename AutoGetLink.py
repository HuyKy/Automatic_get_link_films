
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
    xpath = '//*[@id="media"]/iframe'
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,xpath))
    )
    return element.get_attribute('src')

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
    start = '''⣿⡇⣿⣿⣿⠛⠁⣴⣿⡿⠿⠧⠹⠿⠘⣿⣿⣿⡇⢸⡻⣿⣿⣿⣿⣿⣿⣿
⢹⡇⣿⣿⣿⠄⣞⣯⣷⣾⣿⣿⣧⡹⡆⡀⠉⢹⡌⠐⢿⣿⣿⣿⡞⣿⣿⣿
⣾⡇⣿⣿⡇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣄⢻⣦⡀⠁⢸⡌⠻⣿⣿⣿⡽⣿⣿
⡇⣿⠹⣿⡇⡟⠛⣉⠁⠉⠉⠻⡿⣿⣿⣿⣿⣿⣦⣄⡉⠂⠈⠙⢿⣿⣝⣿
⠤⢿⡄⠹⣧⣷⣸⡇⠄⠄⠲⢰⣌⣾⣿⣿⣿⣿⣿⣿⣶⣤⣤⡀⠄⠈⠻⢮
⠄⢸⣧⠄⢘⢻⣿⡇⢀⣀⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠄⢀
⠄⠈⣿⡆⢸⣿⣿⣿⣬⣭⣴⣿⣿⣿⣿⣿⣿⣿⣯⠝⠛⠛⠙⢿⡿⠃⠄⢸
⠄⠄⢿⣿⡀⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⡾⠁⢠⡇⢀
⠄⠄⢸⣿⡇⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣫⣻⡟⢀⠄⣿⣷⣾
⠄⠄⢸⣿⡇⠄⠈⠙⠿⣿⣿⣿⣮⣿⣿⣿⣿⣿⣿⣿⣿⡿⢠⠊⢀⡇⣿⣿
⠒⠤⠄⣿⡇⢀⡲⠄⠄⠈⠙⠻⢿⣿⣿⠿⠿⠟⠛⠋⠁⣰⠇⠄⢸⣿⣿⣿
⠄⠄⠄⣿⡇⢬⡻⡇⡄⠄⠄⠄⡰⢖⠔⠉⠄⠄⠄⠄⣼⠏⠄⠄⢸⣿⣿⣿
⠄⠄⠄⣿⡇⠄⠙⢌⢷⣆⡀⡾⡣⠃⠄⠄⠄⠄⠄⣼⡟⠄⠄⠄⠄⢿⣿⣿'''
    for kaka in start:
        print(kaka,end='',flush=False)
        sleep(0.01)
    error_list=[]
    ErroName = "Dảk bủh"
    loop=1
    path = input("Enter chromedriver path: <Example: C:\Program Files (x86)\chromedriver.exe>")
    sleep(3)
    NameAnime = input('Enter your anime: <Example: https://anime47.com/xem-phim-dragon-ball-super-ep-001/124989.html>')
    os.system('cls')
    print("WAIT A MOMENT!!!")
    start1 = '''⣿⣿⣷⡁⢆⠈⠕⢕⢂⢕⢂⢕⢂⢔⢂⢕⢄⠂⣂⠂⠆⢂⢕⢂⢕⢂⢕⢂⢕⢂
⣿⣿⣿⡷⠊⡢⡹⣦⡑⢂⢕⢂⢕⢂⢕⢂⠕⠔⠌⠝⠛⠶⠶⢶⣦⣄⢂⢕⢂⢕
⣿⣿⠏⣠⣾⣦⡐⢌⢿⣷⣦⣅⡑⠕⠡⠐⢿⠿⣛⠟⠛⠛⠛⠛⠡⢷⡈⢂⢕⢂
⠟⣡⣾⣿⣿⣿⣿⣦⣑⠝⢿⣿⣿⣿⣿⣿⡵⢁⣤⣶⣶⣿⢿⢿⢿⡟⢻⣤⢑⢂
⣾⣿⣿⡿⢟⣛⣻⣿⣿⣿⣦⣬⣙⣻⣿⣿⣷⣿⣿⢟⢝⢕⢕⢕⢕⢽⣿⣿⣷⣔
⣿⣿⠵⠚⠉⢀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⢕⢕⢕⢕⢕⢕⣽⣿⣿⣿⣿
⢷⣂⣠⣴⣾⡿⡿⡻⡻⣿⣿⣴⣿⣿⣿⣿⣿⣿⣷⣵⣵⣵⣷⣿⣿⣿⣿⣿⣿⡿
⢌⠻⣿⡿⡫⡪⡪⡪⡪⣺⣿⣿⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
⠣⡁⠹⡪⡪⡪⡪⣪⣾⣿⣿⣿⣿⠋⠐⢉⢍⢄⢌⠻⣿⣿⣿⣿⣿⣿⣿⣿⠏⠈
⡣⡘⢄⠙⣾⣾⣾⣿⣿⣿⣿⣿⣿⡀⢐⢕⢕⢕⢕⢕⡘⣿⣿⣿⣿⣿⣿⠏⠠⠈
⠌⢊⢂⢣⠹⣿⣿⣿⣿⣿⣿⣿⣿⣧⢐⢕⢕⢕⢕⢕⢅⣿⣿⣿⣿⡿⢋⢜⠠⠈
⠄⠁⠕⢝⡢⠈⠻⣿⣿⣿⣿⣿⣿⣿⣷⣕⣑⣑⣑⣵⣿⣿⣿⡿⢋⢔⢕⣿⠠⠈
⠨⡂⡀⢑⢕⡅⠂⠄⠉⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⢔⢕⢕⣿⣿⠠⠈
⠄⠪⣂⠁⢕⠆⠄⠂⠄⠁⡀⠂⡀⠄⢈⠉⢍⢛⢛⢛⢋⢔⢕⢕⢕⣽⣿⣿⠠⠈'''
    for keke in start1:
        print(keke,end='',flush=False)
        sleep(0.001)
    sleep(3)
    texts = '''*✲*´*。.❄¯*✲。❄。*¨`*✲´*。❄¨`*✲。❄。*`*
*╔════════════ ༺❀༻❤༺❀༻ ════════════╗*
*♥*❄¯*✲❄♫♪♩░B░E░A░U░T░I░F░U░L░ ♫♫♪❄¯*✲❄
*╚════════════ ༺❀༻❤༺❀༻ ════════════╝*
*✲*´*。.❄¯*✲。❄。*¨`*✲´*。❄¨`*✲。❄。*`*'''
    InitWebDriver(path=path,Link=NameAnime)
    os.system('cls')
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
                    assert "lmao" in ErroName
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
                        link = SeverFe(driver)
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
EndGame = input('\nNhập một ký tự để thoát chương trình')
