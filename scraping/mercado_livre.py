from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import pandas as pd

def buscar_mercado_livre(entrada):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome()
    driver.get('https://www.mercadolivre.com.br/')
    driver.find_element(By.CLASS_NAME, 'nav-search-input').send_keys(entrada+Keys.ENTER)

    items_ml = driver.find_elements(By.XPATH, '//li[@class="ui-search-layout__item"]')
    print(f"{len(items_ml)} produtos encontrados.")

    dados_ml = []

    for item_ml in items_ml:
        title = item_ml.find_element(By.TAG_NAME, 'h3').text
        price = ""
        link = item_ml.find_element(By.CLASS_NAME, 'poly-component__title').get_attribute('href')
        rating = ""
        reviews = ""

        try:
            price = item_ml.find_element(
                By.CLASS_NAME, 
                'andes-money-amount.andes-money-amount--cents-superscript'
            ).text.replace('\n','')
        except:
            pass

        try:
            rating = item_ml.find_elements(
                By.CLASS_NAME,
                'poly-phrase-label'
            )
            for rat in rating:
                if '|' in rat.text:
                    reviews = rat.text
                    reviews = int(reviews.replace('mil','000').replace(' vendidos','').replace('|','').strip())
                else:
                    rating = rat.text
        except Exception as e:
            print(e)
            pass

        dados_ml.append({
            'title': title,
            'price': price,
            'link': link,
            'rating': rating,
            'reviews': reviews
        })

    df_ml = pd.DataFrame(dados_ml)
    return df_ml, driver
