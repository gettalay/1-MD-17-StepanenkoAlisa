english_to_russian = {}
with open('en-ru.txt', 'r', encoding='utf-8') as file:
    for line in file:
        english, russian = line.strip().split(' - ')
        russian_words = [word.strip() for word in russian.split(',')]
        english_to_russian[english] = russian_words

russian_to_english = {}
for english_word, russian_words in english_to_russian.items():
    for russian_word in russian_words:
        if russian_word in russian_to_english:
            russian_to_english[russian_word].append(english_word)
        else:
            russian_to_english[russian_word] = [english_word]

with open('ru-en.txt', 'w', encoding='utf-8') as file:
    for russian_word in sorted(russian_to_english.keys()):
        english_words = ', '.join(sorted(russian_to_english[russian_word]))
        file.write(f"{russian_word} – {english_words}\n")
