##Projeto 18 - Análise, Identificação e Tratamento de Erro e Exceção
#Aluno: Renato Araújo
#Disciplica: Lógica de Programação
nomeCompleto=str(input("Qual seu nome completo?"))
anoNascimentoCorreto = False
while (anoNascimentoCorreto==False):
    print("Insira seu ano do seu nascimento:")
    try:
        ano = int(input())
        if (ano>=1992) and (ano<=2021):
            anoNascimentoCorreto = True
            print(nomeCompleto+" Você Completou ou Completará "+str(2022-ano)+" anos em 2022!")
        else:
            print("Você não digitou um ano válido!")
    except:
        print("Caracter inválido, por favor digite um número corresponde ao ano do seu nascimento!")
