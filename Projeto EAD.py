"""
Projeto de treino em estatística e Machine Learning simples.

Dataset: Tips (gorjetas em restaurante) disponível no seaborn.
Objetivos:
- Explorar estatisticamente os dados
- Aplicar teste qui-quadrado e t-test
- Treinar e avaliar regressão linear (gorjeta ~ conta total)
- Visualizar relações entre variáveis
"""

# ==========================================================
# 1. Importando bibliotecas
# ==========================================================
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency, ttest_ind
from sklearn.linear_model import LinearRegression

# ==========================================================
# 2. Carregando dados
# ==========================================================
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# ==========================================================
# 3. Análise descritiva
# ==========================================================
# print(df.info())
# print(df.describe())

# ==========================================================
# 4. Teste qui-quadrado (independência entre variáveis categóricas)
# ==========================================================
# tabela = pd.crosstab(df['smoker'], df['time'])
# chi2, p, dof, expected = chi2_contingency(tabela)
# print("Chi-square:", chi2)
# print("p-value:", p)
# alpha = 0.05
# if p <= alpha:
#     print("Rejeita H0: variáveis são dependentes")
# else:
#     print("Falha em rejeitar H0: variáveis são independentes")

# ==========================================================
# 5. Teste t (diferença de médias entre grupos)
# ==========================================================
# male_tips = df[df['sex'] == "Male"]["tip"]
# female_tips = df[df['sex'] == "Female"]["tip"]
# t_stat, p_value = ttest_ind(male_tips, female_tips)
# print("T-statistic:", t_stat)
# print("P-value:", p_value)
# if p_value <= alpha:
#     print("Rejeita H0: há diferença significativa")
# else:
#     print("Não rejeita H0: sem diferença significativa")

# ==========================================================
# 6. Visualizações exploratórias
# ==========================================================
# sns.histplot(df["total_bill"], kde=True)
# plt.title("Distribuição de Total Bill")
# plt.show()

# sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
# plt.title("Mapa de calor de correlações")
# plt.show()

# ==========================================================
# 7. Regressão Linear (gorjeta ~ valor da conta)
# ==========================================================
X = df['total_bill'].values.reshape(-1, 1)
y = df['tip'].values

model = LinearRegression()
model.fit(X, y)

print("Slope (coef):", model.coef_[0])
print("Intercept:", model.intercept_)
print("R²:", model.score(X, y))

# Plotando relação
sns.scatterplot(x=df['total_bill'], y=df['tip'], color="blue")
plt.plot(df['total_bill'], model.predict(X), color="red", label="Regressão Linear")
plt.title("Conta Total vs Gorjeta")
plt.legend()
plt.show()
