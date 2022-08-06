#Projeto 17 FLuxo de Entrada e Saída de Dados do Usuário
#Aluno: Renato Araújo
#Disciplica: Lógica de Programação
opSelecao=()
while opSelecao!=0:
    print('''
                1: Soma
                2: Subtração
                3: Multiplicação
                4: Divisão
                0: Sair''')
    opSelecao=int(input("Qual a operação deseja realizar?"))
    valor1=float(input("Insira o primeiro valor:"))
    valor2=float(input("Insira o segundo valor:"))
    if opSelecao==1:
        res1=valor1+valor2
        print("O resultado da soma é " + str(res1))
    elif opSelecao==2:
        res2=valor1-valor2
        print("O resultado da Subtração é " + str(res2))
    elif opSelecao==3:
        res3=valor1*valor2
        print("O resultado da multiplicação é " + str(res3))
    elif opSelecao==4:
        res4=valor1/valor2
        print("O resultado da divisão é " + str(res4))
    elif opSelecao==0:
        print("Finalizando aplicação...")
    else:
        print("Essa Opção não existe")
    print("Saindo da Calculadora")