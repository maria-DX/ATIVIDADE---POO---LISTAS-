lista = [5, 8, 2, 10, 3]
print("Comprimento da lista:", len(lista))

soma = sum(lista)
print("Soma dos elementos da lista:", soma)


lista.sort()
print("Lista em ordem crescente:", lista)

lista.reverse()
print("Lista em ordem inversa:", lista)



lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_mesclada = lista1 + lista2
print("Lista mesclada:", lista_mesclada)



numero = int(input("Digite um número: "))
if numero in lista:
    print(f"O número {numero} está na lista.")
else:
    print(f"O número {numero} NÃO está na lista.")




