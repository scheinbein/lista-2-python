def main():
    while True:
        try:
            fracao = input('Insira uma fração no formato X/Y: ')
            x, y = map(int, fracao.split('/'))

            if y <= 0 or x < 0:
                raise ValueError("X tem que ser maior ou igual a zero e Y tem que ser maior que zero.")
            
            result = 100 * x / y

            
            if result >= 99:
                print('F')  
            elif result <= 1:
                print('E') 
            else:
                print(f'{round(result)}%')  

            break 
        except (ValueError, ZeroDivisionError):
            print("Entrada inválida. Tente novamente.")

if __name__ == "__main__":
    main()
