### Importações 

import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

### Crianção dos parâmetros do Selenium

service = webdriver.ChromeService()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = 'https://www.transparencia.se.gov.br/Pessoal/ServidoresPorOrgao.xhtml?orgao=ITPS'
driver.get(url)
wait = WebDriverWait(driver, 300)
### Seletores das combobox


'''Seletor da combobox do ANO'''
ano_inicial = 0
ano_final = 1


for i in range(ano_final, ano_inicial, -1 ):
    combobox_Ano = driver.find_elements(by=By.CLASS_NAME, value="ui-selectonemenu-label")[0]
    combobox_Ano.click()
    
    wait.until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="j_idt55:j_idt58_modal"]')))

    ano_numero = str(i)
    xpath_ano = '//*[@id="frmPrincipal:ano_'+ano_numero+'"]'
    ano = driver.find_element(by=By.XPATH, value=xpath_ano)
    ano.click()

    '''Seletor da combobox do MES'''

    mes_inicial = 9
    mes_final = 11

    for i in range(mes_inicial, mes_final):
        combobox_Mes = driver.find_elements(by=By.CLASS_NAME, value="ui-selectonemenu-label")[1]
        combobox_Mes.click()
        
        wait.until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="j_idt55:j_idt58_modal"]')))

        mes_numero = str(i)
        xpath_mes = '//*[@id="frmPrincipal:mes_'+mes_numero+'"]'
        mes = driver.find_element(by=By.XPATH, value=xpath_mes)
        mes.click()


        x = driver.find_elements(by=By.XPATH, value='//*[@id="frmPrincipal:selOrgao_panel"]/div[2]/ul/li')
        qtd_orgaos = len([k for k in x])
        qtd_orgaos
        time.sleep(1.2)


        for i in range(qtd_orgaos+1):
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
            time.sleep(1.8)