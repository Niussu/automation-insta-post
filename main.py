from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--incognito")

servico = Service(ChromeDriverManager().install())

nav = webdriver.Chrome(service=servico, options=chrome_options)

nav.get('https://www.instagram.com/')

sleep(5)

#Login no insta

login = input("Digite o seu email ou número de telefone: ")
senha = input("Digite sua senha para acessar o instagran:")

nav.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(login)
nav.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha)

nav.find_element('xpath', '//*[@id="loginForm"]/div/div[3]').click()

#Verificação de dois fatores

codigo_validacao = input("Digite o código que chegou: ")

nav.find_element('xpath', '//*[@id="mount_0_0_4/"]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[1]/div/label/input').send_keys(codigo_validacao)

nav.find_element('xpath', '//*[@id="mount_0_0_4/"]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[2]/button').click()

sleep(30)