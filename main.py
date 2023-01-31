
from emails import Tenminutesemail
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time
import random
from proxy import create_proxy_file
from generation import Generation
from config import settings
from database import Database
import os


# set driver settings
def settings_for_driver(use_proxy):
    options = Options()
    service = Service(settings['path_to_chromedriver'])
    options.add_argument('--disable-blink-features=AutomationControlled')  # hide webdriver usage
    ua = Generation.set_random_user_agent()  # get useragent value
    options.add_argument(f'user-agent={ua}')  # set User-agent
    options.add_argument('--lang=en')  # set browser language
    if use_proxy:
        create_proxy_file()
        options.add_extension('utils\proxy_auth_plugin.zip')  # use proxy
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options, service=service)
    return driver


# create account
def create_account(driver, i):
    try:
        # open Instagram registration page
        driver.get('https://www.instagram.com/accounts/emailsignup/')

        # generate data (name, surname, fullname, password)
        generation = Generation()
        fullname = generation.generate_fullname()
        name, surname = fullname[0], fullname[1]
        username = name + surname + str(random.randint(1000, 2000))
        password = generation.generate_password()

        # get email address
        tenminutesemail = Tenminutesemail()
        email = tenminutesemail.get_email_address()

        # complete the registration form
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'emailOrPhone'))).send_keys(email)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'fullName'))).send_keys(name + ' ' + surname)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'username'))).send_keys(username)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys(password)
        time.sleep(5)
        driver.find_elements(By.CLASS_NAME, '_acan._acap._acas._aj1-')[1].click()

        # set birthday
        time.sleep(2)
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, '_aau-')))
        Select(driver.find_elements(By.CLASS_NAME, '_aau-')[0]).select_by_value(str(random.randint(1, 12)))
        Select(driver.find_elements(By.CLASS_NAME, '_aau-')[1]).select_by_value(str(random.randint(1, 28)))
        Select(driver.find_elements(By.CLASS_NAME, '_aau-')[2]).select_by_value(str(random.randint(1980, 2000)))
        time.sleep(5)
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, '_acan._acap._acaq._acas'))).click()

        # enter confirmation code
        code = tenminutesemail.get_instagram_code()
        tenminutesemail.close_session()
        driver.find_element(By.NAME, 'email_confirmation_code').send_keys(code)
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, '_acan._acap._acaq._acas').click()

        # if account was created press "Turn on"
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, '_a9--._a9_0'))).click()
        print(f'\033[0;92m{i}: {email}, {password}, {time.strftime("%d-%m-%Y %H:%M:%S")} \033[00m')

        # get cookies, date, user agent
        all_cookies = str(driver.get_cookies())
        date = time.strftime("%d-%m-%Y")
        ua = driver.execute_script("return navigator.userAgent;")

        # save data to database
        if not os.path.isfile('accounts.db'):
            Database.create_db()
        Database.save_data_to_db(date, username, email, password, all_cookies, ua)

    except Exception as e:
        print(f'{i}: failed account creation')
        print(e)

    finally:
        driver.quit()


def main():
    i = 1
    while True:
        driver = settings_for_driver(use_proxy=False)
        create_account(driver, i)
        i += 1


if __name__ == '__main__':
    main()