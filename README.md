# Problema: Impressão de Padrão Simétrico

Este programa é projetado para imprimir um padrão simétrico específico usando caracteres e espaços em branco conforme descrito abaixo. O padrão consiste em letras de 'A' a 'E' dispostas em linhas simétricas com uma quantidade crescente de espaços em branco entre as letras. 

## Descrição do Padrão

O padrão é composto por cinco linhas superiores seguidas de quatro linhas inferiores que repetem o padrão das primeiras quatro linhas em ordem inversa. Aqui estão as instruções para cada linha:

1. **Linha 1**: sete espaços em branco, a letra `'A'`.
2. **Linha 2**: seis espaços em branco, a letra `'B'`, um espaço em branco, a letra `'B'`.
3. **Linha 3**: cinco espaços em branco, a letra `'C'`, três espaços em branco, a letra `'C'`.
4. **Linha 4**: quatro espaços em branco, a letra `'D'`, cinco espaços em branco, a letra `'D'`.
5. **Linha 5**: três espaços em branco, a letra `'E'`, sete espaços em branco, a letra `'E'`.
6. **Linhas 6-9**: as quatro primeiras linhas em ordem inversa, criando um efeito simétrico.

## Exemplo de Saída

Ao executar o programa, ele imprime o seguinte padrão:

```
       A
      B B
     C   C
    D     D
   E       E
    D     D
     C   C
      B B
       A
```

## Solução do Código

O programa usa listas para armazenar as letras e o número de espaços antes e entre as letras. Em seguida, ele usa dois loops para construir as linhas superiores e inferiores.

### Código

```python
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
```

### Explicação do Código
1. **Listas de Caracteres e Espaços**: As listas `letras`, `espacos_iniciais`, e `espacos_meio` definem quais caracteres e quantos espaços devem ser impressos em cada linha.
2. **Primeiro Loop**: Imprime as linhas superiores do padrão com os valores das listas.
3. **Segundo Loop**: Imprime as linhas inferiores do padrão em ordem inversa, omitindo a linha do meio para manter a simetria.

## Entradas e Saídas
- **Entrada**: Não há entrada do usuário.
- **Saída**: O padrão simétrico conforme o exemplo acima.

## Complexidade
A complexidade do programa é **O(1)**, pois o número de linhas e operações é fixo.
