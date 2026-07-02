"""
Exemplo simples de KNN utilizando a base de dados Iris.

Objetivo:
Classificar uma nova flor com base nas medidas de outras flores já conhecidas.

Biblioteca utilizada:
scikit-learn
"""

# Importa a base de dados Iris
from sklearn.datasets import load_iris

# Importa o algoritmo KNN
from sklearn.neighbors import KNeighborsClassifier


# ============================================================
# PASSO 1 - Carregar a base de dados
# ============================================================

# A base Iris já vem pronta no scikit-learn.
# Ela contém 150 flores divididas em 3 espécies.

iris = load_iris()

# X representa as características (features)
# Cada linha possui:
# - Comprimento da sépala
# - Largura da sépala
# - Comprimento da pétala
# - Largura da pétala

X = iris.data

# y representa a resposta correta
# 0 = Setosa
# 1 = Versicolor
# 2 = Virginica

y = iris.target


# ============================================================
# PASSO 2 - Criar o algoritmo KNN
# ============================================================

# n_neighbors = quantidade de vizinhos analisados.
# Neste exemplo utilizaremos K = 3.

knn = KNeighborsClassifier(n_neighbors=3)


# ============================================================
# PASSO 3 - "Treinar" o algoritmo
# ============================================================

# Diferente de outros algoritmos,
# o KNN não aprende criando uma fórmula.
#
# Ele apenas guarda todos os exemplos conhecidos
# para compará-los futuramente.

knn.fit(X, y)


# ============================================================
# PASSO 4 - Criar uma nova flor
# ============================================================

# Imagine que alguém mediu uma flor e obteve:

nova_flor = [[5.1, 3.5, 1.4, 0.2]]

# Os valores representam:
#
# Comprimento da sépala = 5.1
# Largura da sépala     = 3.5
# Comprimento da pétala = 1.4
# Largura da pétala     = 0.2
#
# O computador ainda NÃO sabe qual espécie ela é.


# ============================================================
# PASSO 5 - Fazer a previsão
# ============================================================

# O algoritmo irá:
#
# 1. Calcular a distância entre a nova flor
#    e todas as flores da base.
#
# 2. Encontrar os 3 vizinhos mais próximos.
#
# 3. Fazer uma votação.
#
# 4. Retornar a espécie vencedora.

resultado = knn.predict(nova_flor)


# ============================================================
# PASSO 6 - Exibir o resultado
# ============================================================

print("Resultado da classificação:")
print(f"Código da espécie: {resultado[0]}")
print(f"Espécie: {iris.target_names[resultado[0]]}")