# Definimos as letras e o número de espaços iniciais correspondentes
letras = ['A', 'B', 'C', 'D', 'E']
espacos_iniciais = [7, 6, 5, 4, 3]
espacos_meio = [0, 1, 3, 5, 7]

# Impressão das linhas de cima
for i in range(5):
    print(' ' * espacos_iniciais[i] + letras[i] + ' ' * espacos_meio[i] + (letras[i] if espacos_meio[i] > 0 else ''))

# Impressão das linhas de baixo (em ordem reversa, sem repetir a linha do meio)
for i in range(3, -1, -1):
    print(' ' * espacos_iniciais[i] + letras[i] + ' ' * espacos_meio[i] + (letras[i] if espacos_meio[i] > 0 else ''))
