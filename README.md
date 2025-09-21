# Análise de Gorjetas em Restaurantes

# Primeiro Projeto como um ML engineer

### Visão Geral do Projeto

Este projeto de análise de dados exploratória busca entender e modelar os fatores que influenciam as gorjetas em um restaurante. Utilizando o dataset `tips` do Seaborn e ferramentas de Data Science, o objetivo é extrair insights e identificar as principais variáveis que contribuem para o valor da gorjeta.

---

### Objetivos da Análise

1.  **Exploração Estatística:** Analisar a distribuição e as estatísticas descritivas dos dados.
2.  **Testes de Hipóteses:** Aplicar testes estatísticos (`t-test` e `qui-quadrado`) para avaliar a relação entre variáveis categóricas (como gênero, fumante, dia da semana).
3.  **Modelagem Preditiva:** Utilizar a Regressão Linear para modelar a relação entre o valor da conta e a gorjeta.
4.  **Visualização de Dados:** Criar gráficos claros e informativos para comunicar os resultados.

---

### Metodologia e Ferramentas

O projeto foi desenvolvido em Python, utilizando as seguintes bibliotecas:

* **`pandas`**: Para manipulação e análise dos dados.
* **`seaborn` e `matplotlib`**: Para a criação de visualizações estatísticas.
* **`scikit-learn`**: Para a construção do modelo de Regressão Linear.
* **`scipy`**: Para a realização de testes estatísticos.

---

### Resultados e Conclusões

#### **1. Relação entre o Valor da Conta e a Gorjeta**

A análise de regressão linear revelou uma **relação positiva e linear** entre o valor da conta total e a gorjeta.


* **Coeficiente de Inclinação (Slope):** `0.105` - Isso indica que, para cada dólar a mais na conta, a gorjeta aumenta em cerca de 10 centavos.
* **Coeficiente de Determinação (R²):** `0.457` - Aproximadamente **45.7%** da variação nas gorjetas pode ser explicada pelo valor da conta, sugerindo que este é o principal fator de influência.

#### **2. Outras Análises Exploratórias**

Testes estatísticos adicionais (com o código comentado no script) foram usados para explorar outras relações:

* **Teste T de Student:** Analisou se há uma diferença significativa na gorjeta média entre homens e mulheres.
* **Teste Qui-Quadrado:** Avaliou se há uma dependência entre o hábito de fumar e o período do dia (almoço ou jantar).

---

### Como Rodar o Projeto

Para rodar este projeto, clone o repositório, instale as bibliotecas necessárias e execute o script Python.

```bash
pip install pandas numpy seaborn scikit-learn scipy matplotlib
