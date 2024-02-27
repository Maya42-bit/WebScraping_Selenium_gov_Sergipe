### Importações bibliotecas
import pandas as pd
from tqdm import tqdm
import time

from funcs.uniao_arquivos import unir_arquivos
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Importa Func
from funcs.uniao_arquivos import unir_arquivos

### Crianção dos parâmetros do Selenium

service = webdriver.ChromeService()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = 'https://www.transparencia.se.gov.br/Pessoal/ServidoresPorOrgao.xhtml?orgao=ITPS'
driver.get(url)
wait = WebDriverWait(driver, 900)


### Seletores das combobox
print("Fazendo Web Scraping em https://www.transparencia.se.gov.br\n")
ano = input("Ano da busca: ")
mes = input("Mês de Busca (Janeiro, Fevereiro ...): ")

dinovu = ''
repete =0

while repete == 0:

    #Selecionando o Ano

    combobox_Ano = driver.find_element(by=By.XPATH, value='//*[@id="frmPrincipal:ano_input"]')
    select_ano = Select(combobox_Ano)
    select_ano.select_by_visible_text(str(ano))

    #selecionando o Mês 

    combobox_Mes = driver.find_element(by=By.XPATH, value='//*[@id="frmPrincipal:mes_input"]')
    select_mes = Select(combobox_Mes)
    select_mes.select_by_visible_text(mes)


    #selecionando o Ano
    x = driver.find_elements(by=By.XPATH, value='//*[@id="frmPrincipal:selOrgao_panel"]/div[2]/ul/li')
    qtd_orgaos = len([k for k in x])
    time.sleep(1.2)

        #Interando sob os Orgãos
    for i in tqdm(range(qtd_orgaos+1), desc="Senta e Mofa :v"):
        
        combobox_Orgao = driver.find_elements(by=By.CLASS_NAME, value="ui-selectonemenu-label")[2]
        combobox_Orgao.click()
        time.sleep(1)

        orgao_numero = str(i)
        xpath_orgao = '//*[@id="frmPrincipal:selOrgao_'+orgao_numero+'"]'
        orgao = driver.find_element(by=By.XPATH, value = xpath_orgao)
        orgao.click()
        
        ### Botão de Download

        pesquisa_button = driver.find_element(by=By.XPATH, value='//*[@id="frmPrincipal:botaoPesquisar"]')
        pesquisa_button.click()
                    
        wait.until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="j_idt55:j_idt58_modal"]')))

        pesquisa_button = driver.find_element(by=By.XPATH, value='//*[@id="frmPrincipal:j_idt182"]')
        pesquisa_button.click()
        time.sleep(1)

    dinovu = input("fazer o processo para outro Ano ou Mês (y/n)?: ")
    if dinovu=="n":
        break

if dinovu == "n":
    resp = input("Deseja unir os arquivos (y/n)?")
    
    diretorio = input("Diretório dos arquivos baixados (com 2x \): ")
    nome_arquivo_destino = input("Nome do arquivo de destino: ")
    sep_destino = input("Separador do arquivo de destino: ")
        
    #União de arquivos no diretório

    uniao = unir_arquivos(diretorio_arq=diretorio, sep_arq=',' ,nome_destino=nome_arquivo_destino, sep_destino= sep_destino)
    print(f"salvo em {uniao}")