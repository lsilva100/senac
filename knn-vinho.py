"""
Exemplo de KNN utilizando a base Wine.

Objetivo:
Classificar o tipo de um vinho com base em suas características químicas.

Bibliotecas utilizadas:
- scikit-learn

Instalação:
pip install scikit-learn
"""

# ============================================================
# IMPORTAÇÃO DAS BIBLIOTECAS
# ============================================================

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# ============================================================
# PASSO 1 - CARREGAR A BASE DE DADOS
# ============================================================

# A base Wine possui 178 amostras de vinhos.
# Existem 3 tipos diferentes de vinho.

wine = load_wine()

# Características dos vinhos
X = wine.data

# Classe de cada vinho
y = wine.target

print("Tipos de vinho:")
print(wine.target_names)

print("\nQuantidade de características:", len(wine.feature_names))
print("Características analisadas:")

for caracteristica in wine.feature_names:
    print("-", caracteristica)

# ============================================================
# PASSO 2 - DIVIDIR OS DADOS
# ============================================================

# Vamos separar:
# 80% para treinamento
# 20% para teste

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ============================================================
# PASSO 3 - CRIAR O KNN
# ============================================================

# O algoritmo irá consultar os 5 vizinhos mais próximos.

knn = KNeighborsClassifier(n_neighbors=5)

# ============================================================
# PASSO 4 - TREINAR
# ============================================================

# O KNN apenas armazena os exemplos de treinamento.

knn.fit(X_treino, y_treino)

# ============================================================
# PASSO 5 - TESTAR O MODELO
# ============================================================

# Agora o algoritmo tentará adivinhar
# o tipo dos vinhos que ele nunca viu.

previsoes = knn.predict(X_teste)

# ============================================================
# PASSO 6 - CALCULAR A PRECISÃO
# ============================================================

acuracia = accuracy_score(y_teste, previsoes)

print("\nPrecisão do modelo:")
print(f"{acuracia * 100:.2f}%")

# ============================================================
# PASSO 7 - CLASSIFICAR UM NOVO VINHO
# ============================================================

novo_vinho = [[
    13.2,   # álcool
    2.77,   # ácido málico
    2.51,   # cinzas
    18.5,   # alcalinidade
    96,     # magnésio
    2.87,   # fenóis
    2.45,   # flavonoides
    0.40,   # fenóis não flavonoides
    1.35,   # proantocianinas
    2.80,   # intensidade da cor
    1.28,   # tonalidade
    3.40,   # OD280
    1050    # prolina
]]

resultado = knn.predict(novo_vinho)

print("\nNovo vinho classificado como:")
print(wine.target_names[resultado[0]])