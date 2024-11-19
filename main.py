from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pywinauto import Application
from pywinauto.findwindows import find_windows
import time
import random

authorization_way = input('Выберите способ входа в аккаунт/регистрации (google/email): ')
        
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome()

driver.implicitly_wait(20)
time.sleep(5)
driver.get('https://app.towns.com/t/10b5b35c9d40a614a1c434660c02be41f4b08c338d0000000000000000000000/?invite')
def auth(authorization_way, driver):
    # Join
    try:
        first_button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div/div[3]/div/div/div/button')
        first_button.click()
    except:
        try:
            first_button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div/div[3]/div/button')
            first_button.click()
            confirm = driver.find_element(By.XPATH, '//*[@id="above-app-progress-root"]/div/div[2]/div/div/button')
            confirm.click()
            print('You are logged in')
        except:
            print('you are logged in')
            return ''
    else:
        # Google
        if authorization_way == 'google':
            second_button = driver.find_element(By.XPATH, '//*[@id="privy-modal-content"]/div/div[1]/div[3]/div/button[1]')
            second_button.click()
            third_button = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/form/span/section/div/div/div/div/ul/li[1]')
            third_button.click()
            try:
                confirm = driver.find_element(By.XPATH, '//*[@id="above-app-progress-root"]/div/div[2]/div/div/button')
                confirm.click()
            except:
                pass
            finally:
                print('authorization passed')

        # Email
        elif authorization_way == 'email':
            email = input('Enter email: ')
            second_button = driver.find_element(By.XPATH, '//*[@id="email-input"]')
            second_button.send_keys(email)
            second_button.send_keys(Keys.ENTER)
            code = input('enter code: ')
            third_button = driver.find_element(By.XPATH, '//*[@id="privy-modal-content"]/div/div[1]/div[2]/div[2]/div[1]/div[2]/input[1]')
            third_button.send_keys(code)
            third_button.send_keys(Keys.ENTER)
            try:
                confirm = driver.find_element(By.XPATH, '//*[@id="above-app-progress-root"]/div/div[2]/div/div/button')
                confirm.click()
            except:
                pass
            finally:
                print('authorization passed')
        else:
            driver.quit()
            return 'incorrect response'

def communicate(driver):
    try:
        join = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/div[3]/div/div[3]/div/button')
    except:
        f = open('servers.txt')
        for i in f:
            x = random.randint(0, 1)
            if x == 1:
                driver.get(i.split('\n')[0])
                time.sleep(10)
                text_box = driver.find_element(By.CSS_SELECTOR, "div[data-testid='send-message-text-box']")
                x = open('text.txt')
                s = x.readlines()
                index = random.randint(0, len(s) - 1)
                text_box.send_keys((s[index]).split('\n')[0])
                f = driver.find_element(By.XPATH, '//*[@id="editor-container"]/div[2]/div[2]/div[1]/div[2]/div/div/button/div')
                f.click()
            else:
                continue
    else:
        join.click()
        confirm = driver.find_element(By.XPATH, '//*[@id="above-app-progress-root"]/div/div[2]/div/div/button')
        confirm.click()
        f = open('servers.txt')
        for i in f:
            x = random.randint(0, 1)
            if x == 1:
                driver.get(i.split('\n')[0])
                time.sleep(10)
                text_box = driver.find_element(By.CSS_SELECTOR, "div[data-testid='send-message-text-box']")
                x = open('text.txt')
                s = x.readlines()
                index = random.randint(0, len(s) - 1)
                text_box.send_keys((s[index]).split('\n')[0])
                f = driver.find_element(By.XPATH, '//*[@id="editor-container"]/div[2]/div[2]/div[1]/div[2]/div/div/button/div')
                f.click()
            else:
                continue
        
    
def create(driver):
    driver.get('https://app.towns.com/t/new')
    create_button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/a/div/div/div')
    create_button.click()
    time.sleep(2)
    town_name = input('Enter server name: ')
    town_name_button = driver.find_element(By.XPATH, '//*[@id="spaceName"]')
    town_name_button.send_keys(town_name)
    town_name_button.send_keys(Keys.ENTER)
    time.sleep(2)
    town_motto = input('Enter server motto: ')
    town_motto_button = driver.find_element(By.XPATH, '//*[@id="shortDescription"]')
    town_motto_button.send_keys(town_motto)
    town_motto_button.send_keys(Keys.ENTER)
    time.sleep(2)
    town_des = input('Enter server description: ')
    town_des_button = driver.find_element(By.XPATH, '//*[@id="longDescription"]')
    town_des_button.send_keys(town_des)
    town_des_button.send_keys(Keys.ENTER)
    time.sleep(2)
    image = driver.find_element(By.XPATH, '//*[@id="gradients"]')
    image.click()
    time.sleep(2)
    image = input('Enter path to image: ')
    chrome_windows = find_windows(class_name='Chrome_WidgetWin_1')
    for hwnd in chrome_windows:
        app = Application().connect(handle=hwnd)
        window = app.window(handle=hwnd)
        if 'Towns' in window.window_text():
            handle = hwnd
            break
    app = Application(backend = 'uia').connect(class_name = 'Chrome_WidgetWin_1', handle = handle)
    file_dlg = app.top_window().child_window(title = 'Открытие').child_window(class_name = 'ComboBox', title = 'Имя файла:').child_window(class_name = 'Edit', title = 'Имя файла:')
    file_dlg.set_text(f'{image}')
    open_button = app.top_window().child_window(title = 'Открытие').child_window(class_name = 'Button', title = 'Открыть').click()
    time.sleep(5)
    create_button = driver.find_element(By.XPATH, '//*[@id="CreateSpaceFormV2"]/div/div/div[3]/div/div[3]/button')
    create_button.click() 
    time.sleep(50)
    try:
        confirm = driver.find_element(By.XPATH, '//*[@id="above-app-progress-root"]/div/div[2]/div/div/button')
        confirm.click()
    except:
        print('deneg netu')
    else:
        print('Server has created')
auth(authorization_way, driver)
time.sleep(5)
communicate(driver)
time.sleep(5)
a = input('Do you want to create server? (yes/no): ')
if a == 'yes':
    create(driver)
    driver.quit()
else:
    driver.quit()
