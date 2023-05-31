def vogal(caractere):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if caractere in vogais:
        return True
    else:
        return False


x = input()
if vogal(x):
    print(True)
else:
    print(False)
