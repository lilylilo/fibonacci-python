# Função para verificar se um número pertence à sequência de Fibonacci
def verifica_fibonacci(num):
    # Inicializando os primeiros números da sequência
    a, b = 0, 1

    # Continuar a gerar números de Fibonacci até ultrapassar o número dado
    while a <= num:
        if a == num:
            return True  # O número pertence à sequência
        a, b = b, a + b  # Atualiza os dois números anteriores na sequência

    return False  # O número não pertence à sequência


# Entrada do número que será verificado
numero = int(input("Informe um número: "))

# Chama a função e exibe a mensagem apropriada
if verifica_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
