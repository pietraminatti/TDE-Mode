# TDE 01 Enunciado
# Juros composto a 1% ao mes durante 35 anos
# Projecao grafica do Motante apos 420 meses (uma taxa de juros de 1%am)
# Capital inicial de R$1000
# Depositos mensais de R$100
# Em Python! Com Gráfico!

import matplotlib.pyplot as plt
import numpy as np


# Função para calcular a população
def Montante(capital, tempo):
    return capital  * (1 + 1/100) ** tempo

def ValorFuturo(pmt, tempo):
    return pmt * (((1+1/100)**tempo) - 1) / (1/100)


print('Depois de 35 anos teremos', round((Montante(1000, 420) + ValorFuturo(100, 420)), 2), 'reais')


# definindo um vetor os pontos x, y do gráfico
tempo = np.arange(0, 421, 1) # foi adicionado 1 ao tempo total para que o grafico nao fique incompleto
capital = 1000


# Desenho da grade
plt.grid(color='gray', linestyle='-.', linewidth=0.5)


# Criando o gráfico
plt.plot(tempo, Montante(capital, tempo), linewidth=2.5, color='navy',
         label=r'$M = C (1 \plus i)^{n}$')


plt.legend(loc='upper left')
plt.xlabel('Tempo em meses')
plt.ylabel('Montante')


#Mostando o gráfico


plt.show()