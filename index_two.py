def bisseccao(number, tolerancia=1e-5):
    # Verifica se o número é negativo
    if number < 0:
        raise ValueError("A raiz quadrada de um número negativo é indefinida.")
    
    # Inicializa as variáveis para o loop da bisseccao
    a, b = 0, max(1, number) 

    # Executa o método da bisseccao até atingir a tolerância desejada
    while b - a > tolerancia:
        meio = (a + b) / 2  
        quadrado_meio = meio * meio 

        if quadrado_meio < number:
            a = meio
        else:
            b = meio
            
    # Calcula a raiz quadrada e arredonda para a quinta casa decimal
    value = round((a + b) / 2, 5)  
    return value

# Exemplo de uso
number = float(input("Digite um número para encontrar a raiz quadrada: "))
root = bisseccao(number)
print(f"A raiz quadrada de {number} é aproximadamente {root}")
