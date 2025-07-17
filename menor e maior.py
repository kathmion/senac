print("=== comparar dois numeros ==")
# ler dois numeros na tela 
a = int(input("Digite um numero:" ))
b = int(input("Digite outro numero:" ))
#comparar os dois numeros
if(a == b):
    print("numeros iguais!")
else:
    print("numeros diferentes!")
#mostrar o numero maior 
if(a > b):
    print("o maior é a = ",a)
else:
    print("o maior é b = ",b)
#mostrar o numero menor
if (a < b):
    print("o menor numero é a = ",a)
else:
    print("o menor é b = ",b)