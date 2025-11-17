# Busca e Análise de Produtos

Uma ferramenta Python que compara preços de produtos em Mercado Livre e Kabum, calcula um score ponderado e gera relatórios em Excel com a melhor oferta.

## 🎯 Funcionalidades

- Scraping automático em dois e-commerces
- Cálculo de score ponderado considerando preço, avaliação e quantidade de reviews
- Geração de Excel com dados comparativos de ambos os sites
- Captura de screenshot do melhor produto encontrado
- Tratamento automático de dados de diferentes formatos

## 📋 Requisitos

- Python 3.7+
- ChromeDriver (compatível com sua versão do Chrome)

## 📦 Instalação

1. Clone ou baixe o projeto
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## 🚀 Como Usar

Execute o programa principal:

```bash
python main.py
```

Digite o nome do produto que deseja pesquisar quando solicitado. O programa irá:

- Buscar produtos no Mercado Livre e Kabum
- Processar e normalizar os dados
- Calcular um score para cada produto
- Gerar um arquivo Excel em `excels/`
- Capturar um print do melhor produto em `prints/`

## 📊 Estrutura do Projeto

```
.
├── main.py
├── requirements.txt
├── excels/
└── prints/
```

## 🧮 Fórmula do Score

```
score = 0.7 × preço_normalizado + 0.3 × nota_normalizada × (1 + reviews_normalizado)
```

Onde:
- **Preço normalizado**: quanto menor o preço, maior a pontuação
- **Nota normalizada**: escala de 0 a 5
- **Reviews normalizado**: quantidade de avaliações (mais confiança)

## 📝 Saída

Após a execução, você receberá:

- ✅ Arquivo Excel com 3 abas: Mercado Livre, Kabum e Comparativo
- 💰 Preço da melhor oferta exibido no terminal
- ⭐ Avaliação e quantidade de reviews
- 🖼️ Screenshot do melhor produto

## ⚠️ Notas Importantes

- O programa usa Chrome em modo headless para melhor performance
- Os dados são normalizados antes do cálculo do score
- Produtos sem preço válido são removidos da análise
- O ChromeDriver precisa estar na mesma pasta ou no PATH do sistema