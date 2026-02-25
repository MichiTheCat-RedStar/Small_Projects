rus_to_eng = {
    'ё': '`', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '0': '0', '-': '-', '=': '=',
    'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p', 'х': '[', 'ъ': ']', '\\': '\\',
    'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l', 'ж': ';', 'э': "'",
    'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.',
    'Ё': '~', '!': '!', '"': '@', '№': '#', ';': '$', '%': '%', ':': '^', '?': '&', '*': '*', '(': '(', ')': ')', '_': '_', '+': '+',
    'Й': 'Q', 'Ц': 'W', 'У': 'E', 'К': 'R', 'Е': 'T', 'Н': 'Y', 'Г': 'U', 'Ш': 'I', 'Щ': 'O', 'З': 'P', 'Х': '{', 'Ъ': '}', '/': '|',
    'Ф': 'A', 'Ы': 'S', 'В': 'D', 'А': 'F', 'П': 'G', 'Р': 'H', 'О': 'J', 'Л': 'K', 'Д': 'L', 'Ж': ':', 'Э': '"',
    'Я': 'Z', 'Ч': 'X', 'С': 'C', 'М': 'V', 'И': 'B', 'Т': 'N', 'Ь': 'M', 'Б': '<', 'Ю': '>'
}

print('Стоит уточнить, что тут неправильный перевод символов вроде запятых и подобного!')
eng_to_rus = {v: k for k, v in rus_to_eng.items()}

def detect_layout(text):
    rus_chars = sum(1 for char in text if char in rus_to_eng)
    eng_chars = sum(1 for char in text if char in eng_to_rus)
    return 'rus' if rus_chars > eng_chars else 'eng'

def translate_text(text, direction):
    if direction == 'rus_to_eng':
        return ''.join(rus_to_eng.get(char, char) for char in text)
    else:
        return ''.join(eng_to_rus.get(char, char) for char in text)

while True:
    user_input = input('> ')
    layout = detect_layout(user_input)
    
    if layout == 'rus':
        translated = translate_text(user_input, 'rus_to_eng')
    else:
        translated = translate_text(user_input, 'eng_to_rus')
    
    print('\n', translated, '\n')