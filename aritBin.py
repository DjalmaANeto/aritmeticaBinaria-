#A idéia desse programa é a seguinte, dar uma roubadinha e efetuar operações aritméticas entre binários convertendo estes para decimal e depois para binário obtendo o resultado

#função responsavel pela conversao dos binários para decimais
def binToDec(n):
    exp = len(n) - 1
    aux = 0
    
    # o loop percorrerá cada casa do nosso número binário, executando a operaçao de converção
    for x in n:
        # operação de conversão
        aux = aux + (int(x) * (2 ** exp))
        exp = exp - 1

    return aux

#precimos corrigir nosso resultado para binário novamente certo? então:

#função responsavel por converter decimais em binario
def decToBin(D):
    D = int(D)
    numberI = []    
    results = ""
    #operação de conversão
    while D >= 1:
        R = D % 2
        numberI.append(int(R))
        D = int(D)/2

    #depois das consecutivas divisões invertemos o vetor de restos (muito fácil inverter uma lista em python né?)
    numberI = numberI[::-1] 
    #tranformando a lista em string para corrigir o formato do dado    
    for x in numberI:
        results += str(x)
    
    return results

#coração da função soma
def sum(n, n1):
    return decToBin(int(binToDec(n)) + int(binToDec(n1)))
    

#coração da função subtração
def sub(n, n1):
    return decToBin(int(binToDec(n)) - int(binToDec(n1)))
    
#coração da função divisão
def div(n, n1):
    return decToBin(int(binToDec(n)) / int(binToDec(n1)))
    

#coração da função multiplicação
def mul(n, n1):
    return decToBin(int(binToDec(n)) * int(binToDec(n1)))

#função main(principal) responsavel pelo controlador da aplicação
def main():
    n = []
    n1 = []
    results = " "
    op = " "

    print("😁Be welcome to binary arithmetics!😁\n\t🥰Studie is every awesome!🥰")

    op = input("Type:\n1 --------- sum\n2 --------- subtraction\n3 --------- division\n4 --------- multiplication\n🐱‍💻: ")

    if op == "1":
        n = input("Type your first number: ")
        n1 = input("Type your second number: ")
        results = sum(n, n1)
        print(n,"+",n1,"=",results)
    elif op == "2":
        n = input("Type your first number: ")
        n1 = input("Type your second number: ")
        results = sub(n, n1)
        print(n,"-",n1,"=",results)
    elif op == "3":
        n = input("Type your first number: ")
        n1 = input("Type your second number: ")
        results = div(n, n1)
        print(n,"/",n1,"=",results)
    elif op == "4":
        n = input("Type your first number: ")
        n1 = input("Type your second number: ")
        results = mul(n, n1)
        print(n,"*",n1,"=",results)
##########################################################################
    elif op == "666":
        op = input("1 --- DEC to BIN\n2 --- BIN to DEC\n8===D")
        if op == "1":
            n = input("😚hey hot boy type a number to test: ")
            results = decToBin(n)
            print("Look😚\n",n," in bin ", results)
        elif op == "2":
            n = input("😚hey hot boy type a number to test: ")
            results = binToDec(n)
            print("Look😚\n",n," in dec ", results)
        else: 
            print("😪BAKA😪")
##########################################################################
    else:
        print("Invalid option 😪...")

    op = input('\nType 0 to leave...\nOr other character to continue...')
    if op != '0':
        main()
#startando a aplicação, chamando a função no escopo aberto (você já deve ter descoberto que isso não precisa ser feito em C, C++ ou JAVA. A SDK destas procura a função main e a executa por default)
main()
