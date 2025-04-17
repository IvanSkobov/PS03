from bs4 import BeautifulSoup
import requests
from googletrans import Translator

# Функция для получения случайного английского слова и его определения
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    except Exception as e:
        print(f"Произошла ошибка при получении слова: {e}")
        return None

# Основная функция игры
def word_game():
    print("Добро пожаловать в игру! Угадайте слово по его определению.")

    translator = Translator()

    while True:
        word_dict = get_english_words()
        if not word_dict:
            continue  # если не удалось получить слово, пробуем снова

        word_en = word_dict.get("english_word").lower()
        definition_en = word_dict.get("word_definition")

        try:
            word_ru = translator.translate(word_en, dest='ru').text.lower()
            definition_ru = translator.translate(definition_en, dest='ru').text
        except Exception as e:
            print(f"Ошибка при переводе: {e}")
            continue

        print(f"\nОпределение: {definition_ru}")
        user_input = input("Что это за слово (на русском или английском)? ").strip().lower()

        if user_input == word_ru or user_input == word_en:
            print("Правильно! Отличная работа!")
        else:
            print(f"Неверно. Правильный ответ: {word_ru} (англ. {word_en})")

        play_again = input("\nХотите сыграть ещё раз? (y/n): ").strip().lower()
        if play_again != "y":
            print("Спасибо за игру!")
            break

# Запуск игры
word_game()
