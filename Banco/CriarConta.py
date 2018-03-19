from time import sleep
import os
#Pegar as imformações no arquivo
acc_passw = open('Data/acc_passw.txt', 'r')
dados = acc_passw.readline()
dados = eval(dados)
saldo = num_acc = num_pass = 0
acc_passw.close()

def main():
    while True:
        val = str(input("Você quer criar uma nova conta?(S/N) ")).strip().upper()[0]
        if val == "S":
            CriarAcc()
            Deposito()
        else:
            break

def CriarAcc():
    global saldo, num_pass, num_acc
    num_acc = int(input("\nDigite o número da conta: ")) 
    
    while num_acc in dados or len(str(num_acc)) > 6 or len(str(num_acc)) < 6: #Validação do número de conta
        print("Número da conta já está em uso, e só é permitido números de 6 digitos.")
        num_acc = int(input("Digite o número da conta: "))

    num_pass = int(input("Digite uma senha: "))
    
    while len(str(num_pass)) > 4 or len(str(num_pass)) < 4: #Permitir somente senhas com 4 digitos
        print("Só é permitido senha com 4 digitos, digite outro.")
        num_pass = int(input("Digite uma senha: "))

    #Escrever dados no arquivo
    #acc_passw = open('Data/acc_passw.txt','w')
    #dados[num_acc] = [num_pass, volordep]
    #acc_passw.write(str(dados))
    #acc_passw.close()

def Deposito():
    global saldo, num_pass, num_acc
    print("\nPara a conta ser criada, faça seu primeiro depósito.\n")
    volordep = float(input("Valor do primeiro depósito: "))
    
    while volordep < 30: #Deposito minimo de 30 reais
        print("O valor de deposito minimo é R$30,00.")
        volordep = float(input("Valor do primeiro depósito: "))
    saldo += volordep
    
    acc_passw = open('Data/acc_passw.txt','w')
    dados[num_acc] = [num_pass, saldo]
    acc_passw.write(str(dados))
    acc_passw.close()
    sleep(2)
    
    print("\nConta Criada e Deposito feito!\n")
    sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')

main()
