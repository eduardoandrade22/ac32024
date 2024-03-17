def dia_da_semana(número):
    if número == 1:
        return "DOMINGO"
    elif número == 2:
        return "SEGUNDA"
    elif número == 3:
        return "TERÇA"
    elif número == 4:
        return "QUARTA"
    elif número == 5:
        return "QUINTA"
    elif número == 6:
        return "SEXTA"
    elif número == 7:
        return "SÁBADO"
    else:
        return "Número inválido. Insira um número de 1 a 7."

entrada_válida = False
while not entrada_válida:
    entrada = input("Insira um número de 1 a 7: ")
    if entrada.isdigit():
        número = int(entrada)
        if 1 <= número <= 7:
            entrada_válida = True
        else:
            print("Número fora do intervalo permitido. Tente novamente.")
    else:
        print("Entrada inválida. Insira um número inteiro.")

resultado = dia_da_semana(número)
print("Dia da semana:", resultado)




#triangulo


def determina_tipo_triangulo(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Não é um triangulo"
    elif a == b == c:
        return "Equilatero"
    elif a == b or a == c or b == c:
        return "Isosceles"
    else:
        return "Escaleno"

# Função para ler os valores do triangulo fornecidos pelo usuário
def ler_valores_triangulo():
    a = input("insira o valor do lado a: ")
    b = input("insira o valor do lado b: ")
    c = input("insira o valor do lado c: ")
    if not (a.isdigit() and b.isdigit() and c.isdigit()):
        print("Valores inválidos. Certifique-se de inserir números.")
        return None, None, None
    return float(a), float(b), float(c)

# Teste da função
def testa_triangulo():
    a, b, c = ler_valores_triangulo()
    if a is not None and b is not None and c is not None:
        print("Tipo do triângulo:", determina_tipo_triangulo(a, b, c))

testa_triangulo()





#calculadora

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é definida"

def calculadora():
    operacao = input("Digite a operação desejada (+, -, *, /): ")
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if operacao == '+':
        resultado = soma(a, b)
    elif operacao == '-':
        resultado = subtracao(a, b)
    elif operacao == '*':
        resultado = multiplicacao(a, b)
    elif operacao == '/':
        resultado = divisao(a, b)
    else:
        resultado = "Operação inválida"

    print("Resultado:", resultado)

# Teste da função
calculadora()
