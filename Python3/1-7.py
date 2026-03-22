import string

def task1():
    print("Завдання 1")
    print("Знайти кількість слів, що починаються з заданого слова")
    print()

    while True:
        text = input("Введіть текст українською мовою (до 1000 слів): ").strip()
        if len(text) > 0:
            break
        else:
            print("Помилка, текст не може бути порожнім. Спробуйте ще раз.")

    while True:
        search_word = input("Введіть слово для пошуку (без розділових знаків): ").strip()
        if len(search_word) > 0:
            has_punctuation = False
            for char in search_word:
                if char in string.punctuation:
                    has_punctuation = True
                    break
            if has_punctuation:
                print("Помилка, слово не повинно містити розділові знаки. Спробуйте ще раз.")
            else:
                break
        else:
            print("Помилка, слово не може бути порожнім. Спробуйте ще раз.")

    search_word_lower = search_word.lower()
    words = text.split()
    count = 0

    for word in words:
        clean_word = word.strip(string.punctuation)
        clean_word_lower = clean_word.lower()
        if clean_word_lower.startswith(search_word_lower):
            count = count + 1

    print()
    print(f"Результат: знайдено {count} слів, що починаються з '{search_word}'")
    print()

def task2():
    print("Завдання 2")
    print("Замінити букву (а) буквою (А)")
    print()
    while True:
        text = input("Введіть текст: ").strip()
        if len(text) > 0:
            break
        else:
            print("Помилка, текст не може бути порожнім. Спробуйте ще раз.")

    replacement_count = 0
    for char in text:
        if char == 'а':
            replacement_count = replacement_count + 1
    new_text = text.replace('а', 'А')
    total_chars = len(text)
    letter_count = 0
    for char in text:
        if char.isalpha():
            letter_count = letter_count + 1

    print()
    print("Оригінальний текст:")
    print(text)
    print()
    print("Текст після заміни:")
    print(new_text)
    print()
    print(f"Кількість замін (а) на (А): {replacement_count}")
    print(f"Загальна кількість символів: {total_chars}")
    print(f"Кількість літер: {letter_count}")
    print()

def task3():
    print("Завдання 3")
    print("Визначити, скільки разів зустрічається задане слово")
    print()
    while True:
        text = input("Введіть текст: ").strip()
        if len(text) > 0:
            break
        else:
            print("Помилка, текст не може бути порожнім. Спробуйте ще раз.")

    while True:
        search_word = input("Введіть слово для пошуку: ").strip()
        if len(search_word) > 0:
            has_punctuation = False
            for char in search_word:
                if char in string.punctuation:
                    has_punctuation = True
                    break
            if has_punctuation:
                print("Помилка, слово не повинно містити розділові знаки. Спробуйте ще раз.")
            else:
                break
        else:
            print("Помилка: слово не може бути порожнім. Спробуйте ще раз.")

    search_word_lower = search_word.lower()
    words = text.split()
    count = 0

    for word in words:
        clean_word = word.strip(string.punctuation)
        if clean_word.lower() == search_word_lower:
            count = count + 1

    print()
    print(f"Слово '{search_word}' зустрічається {count} разів у тексті")
    print()

def task4():
    print("Завдання 4")
    print("Перетворення тексту з різним форматуванням для двох половин")
    print()
    while True:
        text = input("Введіть текст українською мовою (до 1000 слів): ").strip()
        if len(text) > 0:
            break
        else:
            print("Помилка, текст не може бути порожнім. Спробуйте ще раз.")

    words = text.split()
    total_words = len(words)
    middle_index = total_words // 2

    first_half_words = []
    for i in range(middle_index):
        word = words[i]
        first_letter_index = -1
        for j in range(len(word)):
            if word[j].isalpha():
                first_letter_index = j
                break
        if first_letter_index != -1:
            punctuation_before = word[0:first_letter_index]
            first_letter = word[first_letter_index].upper()
            rest_of_word = word[first_letter_index + 1:].lower()
            new_word = punctuation_before + first_letter + rest_of_word
        else:
            new_word = word
        first_half_words.append(new_word)

    second_half_words = []
    for i in range(middle_index, total_words):
        word = words[i].lower()
        second_half_words.append(word + "*")

    first_half_text = " ".join(first_half_words)
    second_half_text = " ".join(second_half_words)
    result_text = first_half_text + " | " + second_half_text

    print()
    print("Оригінальний текст:")
    print(text)
    print()
    print("Перетворений текст:")
    print(result_text)
    print()

def task5():
    print("Завдання 5")
    print("Знайти слова, що починаються та закінчуються на задані літери")
    print()
    while True:
        text = input("Введіть текст англійською мовою (до 1000 слів): ").strip()
        if len(text) > 0:
            break
        else:
            print("Помилка, текст не може бути порожнім. Спробуйте ще раз.")

    while True:
        start_letter = input("Введіть літеру початку слова (англійською): ").strip()
        if len(start_letter) == 1 and start_letter.isalpha():
            if start_letter.lower() in 'abcdefghijklmnopqrstuvwxyz':
                break
            else:
                print("Помилка, літера повинна бути англійською. Спробуйте ще раз.")
        else:
            print("Помилка, введіть одну літеру. Спробуйте ще раз.")

    while True:
        end_letter = input("Введіть літеру кінця слова (англійською): ").strip()
        if len(end_letter) == 1 and end_letter.isalpha():
            if end_letter.lower() in 'abcdefghijklmnopqrstuvwxyz':
                break
            else:
                print("Помилка, літера повинна бути англійською. Спробуйте ще раз.")
        else:
            print("Помилка, введіть одну літеру. Спробуйте ще раз.")

    start_letter_lower = start_letter.lower()
    end_letter_lower = end_letter.lower()
    words = text.split()
    words_starting = []
    for word in words:
        clean_word = word.strip(string.punctuation)
        if len(clean_word) > 0:
            if clean_word[0].lower() == start_letter_lower:
                words_starting.append(clean_word)

    words_ending = []
    for word in words:
        clean_word = word.strip(string.punctuation)
        if len(clean_word) > 0:
            if clean_word[len(clean_word) - 1].lower() == end_letter_lower:
                words_ending.append(clean_word)

    print()
    print(f"Слова, що починаються на літеру '{start_letter}':")
    if len(words_starting) > 0:
        for word in words_starting:
            print(f"  - {word}")
    else:
        print("  (слова не знайдено)")

    print()
    print(f"Слова, що закінчуються на літеру '{end_letter}':")
    if len(words_ending) > 0:
        for word in words_ending:
            print(f"  - {word}")
    else:
        print("  (слова не знайдено)")
    print()

def task6():
    print("Завдання 6")
    print("Підрахунок голосних літер в тексті")
    print()
    while True:
        text = input("Введіть текст англійською мовою (до 100 слів): ").strip()
        if len(text) > 0:
            break
        else:
            print("Помилка, текст не може бути порожнім. Спробуйте ще раз.")

    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count = vowel_count + 1

    print()
    print(f"Кількість голосних літер у тексті: {vowel_count}")
    print()

def task7():
    print("Завдання 7")
    print("Знайти всі імена і власні назви (слова з великої літери)")
    print()
    while True:
        text = input("Введіть текст англійською мовою (до 1000 слів): ").strip()
        if len(text) > 0:
            break
        else:
            print("Помилка: текст не може бути порожнім. Спробуйте ще раз.")

    sentences = []
    current_sentence = ""
    for char in text:
        current_sentence = current_sentence + char
        if char in '.!?':
            sentences.append(current_sentence.strip())
            current_sentence = ""
    if len(current_sentence.strip()) > 0:
        sentences.append(current_sentence.strip())

    proper_nouns = []
    for sentence in sentences:
        words = sentence.split()
        for i in range(len(words)):
            word = words[i]
            clean_word = word.strip(string.punctuation)
            if len(clean_word) > 0:
                if clean_word[0].isupper():
                    if i > 0:
                        proper_nouns.append(clean_word)
                    else:
                        for j in range(1, len(words)):
                            other_word = words[j].strip(string.punctuation)
                            if other_word.lower() == clean_word.lower() and other_word[0].isupper():
                                proper_nouns.append(clean_word)
                                break

    print()
    print("Знайдені імена та власні назви:")
    if len(proper_nouns) > 0:
        for noun in proper_nouns:
            print(f"  - {noun}")
    else:
        print("  (імена та власні назви не знайдено)")
    print()

def main():
    while True:
        print("Оберіть завдання для виконання:")
        print("1 - Завдання 1: Підрахунок слів, що починаються з заданого слова")
        print("2 - Завдання 2: Заміна букви (а) на (А)")
        print("3 - Завдання 3: Підрахунок заданого слова в тексті")
        print("4 - Завдання 4: Перетворення тексту (дві половини)")
        print("5 - Завдання 5: Слова на задані літери (початок/кінець)")
        print("6 - Завдання 6: Підрахунок голосних літер")
        print("7 - Завдання 7: Знайти імена та власні назви")
        print("0 - Вихід")
        print()

        choice = input("Ваш вибір: ").strip()
        print()

        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "3":
            task3()
        elif choice == "4":
            task4()
        elif choice == "5":
            task5()
        elif choice == "6":
            task6()
        elif choice == "7":
            task7()
        elif choice == "0":
            print("Завершення роботи програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
            print()

if __name__ == "__main__":
    main()