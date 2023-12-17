def is_prime(number):
    #Verifica se um número é primo.
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
    #Encontra os primeiros numeros primos 
def first_numbers(n):
    prime = []
    number = 2
    while len(prime) < n:
        if is_prime(number):
            prime.append(number)
        number += 1
    return prime
    #Organiza os números primos em uma matriz de 10 colunas.
def matrix_numbers(prime):
    matrix = []
    for i in range(0, len(prime), 10):
        matrix.append(prime[i:i+10])
    return matrix

#Encontrar os 100 primeiros números primos
prime_one = 100
first_hundred = first_numbers(prime_one)

#Criar a matriz
matrix_of_numbers = matrix_numbers(first_hundred)

#Imprimir a matriz
for line in matrix_of_numbers:
    print(line)
