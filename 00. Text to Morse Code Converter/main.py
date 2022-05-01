morse_code = {
    'a': '·−',
    'b': '−···',
    'c': '−·−·',
    'd': '−··',
    'e': '·',
    'f': '··−·',
    'g': '−−·',
    'h': '····',
    'i': '··',
    'j': '·−−−',
    'k': '−·−',
    'l': '·−··',
    'm': '−−',
    'n': '−·',
    'o': '−−−',
    'p': '·−−·',
    'q': '−−·−',
    'r': '·−·',
    's': '···',
    't': '−',
    'u': '··−',
    'v': '···−',
    'w': '·−−',
    'x': '−··−',
    'y': '−·−−',
    'z': '−−··',
    '0': '−−−−−',
    '1': '·−−−−',
    '2': '··−−−',
    '3': '···−−',
    '4': '····−',
    '5': '·····',
    '6': '−····',
    '7': '−−···',
    '8': '−−−··',
    '9': '−−−−·'
}

sentence = input("Write a sentence to encode in morse : ").lower().split()
encoded_word = ""

for word in sentence:
    for letter in word:
        if letter == "'":
            letter = "·−−−−·"
            encoded_word += " " + letter
        else:
            try:
                letter = morse_code[letter]
            except KeyError:
                pass
            else:
                encoded_word += " " + letter
    if sentence.index(word) != len(sentence) - 1:
        encoded_word += " / "

print(f'Your encoded sentence is: {encoded_word}')
