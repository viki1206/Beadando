def fordito(szoveg,irany):
    karakterek = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','',' ','\t',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '?', '/', '-', '(', ')', '!']
    morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..','.---', '-.-','.-..', '--', '-.',
        '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..','','\t',' ',
        '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----', '--..--',
        '.-.-.-', '..--..', '-..-.', '-....-', '-.--.', '-.--.-', '-.-.--']

    ODA=dict(zip(karakterek,morse))
    VISSZA=dict(zip(morse,karakterek))

    alak = ''

    if irany.upper() == "MORSE":
        for c in szoveg:
            alak += ODA[c.upper()] + ' '
        alak = alak[0:len(alak) - 1]

    else:
        szoveg += ' '
        szavak = ''
        for char in szoveg:
            if char != ' ' and char != '\t':
                szavak += char
            elif char == ' ' or char == '\t':
                alak += VISSZA[szavak]
                szavak = ''
                if char == '\t':
                    alak += ' '
    print(alak)
    fordito("ez a program", "morse")
