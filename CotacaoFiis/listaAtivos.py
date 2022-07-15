import importacoes as imp

def gerarListaAtivos():
    novosAtivos = navegador.find_elements(By.CLASS_NAME, 'ticker')
    listaDeAtivos = {}
    print('Lista coletada com sucesso!')
    pos = 0
    for i in novosAtivos:
        listaDeAtivos[pos] = i.text
        print(f'ativo {pos}:{i.text}')
        pos += 1