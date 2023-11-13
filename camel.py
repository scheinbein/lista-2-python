def separar_palavra_por_maiusculas(palavra):
    partes = []
    parte_atual = ""

    for letra in palavra:
        if letra.isupper():
            if parte_atual:
                partes.append(parte_atual)
            parte_atual = letra
        else:
            parte_atual += letra

    if parte_atual:
        partes.append(parte_atual)

    return partes

def main():
    palavra = input("Digite uma palavra com letras maiúsculas no meio: ")
    partes_separadas = separar_palavra_por_maiusculas(palavra)
    
    print("Partes separadas:")
    for parte in partes_separadas:
        print(parte)

if __name__ == "__main__":
    main()
