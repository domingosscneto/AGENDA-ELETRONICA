3import sys
agenda = []
print("""Escolha o que deseja fazer na sua agenda:
1)Inserir nome na lista
2)buscar nome na lista
3)remover nome da lista
4)Ordenar a lista em ordem crescente
5)Ordenar a lista em ordem decrescente
6)Sair do programa""")
def insert():
    inserir = input("Digite o nome que deseja inserir na agenda: ")
    agenda.append(inserir)
def search():
    busca = input("Digite o nome que deseja buscar na agenda: ")
    if busca in agenda:
        print("O nome existe na agenda")
    else:
        print("O nome não existe na lista")
def remove():
    remover = input("Digite o nome que deseja remover da agenda: ")
    agenda.remove(remover)
    print("Nome removido")
def growing():
    agenda.sort()
    print(agenda)
def decreasing():
    agenda.sort(reverse=True)
    print(agenda)
def menu():
    op = int(input("O que deseja fazer: "))
    while op<1 or op>6:
        op = int(input("O que deseja fazer: "))
    return op
def main():
    op = menu()
    while op!=6:
        if op==1:
            insert()
        if op==2:
            search()
        if op==3:
            remove()
        if op==4:
            growing()
        if op==5:
            decreasing()
        op = menu()
    sys.exit("EXIT")
main()
