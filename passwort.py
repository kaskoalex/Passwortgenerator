import random

def ask_question(question):
    print( question, "Нажмите Да или Нет")
    answer = input()
    if answer == "Да":
        return True
    else:
        print("Вводите пожалуйста правильные значения: или Да, или Нет")
        return False

def generate_password(length, chars):
    passwort = ""
    for i in range(length):
        random_index = random.randint(0, len(chars) - 1)
        passwort += chars[random_index]

    return passwort

def is_valid(length_number):

    if length_number.isdigit():
        return True
    else:
        print("Не правильный ввод. Введите пожалуйста цифры")        
        return False
    



while True:
    print("Привет. Я генератор паролей. \nЯ задам пару уточняющих вопросов, на основе которых сгенерирую пароль. \nДавай начнём.")
    
    print("Введите длину пароля")
    length_number=input()
    if not is_valid(length_number):
        continue
    length = int(length_number)
    
    print("Введите сколько вам нужно паролей")
    crowd_number = input()
    
    if not is_valid(crowd_number):
        continue
    crowd = int(crowd_number)
    
    digits_enabled = ask_question("Включать ли цыфры?")
    
    latin_lowercase_enabled = ask_question("Включать ли строчные латинские буквы?")
    
    latin_uppercase_enabled = ask_question("Включать ли заглавные латинские буквы?")

    russian_lowercase_enabled = ask_question("Включать ли строчные русские буквы?")
    
    russian_uppercase_enabled = ask_question("Включать ли заглавные русские буквы?")
    
    russian_uppercase_enabled = ask_question("Включать ли знаки пунктуации?")
    
    enabled_chars = ""
    digits = "0123456789"
    latin_lowercase_letters="abcdefghijklmnopqrstuvwxyz"
    latin_uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    russian_lowercase_letters = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    russian_uppercase_letters = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    punctuation = "!#$%&*+-=?@^_"
    
    
    if digits_enabled:
        enabled_chars += digits
    
    if latin_uppercase_enabled:
        enabled_chars += latin_uppercase_letters
        
    if latin_lowercase_enabled:
        enabled_chars += latin_lowercase_letters
    
    if russian_uppercase_enabled:
        enabled_chars += russian_uppercase_letters
        
    if russian_lowercase_enabled:
        enabled_chars += russian_lowercase_letters
        
    if punctuation:
        enabled_chars += punctuation
    for i in range(crowd):
        passwort = generate_password(length, enabled_chars)
        print(passwort)
        
