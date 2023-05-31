def alfabeto_para_morse(mensagem):
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  # lista contendo alfabeto
    morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.',
             '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']  # alfabeto em morse

    # Converter as letras em código Morse
    letras = mensagem.upper()
    codigo_morse = []
    for letra in letras:
        if letra == ' ':
            codigo_morse.append(' ')
        else:
            for i in range(len(alfabeto)):
                if letra == alfabeto[i]:
                    codigo_morse.append(morse[i])
                    break
            else:
                codigo_morse.append(' ')

    # Retornar a mensagem em código Morse
    mensagem_morse = ' '.join(codigo_morse)
    return mensagem_morse


mensagem = input()
mensagem_morse = alfabeto_para_morse(mensagem)
print(mensagem_morse)
