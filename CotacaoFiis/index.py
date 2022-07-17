from datetime import datetime
from time import sleep, time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import importacoes as imp
from selenium.webdriver.chrome.options import Options
import sqlite3
import BD
import listaAtivos

#EVITAR ERROS/PARADAS NO CODIGO
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#VARIAVEIS
novosAtivos = []
num = 0

#INICIALIZACAO DO DRIVER/NAVEGADOR
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
link = 'https://fiis.com.br/lista-de-fundos-imobiliarios/'
navegador.get(link)
print('Site acessado com SUCESSO!')

#-------------------------------------------------------------------------------------------

novosAtivos = navegador.find_elements(By.CLASS_NAME, 'ticker')
listaDeAtivos = {}
print('Lista coletada com SUCESSO!')

pos = 0
for i in novosAtivos:
    listaDeAtivos[pos] = i.text
    #print(f'ativo {pos}:{i.text}')
    pos += 1
print('lista convertida com SUCESSO!')

#-------------------------------------------------------------------------------------------

#CRIAR DATABASE
database = sqlite3.connect('BancoDadosFii.db')
c = database.cursor()

BD.criarTabela()

#-------------------------------------------------------------------------------------------

cont = 0
for i in listaDeAtivos.values():
    print(f'ativo {cont}:{i}')
    cont += 1
print('-----------------------------')

#-------------------------------------------------------------------------------------------

for i in listaAtivos.ativos2:
    try: 
        sleep(2)
        link = 'https://fiis.com.br/' + i + '/'
        print('Acessando:', link)
        navegador.get(link)     #alguns links o codigo quebra e nao acessa, é aleatorio! 
        print(num, i)

        #DADOS A COLETAR
        valorAtivo = navegador.find_element(By.XPATH, '//*[@id="quotations--infos-wrapper"]/div[1]/span[2]')
        #dividendYield = imp.navegador.find_element(By.XPATH, '//*[@id="informations--indexes"]/td[1]')

        dividendYield = navegador.find_element(By.XPATH, '//*[@id="informations--indexes"]/td[1]/h3[1]').text

        print('dividend Yield:', dividendYield)

        if dividendYield == '0,00%':
            print("PROXIMO POIS -------------------------------o dividendo é > 0,00")
        if valorAtivo.text != '0,00' or dividendYield != '0,00%':
            ticker = navegador.find_element(By.XPATH, '//*[@id="fund-ticker"]')
            menu = navegador.find_element(By.XPATH, '//*[@id="last-revenues--table"]/thead/tr')
            dados = navegador.find_element(By.XPATH, '//*[@id="last-revenues--table"]/tbody')
            tickertext = ticker.text
            menu = menu.text
            dadostext = dados.text
            dadosdiv = dadostext.split()
            linhas = int(len(dadosdiv) / 7)

            print('dados:')
            '''print(dadostext)'''
            
            cont = 0

            for l in range(0, linhas):

                for c in range(0, 1):
                    BD.inserirat(tickertext, dadosdiv[cont + 0], dadosdiv[cont + 1],
                                            dadosdiv[cont + 3], dadosdiv[cont + 4], dadosdiv[cont + 6])
                    database.commit()
                    cont += 7
            num += 1
            print("---------------------------------- OK")
            
        else:
            print('- Ativo nao existe!')
    except Exception as erro:
        print('\n*******ERRO inesperado!*********') 
        print('Erro = ', erro)
        print('**********************************')
        sleep(2)     
        navegador.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 'w')
        print('navegador fechado.')
        
        

navegador.close()
print('SUCESSO!')