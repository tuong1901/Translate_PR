from googletrans import Translator

class translation_ggapi:
    def __init__(self):
        self.translator = Translator()
    def translate(self, text, dest="vi"):
        return self.translator.translate(text, dest=dest).text

