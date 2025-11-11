from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait 

import pandas as pd


entrada = input('Digite o produto que deseja pesquisar: ')

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 8)
driver.get('https://www.mercadolivre.com.br/')
driver.find_element(By.CLASS_NAME, 'nav-search-input').send_keys(entrada+Keys.ENTER)

items_ml = driver.find_elements(By.XPATH, '//li[@class="ui-search-layout__item"]')
print(f"{len(items_ml)} produtos encontrados.")

dados_ml = []

for item_ml in items_ml:
    title = item_ml.find_element(By.TAG_NAME, 'h3').text
    price = ""
    link = item_ml.find_element(By.CLASS_NAME, 'poly-component__title').get_attribute('href')
    avaliation = ""
    qtd_sellers = ""

    try:
        price = item_ml.find_element(
            By.CLASS_NAME, 
            'andes-money-amount.andes-money-amount--cents-superscript'
        ).text.replace('\n','')
    except:
        pass

    try:
        avaliation = item_ml.find_elements(
            By.CLASS_NAME,
            'poly-phrase-label'
        )
        for aval in avaliation:
            if '|' in aval.text:
                qtd_sellers = aval.text
                qtd_sellers = qtd_sellers.replace('|','').strip()
                qtd_sellers = qtd_sellers.replace(' vendidos','')
                qtd_sellers = int(qtd_sellers.replace('mil','000'))
            else:
                avaliation = aval.text
    except Exception as e:
        print(e)
        pass

    dados_ml.append({
        'title': title,
        'price': price,
        'link': link,
        'avaliation': avaliation,
        'qtd_sellers': qtd_sellers
    })

df_ml = pd.DataFrame(dados_ml)
print(dados_ml)
df_ml.to_excel(f"dados_Mercado_Livre.xlsx", index=False)
print(f"\nArquivo Excel 'dados_Mercado_Livre.xlsx' criado com sucesso!")

driver.quit()
