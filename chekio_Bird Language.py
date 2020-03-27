# Bird Language

VOWELS = "aeiouyAEIOUY"
CONSONANTS = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

def translate(phrase):
    i = 0
    new_phrase = ''
    while i <= len(phrase):
        if phrase[i] in VOWELS:
            new_phrase += phrase[i]
            i += 3
        elif phrase[i] in CONSONANTS:
            new_phrase += phrase[i]
            i += 2
        else:
            new_phrase += phrase[i]
            i += 1
        if i >= len(phrase):
            return new_phrase
    return new_phrase

if __name__ == '__main__':
    print("Example:")
    print(translate("sooooso aaaaaaaaa"))

'''
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
'''

# other solution

VOWELS = "aeiouy"
def cut(text):
    i = 0
    while i < len(text):
        yield text[i]
        if text[i] in VOWELS: i += 3
        else: i += 2

def translate(phrase):
    return " ".join(["".join(cut(word)) for word in phrase.split()])