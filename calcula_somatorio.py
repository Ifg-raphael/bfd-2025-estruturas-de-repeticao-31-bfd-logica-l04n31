# lê n do usuário
n = int(input("Digite um número inteiro n: "))
soma = 0 # acumula o somatório

# só calcula se n for pelo menos 2
if n >= 2:
    for i in range(2, n + 1): # percorre valores de 2 até n
        soma += 1 / (i - 1) # adiciona o termo 1/(i-1)
# exibe resultado
print(f"{soma:.2f}")
