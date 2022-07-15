import importacoes as imp

def gerarListaAtivos():
    link = 'https://fiis.com.br/lista-de-fundos-imobiliarios/'
    imp.navegador.get(link)
    novosAtivos = imp.navegador.find_element(imp.By.XPATH, '//*[@id="items-wrapper"]/div[1]/a/span[1]')
    for i in novosAtivos:
        print('novos Ativos:\n', novosAtivos[i].text)