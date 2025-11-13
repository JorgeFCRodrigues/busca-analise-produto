import numpy as np
import pandas as pd

def calcular_score(df):
     
    """
    Calcula o score ponderado de cada produto com base em:
    - preço (quanto menor, melhor)
    - avaliação (nota de 0 a 5)
    - quantidade de reviews (mais avaliações = mais confiança)
    """
     
    # Garante que as colunas necessárias existam
    colunas_necessarias = {'price', 'rating', 'reviews'}
    if not colunas_necessarias.issubset(df.columns):
        raise ValueError(f"O DataFrame precisa conter as colunas: {colunas_necessarias}")
    
    # Conversão para numpy arrays
    preco = np.array(df['price'], dtype=float)
    nota = np.array(df['rating'], dtype=float)
    reviews = np.array(df['reviews'], dtype=float)

    # --- Normalizações (0 a 1) ---
    # Evita divisões por zero com +1e-9
    preco_norm = 1 / (preco +1e-9)
    preco_norm = preco_norm / np.nanmax(preco_norm)

    nota_norm = nota / 5
    reviews_norm = reviews / (np.nanmax(reviews) if np.nanmax(reviews) > 0 else 1)

    # --- Cálculo do Score ---
    # 70% preço baixo + 30% boa avaliação ponderada por reviews
    score = (0.7 * preco_norm) + (0.3 * nota_norm * (1 + reviews_norm))

    score = score / np.nanmax(score)

    # Retorna o DataFrame com a coluna de score
    df = df.copy()
    df['score'] = score

    return df
