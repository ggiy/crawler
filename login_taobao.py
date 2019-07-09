'''
先在命令行输入“ mitmweb -s 文件路径”开启mitmdump
'''
import selenium
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime
import re
from pykeyboard import PyKeyboard

url = 'https://www.taobao.com'
telephone = '18479362797'
password = 'haoge1228'
buy_password = [1, 2, 4, 8, 7, 8]


def login_taobao(telephone, password, buy_password, url='https://www.taobao.com'):
    proxy = '127.0.0.1:8080'
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--proxy-server=http://' + proxy)
    browser = webdriver.Firefox(firefox_options=firefox_options)
    wait = WebDriverWait(browser, 10)
    browser.get(url)
    sleep(3)
    browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/ul[1]/li[2]/div[1]/div[1]/a[1]').click()
    sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div[4]/div/div[5]/a[1]')))
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div[4]/div/div[5]/a[1]').click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="TPL_username_1"]')))
    browser.find_element_by_xpath('//*[@id="TPL_username_1"]').send_keys(telephone)
    browser.find_element_by_xpath('//*[@id="TPL_password_1"]').send_keys(password)
    browser.find_element_by_xpath('//*[@id="J_SubmitStatic"]').click()
    sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/ul[2]/li[3]/div[1]/a/span[2]')))
    browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/ul[2]/li[3]/div[1]/a/span[2]').click()
    sleep(3)
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div[1]/div/label')))
    except:
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="TPL_password_1"]')))
        browser.find_element_by_xpath('//*[@id="TPL_password_1"]').send_keys(password)
        browser.find_element_by_xpath('//*[@id="J_SubmitStatic"]').click()
        sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div[1]/div/label')))
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div[1]/div/label').click()
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div[3]/div[5]/a/span').click()
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div[4]/h2')))
    browser.execute_script('window.scrollTo(0, 740)')
    sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div[9]/div/a[2]')))
    browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[9]/div/a[2]').click()
    sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/form/div[1]/div/ul[2]/li/div[1]/label/span[2]')))
    buy_password = list(buy_password)
    k = PyKeyboard()
    for i in buy_password:
        sleep(1)
        k.press_key(i)
        k.release_key(i)
    browser.find_element_by_xpath('//*[@id="J_authSubmit"]').click()
    sleep(4)

if __name__ == "__main__":
    '''
    re_compile = re.compile('0:00:0.*')
    now = datetime.today()
    target_time = datetime(2019, 6, 17, 23, 54)
    if re_compile.match(str(now - target_time)):
    '''
    login_taobao(telephone, password, buy_password)





