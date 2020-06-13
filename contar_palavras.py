import string

entrada = input().split()

num_palavras = 0

for palavra in entrada:

    for letra in palavra:
        if letra in string.ascii_letters:
            num_palavras += 1
            break
    
print(num_palavras)

