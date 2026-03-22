import string

class Alphabet:
    lang = 'UA'
    letters = list("абвгґдеєжзиіїйклмнопрстуфхцчшщьюя")

    def __init__(self, lang=None, letters=None):
        if lang is None:
            self.lang = Alphabet.lang
        else:
            self.lang = lang
        if letters is None:
            self.letters = Alphabet.letters
        else:
            self.letters = letters

    def print_alphabet(self):
        print(f"Алфавіт ({self.lang}): {self.letters}")

    def letters_num(self):
        return len(self.letters)

    def is_ua_lang(self, text):
        ua_letters = set("абвгґдеєжзиіїйклмнопрстуфхцчшщьюя")
        text_lower = text.lower()
        for char in text_lower:
            if char in ua_letters:
                return True
        return False


class EngAlphabet(Alphabet):
    __en_letters_num = 26

    def __init__(self):
        super().__init__('En', list(string.ascii_uppercase))

    def is_en_letter(self, letter):
        return letter.upper() in self.letters

    def letters_num(self):
        return EngAlphabet.__en_letters_num

    @staticmethod
    def example():
        return "The quick brown fox jumps over the lazy dog."


if __name__ == '__main__':
    print("--- Тести Завдання 1 ---")
    eng_alpha = EngAlphabet()
    eng_alpha.print_alphabet()
    print(f"Кількість літер в алфавіті: {eng_alpha.letters_num()}")
    print(f"Чи 'J' належить до англійського алфавіту? {eng_alpha.is_en_letter('J')}")
    
    ua_alpha = Alphabet()
    print(f"Чи 'Щ' належить до українського алфавіту? {ua_alpha.is_ua_lang('Щ')}")
    
    print(f"Приклад тексту англійською: {EngAlphabet.example()}")
