# TDE 01 Enunciado
# Sabendo que a bactéria B se reproduz a cada 2 minutos, criando uma nova bactéria.
# Quantas bactérias existirão em uma colônia depois de 14 minutos?
# Sabe-se que inicialmente havia apenas 10 bactérias nesta colônia
# Sabe-se que apenas 80% das bacterias iniciais sobrevivem
# Em Python! Com Gráfico!

import matplotlib.pyplot as plt
import numpy as np


# Função para calcular a população
def Populacao(bacteriasIniciais, tempo):
    return bacteriasIniciais * 1.8 ** (tempo / 2)

print('Depois de 14 minutos teremos', int(Populacao(10, 14)), 'bactérias')


# definindo um vetor os pontos x, y do gráfico
tempo = np.arange(0, 15, 1) # foi adicionado 1 ao tempo total para que o grafico nao fique incompleto
bacteriasIniciais = 10


# Desenho da grade
plt.grid(color='gray', linestyle='-.', linewidth=0.5)


# Criando o gráfico
plt.plot(tempo, Populacao(bacteriasIniciais, tempo), linewidth=2.5, color='navy',
         label=r'$População = bactéria \times 1.8^{(\frac{tempo}{2})}$')

plt.legend(loc='upper left')
plt.xlabel('Tempo')
plt.ylabel('População')

# Mostando o gráfico
plt.show()