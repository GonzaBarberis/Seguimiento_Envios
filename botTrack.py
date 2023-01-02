from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import telebot
from flask import Flask, request
from waitress import serve
import os
import sys
from collections.abc import MutableMapping
import threading

token = '5772840428:AAH9RQxRGdBzmfjSZ9TxLUGZsqVD-lUvyH8'
id = 5760438151

bot = telebot.TeleBot(token)
webserver = Flask(__name__)


#POST (enviar informacion al seridor)
@webserver.route("/", methods=['POST'])
def webhook():
    if request.headers.get("content-type") == "application/json":
        update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
        bot.process_new_updates([update])
        return "OK", 200



#bot.send_message(5760438151,"Esta funcionando")


def iniciarChrome():
    #ruta = ChromeDriverManager(path='./chromedriver').install()
    service = Service(executable_path="./chromedriver.exe")
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=3")
    options.add_argument("--no-first-run")
    options.add_argument("--no-proxy-server")
    options.add_argument("--disable-blink-features=AutomationControlled")
    exp_opt = [
        'enable-automation',
        'enable-logging'
    ]
    options.add_experimental_option("excludeSwitches", exp_opt)

    prefs = {
        "profile.default_content_setting_values.notifications" : 2,
        "intl.accept_languages" : ["es-ES","es"],
        "credentials_enable_service":False
        }
     #para evitar que Chrome
    options.add_experimental_option("prefs", prefs)

    
    #s = Service(service)

    #driver = webdriver.Chrome(service=s, options=options)
    driver = webdriver.Chrome(service=service, options=options)

    return driver




def buscar_Info():
    print('\033[92m' + "A ver que sale..." + '\033[0m')
    try:
        bot.send_message(5760438151,"<b>jeje</b>", parse_mode="html")
        time.sleep(2)
        input = inicio.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        input.click()
        time.sleep(1)
        input.send_keys('Davo')
        time.sleep(1)
        buscar = inicio.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')
        time.sleep(2)
        buscar.click()

        time.sleep(5)
        inicio.quit()

    except:
        print('\033[96m' + "Eror en la búsqueda" + '\033[0m')
        inicio.quit()

if __name__ == '__main__':
    inicio = iniciarChrome()
    wait = WebDriverWait(inicio, 20)
    url = "https://google.com"
    inicio.get(url)
    buscar_Info()