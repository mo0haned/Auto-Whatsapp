import eel
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import qrcode
import os 
import time
import pandas as pd
import re
import sys
eel.init('')
op = webdriver.ChromeOptions()
op.add_argument("headless")
qr_xpath='//*[@id="app"]/div/div/div[2]/div[1]/div/div[2]/div'
reload_xpath='//*[@id="app"]/div/div/div[2]/div[1]/div/div[2]/div/span/div'
message_xpath='//*[@id="main"]/div[3]/div/div/div[3]/div[25]/div/div/div/div[2]/div/div/span'
click_xpath='//*[@id="main"]/footer/div[1]/div[3]/button'
phone_reg = r'[0-9]{11}'
send_link="https://web.whatsapp.com/send?phone="
op.add_argument("--disable-extensions")
op.add_argument("--disable-gpu")
op.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
op.add_experimental_option("excludeSwitches", ["enable-automation"])
op.add_experimental_option('useAutomationExtension', False)
i = 0
@eel.expose
def get_nums():
    eel.change_nums(len(numbers))

@eel.expose
def StartSendingProcess(message):
    global mess
    mess = message
    eel.st()

def try_to_click():
    global i
    notDone = True
    tries = 0
    while notDone:
        try:
            driver.find_element_by_xpath(click_xpath).click()
            notDone = False
            i+=1
        except Exception as ex:
            if tries > 10000:
                notDone = False
@eel.expose
def sender():
    global i
    if(i<len(numbers)):
        try:
            driver.get("https://www.google.com")
            driver.get(send_link+'+20'+numbers[i]+"&text="+mess)
            try_to_click()
        except :
            pass
        eel.ChSt("Messages Sent : "+str(i)+"/"+str(len(numbers))+".")
    else:
        eel.DoSt("All messages sent.")
        eel.notifier("I'm done","the app will close now")
        sys.exit()
    if(i%100 == 0):
        eel.notifier("Update","Done : "+str(i)+"/"+str(len(numbers)))

        

@eel.expose
def write(txt):
    fil = pd.read_excel(txt)
    cs = fil.to_csv()
    new_cs = re.sub(' ','',cs)
    new_cs = re.sub(r'/',' ',new_cs)
    global numbers
    numbers = re.findall(r'1[0-9]{9}',new_cs)
    eel.messages()
@eel.expose
def close_driver():
    driver.quit()
def redirect(link):
    driver.get(link)
def check_reload():
    try:
        reload_var = driver.find_element_by_xpath(reload_xpath)
        if reload_var:
            reload_var.click()
    except Exception as e :
        #print(e)
        pass
def get_qr():
    global last_qr
    try:
        qr = driver.find_element_by_xpath(qr_xpath)
        if qr:
            if os.path.exists("img.png"):
                os.remove("img.png")
            qr_value = qr.get_attribute('data-ref')
            if(qr_value == None):
                eel.slow_conn()
                time.sleep(1)
                get_qr()
            else:
                last_qr = qr_value
                img = qrcode.make(qr_value)
                img.save("img.png")
                eel.index_next()
    except Exception as e :
        print(e)
        eel.conecction_error()
        time.sleep(5)
        redirect('https://web.whatsapp.com')
@eel.expose 
def start():
    try:
        global driver
        global last_qr 
        last_qr = None
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=op)
        eel.check_login()
        redirect("https://web.whatsapp.com")
        get_qr()
    except Exception as e:
        print(e)
        eel.chrome_update()
@eel.expose
def check_login():
    try:
        login = driver.find_elements_by_id('side')
        if login:
            eel.loginConf()
        else:
            eel.check_again()
    except Exception as e:
        print("check again")
        eel.check_again()

@eel.expose
def qr_change():
    global last_qr
    check_reload()
    try:
        qr = driver.find_element_by_xpath(qr_xpath)
        if qr:
            qr_value = qr.get_attribute('data-ref') 
            if qr_value == last_qr:
                eel.no_change()
            else :
                last_qr = qr_value
                if os.path.exists("img.png"):
                    os.remove("img.png")
                img = qrcode.make(qr_value)
                img.save("img.png")
                if qr_value ==None:
                    qr_change()
                else:
                    eel.refresh_page()
    except:
        eel.LoginConfirm()    

eel.start("index.html",mode='electron',block=False)

while (True):
    eel.sleep(1)