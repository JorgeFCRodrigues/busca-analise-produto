import pandas as pd
import time
from scraping.kabum import buscar_kabum
from scraping.mercado_livre import buscar_mercado_livre
from utils.calculo_score import calcular_score
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

entrada = input('Digite o produto que deseja pesquisar: ')

# Busca nos dois sites
df_kb = buscar_kabum(entrada)
df_ml, driver_ml = buscar_mercado_livre(entrada)

# Identificação da origem
df_kb['origem'] = 'Kabum'
df_ml['origem'] = 'Mercado Livre'

# União dos dados
df_total = pd.concat([df_ml, df_kb], ignore_index=True)

# --- Tratamento dos dados ---
def tratar_preco(valor):
    """Limpa e converte valores de preço para float"""
    try:
        if isinstance(valor, (list, tuple)):  # se for lista, pega o primeiro
            valor = valor[0]
        valor = str(valor).replace('R$', '').replace('.', '').replace(',', '.').strip()
        return float(valor)
    except:
        return None

def tratar_numero(valor):
    """Converte número de avaliações para int"""
    try:
        if isinstance(valor, (list, tuple)):
            valor = valor[0]
        valor = str(valor).replace('+', '').replace('.', '').replace(',', '').strip()
        return int(valor)
    except:
        return 0

def tratar_rating(valor):
    """Converte nota de avaliação (ex: '4,8') para float"""
    try:
        if isinstance(valor, (list, tuple)):
            valor = valor[0]
        valor = str(valor).replace(',', '.').strip()
        return float(valor)
    except:
        return 0.0

# Aplica as funções
df_total['price'] = df_total['price'].apply(tratar_preco)
df_total['rating'] = df_total['rating'].apply(tratar_rating)
df_total['reviews'] = df_total['reviews'].apply(tratar_numero)

# Remove linhas sem preço válido
df_total = df_total.dropna(subset=['price'])

# --- Recalcula o score (agora com dados limpos) ---
df_total = calcular_score(df_total)

# Melhor oferta
melhor_oferta = df_total.loc[df_total['score'].idxmax()]

# Criação da aba comparativa
df_comparativo = df_total.sort_values('score', ascending=False)[
    ['title', 'price', 'rating', 'reviews', 'origem', 'link']
].reset_index(drop=True)

# --- Criação do Excel ---
arquivo_excel = f'outputs/excels/tabela_precos_{entrada}.xlsx'
with pd.ExcelWriter(arquivo_excel) as writer:
    df_ml.to_excel(writer, sheet_name='Mercado Livre', index=False)
    df_kb.to_excel(writer, sheet_name='Kabum', index=False)
    df_comparativo.to_excel(writer, sheet_name='Comparativo', index=False)

print(f"✅ Arquivo '{arquivo_excel}' criado com sucesso!")
print(f"💰 Melhor oferta: {melhor_oferta['origem']} - R${melhor_oferta['price']:.2f}")
print(f"⭐ Avaliação: {melhor_oferta['rating']} ({melhor_oferta['reviews']} avaliações)")
print(f"🔗 Produto: {melhor_oferta['title']}")

# --- Print do melhor produto ---
try:
    if melhor_oferta['origem'] == 'Mercado Livre':
        print("🟡 Gerando print do produto no Mercado Livre...")
        driver_ml.get(melhor_oferta['link'])
        time.sleep(3)

        scroll_height = driver_ml.execute_script("return document.body.scrollHeight")
        driver_ml.set_window_size(1920, scroll_height)
        time.sleep(1)

        driver_ml.save_screenshot(f'outputs/prints/print_{entrada}.png')
        driver_ml.quit()
    else:
        print("🔵 Gerando print do produto na Kabum...")
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")

        scroll_height = driver_ml.execute_script("return document.body.scrollHeight")
        driver_ml.set_window_size(1920, scroll_height)
        time.sleep(1)
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(melhor_oferta['link'])
        time.sleep(3)
        driver_ml.save_screenshot(f'outputs/prints/print_{entrada}.png')
        driver.quit()

    print(f"🖼️ Print salvo como 'print_{entrada}.png'")
except Exception as e:
    print(f"⚠️ Erro ao gerar print: {e}")