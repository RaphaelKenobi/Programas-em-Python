####### Raphael Pereira da Silva Piloneto########
############# 12221ECP001########################
######### 08-tradutor-codigo-morse###############


def morse_conveter_codigo(codigo_morse):
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']  # lista contendo alfabeto
    morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
             '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']  # alfabeto em morse

    # Converter o código Morse em letras
    erro = []  # lista para receber os erros
    for i in range(len(alfabeto)):
        codigo_separado = [alfabeto[i], morse[i]]
        erro.append(codigo_separado)

    letras = []  # letras para formar as frases

    for i in codigo_morse:  # reparar o erro
        if i == '':
            letras.append(' ')
        elif '*' in i:  # se houver * na frase vai substituir por espaço vazio
            codigo_corrompido = i.replace('*', '')
            bug = []
            for j in erro:
                # faz a comparação de .- em toda lista
                if j[1].startswith(codigo_corrompido):
                    bug.append(j[0])
            bug.sort()  # organizar em ordem alfabetica
            letras.append('[' + ''.join(bug) + ']')
        else:
            for k in erro:
                if i == k[1]:
                    letras.append(k[0])

    espaço = ''
    for espaços in letras:
        if espaços != ' ':
            espaço += espaços
        else:
            espaço += ' '
    return espaço


def main():
    codigo_morse = input().split(' ')  # recebe o código do usuario
    resultado = morse_conveter_codigo(
        codigo_morse)  # Correção do nome da função
    print(resultado)


main()
