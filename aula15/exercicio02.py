# Crie uma função chamada estatisticas_numericas que recebe uma lista de números 
# e retorna um dicionário contendo a média, o maior valor, o menor valor e a mediana dos números.
# A função deve garantir que a lista não esteja vazia e que todos os elementos sejam numéricos.

def estatisticas_numericas(lista):
    if(not lista):
      return 'A lista está vazia'
    
    if(not all(isinstance(numero, (int, float)) for numero in lista) ):
        return 'Nem todos os valores são numéricos'  
    
    soma = sum(lista)
    media = soma / len(lista)

    maior = max(lista)

    menor = min(lista)

    lista_ordenada = sorted(lista)
    tamanho = len(lista_ordenada)

    if(tamanho % 2 == 0):
       mediana = (lista_ordenada[tamanho // 2 - 1] + lista_ordenada[tamanho // 2]) / 2
    else:
       mediana = lista_ordenada[tamanho // 2]

    return {
       'Média': media,
       'Maior': maior,
       'Menor': menor,
       'Mediana': mediana
    }


print(estatisticas_numericas([30, 10, 20, 40]))