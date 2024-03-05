from latin2telugu import lang as telugu, latinized as telugu_latinized
from latin2tamil import lang as tamil, latinized as tamil_latinized
from latin2kannada import lang as kannada, latinized as kannada_latinized
from latin2malayalam import lang as malayalam, latinized as malayalam_latinized

class DeTransliterator:
    def __init__(self, lang=None):
        self.transliterated_text = ""
        self.lang = lang

        lang_txt = None
        lang_latinized = None
        if lang == "Telugu":
            lang_txt = telugu
            lang_latinized = telugu_latinized
        if lang == "Kannada":
            lang_txt = kannada
            lang_latinized = kannada_latinized
        if lang == "Tamil":
            lang_txt = tamil
            lang_latinized = tamil_latinized
        if lang == "Malayalam":
            lang_txt = malayalam
            lang_latinized = malayalam_latinized

        lang_txt = [each2 for each in lang_txt for each2 in each]
        lang_latinized = [each2 for each in lang_latinized for each2 in each]

        self.dict_of_letters = {}
        for j in range(len(lang_txt)):
            self.dict_of_letters[lang_latinized[j]] = lang_txt[j]

        self.sorted_keys = sorted(self.dict_of_letters.keys(), key=len, reverse=True)
    
    def detransliterate(self, text, lang=None):
        """DeTransliterate Dravida unicode strings from Latin characters as per ISO 15919.

        Args:
            text (string): Original text in Dravida unicode.
            lang (string): Language to transliterate

        Returns:
            string: DeTransliterated text.
        """
        if lang is None:
            lang = self.lang
        for key in self.sorted_keys:
            if key in text:
                text = text.replace(key, self.dict_of_letters[key])
        return text

