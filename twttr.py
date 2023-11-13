txt = input('Digite sua mensagem: ').casefold()

txtsa = ''

for char in txt:
    
    if char not in ['a','e','i','o','u']:
        txtsa += char

print(txtsa)
