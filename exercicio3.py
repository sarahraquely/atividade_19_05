def fatorial(numero):
    resultado = 1
    for i in range (2, numero+1):
        resultado *= i
    return resultado
print(fatorial(5))
