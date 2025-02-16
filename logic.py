# Задание №3
from translate import Translator
import requests
from collections import defaultdict


# Задание №5
qeastions = {"Как тебя зовут?" : "Я твой бот переводчик и я тебе переведу любое слово или предложение.",
             "Сколько тебе лет?" : "Это слишком тяжелый вопрос"}


class TextAnalysis():

    # Задание №1
    memory = defaultdict(list)

    def __init__(self, text, owner):

        # Задание №2
        TextAnalysis.memory[owner].append(self)

        self.text = text
        self.translation = self.__translate(self.text, "ru", "en")

        # Задание №6
        if self.text in qeastions.keys():
            self.response = qeastions[self.text]
        else:
            self.response = self.get_answer()

    def get_answer(self):
        res = self.__translate("I don't know how to help", "en", "ru")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            translator = Translator(from_lang=from_lang, to_lang=to_lang)
            translation = translator.translate(text)
            return translation
        except:
            return "Перевод не удался"


