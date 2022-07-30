#Projeto Função
#Aluno: Renato Araújo
#Disciplica: Lógica de Programação
def calculadoraDeDoisNumeros(numero1,numero2,entradaDaOperacao):
    if entradaDaOperacao==1:
        return numero1+numero2
    elif entradaDaOperacao==2:
        return numero1-numero2
    elif entradaDaOperacao==3:
        return numero1*numero2
    elif entradaDaOperacao==4:
        return numero1/numero2
    else:
        return 0

print('1 Soma, 2 Subtração, 3 Divisão ou 4 Multiplicação')
numero1=int(input("Escolha o primeiro número inteiro:"))
numero2=int(input("Escolha o segundo número inteiro:"))
entradaDaOperacao=int(input("Qual operação deseja realizar?"))
print(calculadoraDeDoisNumeros(numero1,numero2,entradaDaOperacao))

