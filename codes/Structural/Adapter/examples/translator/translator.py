# Target Interface
class Translator:
    """
    رابط استاندارد برای مترجمان مختلف.
    """
    def translate(self, text):
        pass


# Adaptees
class EnglishTranslator:
    """
    مترجم مخصوص زبان انگلیسی.
    """
    def english_to_other(self, text):
        return f"Translated '{text}' from English."

class FrenchTranslator:
    """
    مترجم مخصوص زبان فرانسوی.
    """
    def french_to_other(self, text):
        return f"Traduit '{text}' du français."

class SpanishTranslator:
    """
    مترجم مخصوص زبان اسپانیایی.
    """
    def spanish_to_other(self, text):
        return f"Traducido '{text}' del español."


# Adapters
class EnglishAdapter(Translator):
    """
    آداپتر برای مترجم انگلیسی.
    """
    def __init__(self, translator: EnglishTranslator):
        self.translator = translator

    def translate(self, text):
        return self.translator.english_to_other(text)


class FrenchAdapter(Translator):
    """
    آداپتر برای مترجم فرانسوی.
    """
    def __init__(self, translator: FrenchTranslator):
        self.translator = translator

    def translate(self, text):
        return self.translator.french_to_other(text)


class SpanishAdapter(Translator):
    """
    آداپتر برای مترجم اسپانیایی.
    """
    def __init__(self, translator: SpanishTranslator):
        self.translator = translator

    def translate(self, text):
        return self.translator.spanish_to_other(text)


# Client Code
def translate_text(translator: Translator, text: str):
    """
    متن را با استفاده از مترجم ترجمه می‌کند.
    """
    print(translator.translate(text))


def main():
    english_translator = EnglishAdapter(EnglishTranslator())
    french_translator = FrenchAdapter(FrenchTranslator())
    spanish_translator = SpanishAdapter(SpanishTranslator())

    print("ترجمه‌ها:")
    translate_text(english_translator, "Hello world")
    translate_text(french_translator, "Bonjour le monde")
    translate_text(spanish_translator, "Hola mundo")


if __name__ == "__main__":
    main()
