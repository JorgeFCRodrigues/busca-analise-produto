from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait 

import pandas as pd

entrada = input('Digite o produto que deseja pesquisar: ')

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 8)
driver.get('https://www.kabum.com.br/')
busca = wait.until(EC.visibility_of_element_located((By.ID, 'inputBusca')))
for i in entrada:
    busca.send_keys(i)
busca.send_keys(Keys.ENTER)

grid_items_kb = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'sc-5f13a78a-9.PuPCZ')))
items_kb = grid_items_kb.find_elements(By.CLASS_NAME, 'sc-27518a44-3.hLEhJe.productCard')
print(f'{len(items_kb)} produtos encontrados.')

dados_kb = []

for item_kb in items_kb:
    title = item_kb.find_element(By.TAG_NAME, 'h3').text
    price = ""
    link = item_kb.find_element(By.TAG_NAME, 'a').get_attribute('href')
    avaliation = ""

    try:
        price = item_kb.find_element(
            By.CLASS_NAME, 
            'sc-57f0fd6e-2.hjJfoh.priceCard'
        ).text.replace('\n','')
    except:
        pass

    try:
        avaliation = item_kb.find_element(
            By.CLASS_NAME,
            'text-xxs.text-black-600.leading-none.pt-4'
        ).text.replace('(', 'Avaliações: ').replace(")", "")
    except:
        pass

    dados_kb.append({
        'title': title,
        'price': price,
        'link': link,
        'avaliation': avaliation,
    })

df_kb = pd.DataFrame(dados_kb)
print(dados_kb)
df_kb.to_excel(f"dados_kabum.xlsx", index=False)
print(f"\nArquivo Excel 'dados_kabum.xlsx' criado com sucesso!")

driver.quit()