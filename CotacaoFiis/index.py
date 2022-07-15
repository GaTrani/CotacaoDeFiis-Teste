from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import importacoes as imp

#VARIAVEIS
i = 0
novosAtivos = []

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
#navegador.get('https://fiis.com.br/')

link = 'https://fiis.com.br/lista-de-fundos-imobiliarios/'
navegador.get('https://fiis.com.br/lista-de-fundos-imobiliarios/')
#novosAtivos = navegador.find_element(By.XPATH, '//*[@id="items-wrapper"]/div[1]/a/span[1]')
novosAtivos = navegador.find_elements(By.CLASS_NAME, 'ticker')
listaDeAtivos = {}
print('Lista coletada com sucesso!')
pos = 0
for i in novosAtivos:
    listaDeAtivos[pos] = i.text
    #print(f'ativo {pos}:{i.text}')
    pos += 1