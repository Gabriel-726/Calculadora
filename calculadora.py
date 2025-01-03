#Variavel que irá servir como loop de execução de aplicativo
run = True

#Operações

def soma(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2 

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

#Dicionário com operações

operacoes = {
'+': soma,
'-': sub,
'*': mult,
'/': div
}

#calculo
def calculadora(n1, n2, op):
    if op in operacoes:
        resultado = operacoes[op](In1, In2)
        print(f"{n1} {op} {n2} = {resultado}")

    resultadoAnt = resultado

    p = input(f"Deseja realizar outra operação com {resultado}?")
        
    while p == "s":
        
        for sinal in operacoes:
            print(sinal)
        
        op = input("Escolha uma operação acima: ")
    
        n2 = input("Informe o segundo número: ")
        Inn2 = float(n2)
        
        if op in operacoes:
            resultado = operacoes[op](resultadoAnt, Inn2)
        
       
            
        print(f"{resultadoAnt} {op} {n2} = {resultado}")

        resultadoAnt = resultado    

        p = input(f"Deseja realizar outra operação com {resultado}?")
       

#Função que recolhe os dados que serão utilizados na função "calculadora"
def start():
    n1 = input("Informe o primeiro número: ")
    In1= float(n1)

    for sinal in operacoes:
        print(sinal)
    op = input("Escolha uma operação acima: ")

    n2 = input("Informe o segundo número: ")
    In2 = float(n2)
    
    return In1, op, In2

while run == True:
    In1, op, In2 = start()

    calculadora(n1 = In1, n2 = In2, op = op)

    print("\033[H\033[J", end="")






