def morse_para_alfabeto(codigo_morse):
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  # lista contendo alfabeto
    morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.',
             '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']  # alfabeto em morse

    # Converter o código Morse em letras
    letras = []
    codigo_separado = codigo_morse.split(' ')
    for codigo in codigo_separado:
        for i in range(len(morse)):
            if codigo == morse[i]:
                letras.append(alfabeto[i])
                break
        else:
            letras.append(' ')

    # Retornar as letras correspondentes
    mensagem = ''.join(letras)
    return mensagem


codigo_morse = input()
mensagem_alfabeto = morse_para_alfabeto(codigo_morse)
print(mensagem_alfabeto)
