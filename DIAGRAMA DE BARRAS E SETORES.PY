

import pandas as pd
import matplotlib.pyplot as plt

# Dados (mantidos do exemplo anterior)
dados = pd.Series ([5, 6, 7, 2, 3, 9, 10, 8, 6, 9])

#Gráfico de Pizza


contagem_valores = dados.value_counts()
plt.figure(figsize=(8, 6)) 
plt.pie(contagem_valores, labels=contagem_valores.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribuição de Frequencia dos Dados')
plt.axis('equal')
plt.show()


#---------------------------------------------------

#Gráfico de Barras

plt.figure(figsize=(8, 6))
plt.bar(contagem_valores.index, contagem_valores.values)
plt.xlabel('Valores')
plt.ylabel('Frequencia')
plt.title('Frequência de cada valor')
plt.show()

#Criar o boxplot

plt.figure(figsize=(8, 6))
plt.boxplot(dados, vert=False)
plt.title('Boxplot dos dados')
plt.xlabel('Valores')
plt.show()

#Base de dados simulada: tempo de deslocamento ao trabalho (minutos)

tempo_deslocamento = pd.Series([
    10, 12, 15, 13, 14, 16, 20, 22, 25, 30,
    35, 36, 38, 40, 42, 43, 45, 50, 55, 60, 
    65, 70, 75, 80, 90, 100, 120, 150, 180, 200
])

#Geração do boxplot

plt.figure(figsize=(10, 6))
plt.boxplot(tempo_deslocamento, vert=False, patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='blue'),
            medianprops=dict(color='red'),
            whiskerprops=dict(color='black'),
            capprops=dict(color='black'),
            flierprops=dict(marker='o', markerfacecolor='orange', markersize=8))

plt.title("Tempo de deslocamento até o Trabalho (minutos)")
plt.xlabel("minutos")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

