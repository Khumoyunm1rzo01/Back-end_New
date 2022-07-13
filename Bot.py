from googletrans import Translator, constants

translator = Translator()
translation = translator.translate("Salom bu mening birinchi tarjimon botim! Bu botni mualliflik huquqlarini buzmagan holatda ishlashingiz tarafdoriman!", src="uz", dest="ru")
print(translation.text, translation.src)

LANGUAGES = constants.LANGUAGES
print(LANGUAGES)