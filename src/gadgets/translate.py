from googletrans import Translator


def translate_to_english(text):
    """
    Translates the given text to English using Google Translate API.
    """
    translator = Translator()
    try:
        translated = translator.translate(text, dest='en')
        return translated.text
    except Exception as e:
        print(f"Error during translation: {e}")
        return None
