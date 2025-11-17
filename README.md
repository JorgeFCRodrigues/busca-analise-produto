# 📦 Busca e Análise de Produto  
### *Automação de cotação, comparação de preços e geração de relatórios com Python + Selenium*

Este projeto automatiza a busca de produtos em diferentes e-commerces, coleta preços, avaliações, quantidade de reviews, calcula automaticamente qual é a melhor oferta e gera relatórios completos em Excel.  
Além disso, o sistema tira **prints automáticos** (screenshots) da página do produto vencedor.

Ideal para setores de **compras**, **estoque**, **reposições** ou qualquer processo que precise comparar rapidamente preços na internet.

---

## ✨ Funcionalidades

- 🔍 Busca automática do produto informado  
- 🛒 Scraping em:
  - Mercado Livre  
  - Kabum  
- 📊 Cálculo de Score com NumPy (preço + avaliação + reviews)  
- 📁 Geração de Excel com abas:
  - Mercado Livre  
  - Kabum  
  - Comparativo  
- 🖼️ Print automático da página do produto vencedor  
- 🧹 Tratamento e normalização dos dados  
- 🧩 Arquitetura modular

---

## 📁 Estrutura do Projeto

```
busca-analise-produto/
│
├── main.py
│
├── scraping/
│   ├── mercado_livre.py
│   └── kabum.py
│
├── utils/
│   └── score_calculator.py
│
├── outputs/
│   ├── prints/
│   └── excels/
│
├── requirements.txt
└── README.md
```

---

## 🚀 Como Executar

### 1️⃣ Clone o repositório  
```
git clone https://github.com/JorgeFCRodrigues/busca-analise-produto.git
cd busca-analise-produto
```

### 2️⃣ Crie o ambiente virtual  
```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Instale as dependências  
```
pip install -r requirements.txt
```

### 4️⃣ Execute  
```
python main.py
```

Digite o produto quando solicitado.

---

## 📊 Sobre o Score

O score é calculado considerando:

| Fator     | Peso |
|-----------|------|
| Preço     | 70%  |
| Avaliação | 30%  |
| Reviews   | Aumentam a confiança |

Os valores são normalizados com NumPy para precisão e eficiência.

---

## 📁 Saídas Geradas

📄 Excel em `outputs/excels/`  
🖼️ Screenshot em `outputs/prints/`  

---

## 🧠 Tecnologias
- Python  
- Selenium  
- Pandas  
- NumPy  
- OpenPyXL  

---

## 🤝 Contribuição

1. Fork  
2. Branch  
3. Commit  
4. Push  
5. Pull Request 🚀  

---

## 📄 Licença
MIT License

---

## 👨‍💻 Autor
**Jorge Fernando C. Rodrigues**
