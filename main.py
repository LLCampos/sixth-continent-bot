import csv
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def load_credentials():
    with open('credentials.csv', mode='r') as f:
        reader = csv.reader(f)
        credentials = {}
        for row in reader:
            credentials[row[0]] = row[1]
        return credentials


def login(driver, email, password):
    driver.find_element_by_link_text("Login").click()
    sleep(1)
    driver.find_element_by_id("loginEmail").send_keys(email)
    sleep(1)
    driver.find_element_by_id("pwdReg").send_keys(password)
    sleep(1)
    driver.find_element_by_xpath("//a[@data-ng-click='getLogin()']").click()
    sleep(5)


def get_sixthcontinent(driver):
    driver.get("https://pt.sixthcontinent.com/")


def go_to_wallet(driver):
    driver.find_element_by_link_text("Perfil").click()
    sleep(1)
    driver.find_element_by_link_text("Carteira").click()
    sleep(4)
    try:
        driver.find_element_by_link_text("Rejeitar").click()
    except NoSuchElementException:
        pass


if __name__ == "__main__":
    credentials = load_credentials()
    for email, password in credentials.items():
        with webdriver.Chrome() as driver:
            get_sixthcontinent(driver)
            sleep(1)
            login(driver, email, password)
            go_to_wallet(driver)
            sleep(3)