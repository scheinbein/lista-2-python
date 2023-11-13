
def main ():
    precococa = 50
    totalinserido = 0

    while totalinserido < precococa:
        moeda = int(input('Insira uma moeda de 5, 10 ou 25 (centavos): '))
        
        if moeda not in [5,10,25]:
            print('Moeda não aceita. Tente outra: ')
        else:
            totalinserido += moeda
            valordevido = precococa - totalinserido

            if valordevido > 0:
                print(f'O valor devido é {valordevido}')

    if totalinserido >= precococa:
        troco = totalinserido - precococa
        print(f'Valor suficiente. Troco de {troco} centavos.')

if __name__ == '__main__':
    main()
