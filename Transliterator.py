#!/usr/bin/env python
# coding: utf-8

charmap_iso15919 = {
    "Kannada": [
        u"ಀ", u"ಁ", u"ಂ", u"ಃ", u"಄", u"ಅ", u"ಆ", u"ಇ", u"ಈ", u"ಉ", u"ಊ", u"ಋ", u"ಌ", u"಍", u"ಎ", u"ಏ",
        u"ಐ", u"಑", u"ಒ", u"ಓ", u"ಔ", u"ಕ", u"ಖ", u"ಗ", u"ಘ", u"ಙ", u"ಚ", u"ಛ", u"ಜ", u"ಝ", u"ಞ", u"ಟ",
        u"ಠ", u"ಡ", u"ಢ", u"ಣ", u"ತ", u"ಥ", u"ದ", u"ಧ", u"ನ", u"಩", u"ಪ", u"ಫ", u"ಬ", u"ಭ", u"ಮ", u"ಯ",
        u"ರ", u"ಱ", u"ಲ", u"ಳ", u"಴", u"ವ", u"ಶ", u"ಷ", u"ಸ", u"ಹ", u"಺", u"಻", u"಼", u"ಽ", u"ಾ", u"ಿ",
        u"ೀ", u"ು", u"ೂ", u"ೃ", u"ೄ", u"೅", u"ೆ", u"ೇ", u"ೈ", u"೉", u"ೊ", u"ೋ", u"ೌ", u"್", u"೎", u"೏",
        u"೐", u"೑", u"೒", u"೓", u"೔", u"ೕ", u"ೖ", u"೗", u"೘", u"೙", u"೚", u"೛", u"೜", u"ೝ", u"ೞ", u"೟",
        u"ೠ", u"ೡ", u"ೢ", u"ೣ", u"೤", u"೥", u"೦", u"೧", u"೨", u"೩", u"೪", u"೫", u"೬", u"೭", u"೮", u"೯",
        u"೰", u"ೱ", u"ೲ", u"ೳ", u"೴", u"೵", u"೶", u"೷", u"೸", u"೹", u"೺", u"೻", u"೼", u"೽", u"೾", u"೿"
    ],
    
    "Telugu": [
        u"ఀ", u"ఁ", u"ం", u"ః", u"಄", u"అ", u"ఆ", u"ఇ", u"ఈ", u"ఉ", u"ఊ", u"ఋ", u"ఌ", u"಍", u"ఎ", u"ఏ",
        u"ఐ", u"೐", u"ఒ", u"ఓ", u"ఔ", u"క", u"ఖ", u"గ", u"ఘ", u"ఙ", u"చ", u"ఛ", u"జ", u"ఝ", u"ఞ", u"ట",
        u"ఠ", u"డ", u"ఢ", u"ణ", u"త", u"థ", u"ద", u"ధ", u"న", u"೐", u"ప", u"ఫ", u"బ", u"భ", u"మ", u"య",
        u"ర", u"ఱ", u"ల", u"ళ", u"ఴ", u"వ", u"శ", u"ష", u"స", u"హ", u"಺", u"಻", u"఼◌఼ ", u"ఽ", u"ా", u"ి",
        u"ీ", u"ు", u"ూ", u"ృ", u"ౄ", u"೔", u"ె", u"ే", u"ై", u"೉", u"ొ", u"ో", u"ౌ", u"్", u"೉", u"೉",
        u"೐", u"೑", u"೒", u"೓", u"೔", u"ౕ", u"ౖ", u"೔", u"ౘ", u"ౙ", u"ౚ", u"೔", u"೔", u"◌్", u"೔", u"೔",
        u"ౠ", u"ౡ", u"ౢ", u"ౣ", u"೤", u"೥", u"౦", u"౧", u"౨", u"౩", u"౪", u"౫", u"౬", u"౭", u"౮", u"౯",
        # u"౷", u"౷", u"౷", u"౷", u"౷", u"౷", u"౷", u"౷", u"౸", u"౹", u"౺", u"౻", u"౼", u"౽", u"౾", u"౿",
        u"౷", u"౷", u"౷", u"౷", u"౷", u"౷", u"౷", u"౷", u"", u"", u"", u"", u"", u"", u"", u"",
    ],

    "Tamil": [
        u"", u"", u"", u"ஃ", u"", u"அ", u"ஆ", u"இ", u"ஈ", u"உ", u"ஊ", u"", u"", u"", u"எ", u"ஏ",
        u"ஐ", u"", u"ஒ", u"ஓ", u"ஔ", u"க", u"", u"", u"", u"ங", u"ச", u"", u"ஜ", u"", u"ஞ", u"ட",
        u"", u"", u"", u"ண", u"த", u"", u"", u"", u"ந", u"ன", u"ப", u"", u"", u"", u"ம", u"ய",
        u"ர", u"ற", u"ல", u"ள", u"ழ", u"வ", u"ஶ", u"ஷ", u"ஸ", u"ஹ", u"", u"", u"", u"", u"ா", u"ி",
        u"ீ", u"ு", u"ூ", u"", u"", u"", u"ெ", u"ே", u"ை", u"", u"ொ", u"ோ", u"ௌ", u"்", u"", u"",
        u"ௐ", u"", u"", u"", u"", u"", u"", u"ௗ", u"", u"", u"", u"", u"", u"", u"", u"",
        u"", u"", u"", u"", u"", u"", u"௦", u"௧", u"௨", u"௩", u"௪", u"௫", u"௬", u"௭", u"௮", u"௯",
        # u"௰", u"௱", u"௲", u"௳", u"௴", u"௵", u"௶", u"௷", u"௸", u"௹", u"௺", u"", u"", u"", u"", u""
        u"౷", u"౷", u"౷", u"౷", u"౷", u"౷", u"౷", u"౷", u"", u"", u"", u"", u"", u"", u"", u"",
    ],

    "Malayalam": [
       u"", u"◌ഁ", u"ം", u"ഃ", u"ഄ", u"അ" u"ആ", u"ഇ", u"ഈ", u"ഉ", u"ഊ", u"ഋ", u"ഌ", u"", u"എ", u"ഏ",
       u"ഐ", u"", u"ഒ", u"ഓ", u"ഔ", u"ക", u"ഖ", u"ഗ", u"ഘ", u"ങ", u"ച", u"ഛ", u"ജ", u"ഝ", u"ഞ", u"ട",
       u"ഠ", u"ഡ", u"ഢ", u"ണ", u"ത", u"ഥ", u"ദ", u"ധ", u"ന", u"ഩ", u"പ", u"ഫ", u"ബ", u"ഭ", u"മ", u"യ",
       u"ര", u"റ", u"ല", u"ള", u"ഴ", u"വ", u"ശ", u"ഷ", u"സ", u"ഹ", u"ഺ", u"഻", u"഼", u"ഽ", u"ാ", u"ി",
       u"ീ", u"ു", u"ൂ", u"ൃ", u"ൄ", u"", u"െ", u"േ", u"ൈ", u"", u"ൊ", u"ോ", u"ൌ", u"്", u"ൎ", u"൏",
       u"", u"", u"", u"", u"ൔ", u"ൔ", u"ൔ", u"ൗ", u"ൔ", u"ൔ", u"ൔ", u"ൔ", u"ൔ", u"ൔ", u"ൔ", u"ൟ",
       u"ൠ", u"ൡ", u"ൢ", u"ൣ", u"", u"", u"൦", u"൧", u"൨", u"൩", u"൪", u"൫", u"൬", u"൭", u"൮", u"൯",
       # u"൰", u"൱", u"൲", u"൳", u"൴", u"൵", u"൶", u"൷", u"൸", u"൹", u"ൺ", u"ൻ", u"ർ", u"ൽ", u"ൾ", u"ൿ",
       u"", u"൱", u"൲", u"൳", u"൴", u"൵", u"൶", u"൷", u"൸", u"൹", u"ൺ", u"ൻ", u"ർ", u"ൽ", u"ൾ", u"ൿ",
    ],

    "Latin": [
        u"", u"m̐", u"ṁ", u"ḥ", u"", u"a", u"ā", u"i", u"ī", u"u", u"ū", u"ṛ", u"l̥", u"ê", u"e", u"ē",
        u"ai", u"ô", u"o", u"ō", u"au", u"ka", u"kha", u"ga", u"gha", u"ṅa", u"ca", u"cha", u"ja", u"jha", u"ña", u"ṭa",
        u"ṭha", u"ḍa", u"ḍha", u"ṇa", u"ta", u"tha", u"da", u"dha", u"na", u"ṉa", u"pa", u"pha", u"ba", u"bha", u"ma", u"ya",
        u"ra", u"ṟa", u"la", u"ḷa", u"ḻa", u"va", u"śa", u"ṣa", u"sa", u"ha", u"", u"", u"", u"'", u"ā", u"i",
        u"ī", u"u", u"ū", u"ṛ", u"ṝ", u"ê", u"e", u"ē", u"ai", u"ô", u"o", u"ō", u"au", u"", u"", u"",
        u"oṃ", u"", u"", u"", u"", u"", u"", u"", u"qa", u"ḵẖa", u"ġ", u"za", u"ṛa", u"ṛha", u"fa", u"ẏa",
        u"ṝ", u"ḹ", u"l̥", u"ḹ", u".", u"..", u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9",
        u"…", u"", u"", u"", u"", u"", u"", u"", u"", u"", u"ṇ", u"n", u"ṟ", u"l", u"ḷ", u"k"
    ],
}


class Transliterator:

    def __init__(self, lang=None):
        self.transliterated_text = ""
        self.lang = lang

    def transliterate(self, text, lang=None):
        """Transliterate Dravida unicode strings to Latin characters as per ISO 15919.

        Args:
            text (string): Original text in Dravida unicode.
            lang (string): Language to transliterate

        Returns:
            string: Transliterated text.
        """
        if lang is None:
            lang = self.lang
        index = 0
        self.transliterated_text = ""
        for character in text:
            index += 1
            character_position = self._get_character_position(character, lang)

            if character_position >= 62 and character_position <= 77:
                self._delete_schwa()

            if character_position in [7, 9] and self.transliterated_text[-1:] == "a":
                self.transliterated_text += ":"

            if character_position > 0 and character_position <= 128:
                try:
                    if character_position == 2:
                        if self._get_character_position(text[index]) in [21, 22, 23, 24, 25]:
                            self.transliterated_text += charmap_iso15919["Latin"][25]
                            self._delete_schwa()
                        elif self._get_character_position(text[index]) in [26, 27, 28, 29, 30]:
                            self.transliterated_text += charmap_iso15919["Latin"][30]
                            self._delete_schwa()
                        elif self._get_character_position(text[index]) in [31, 32, 33, 34, 35]:
                            self.transliterated_text += charmap_iso15919["Latin"][35]
                            self._delete_schwa()
                        elif self._get_character_position(text[index]) in [36, 37, 38, 39, 40]:
                            self.transliterated_text += charmap_iso15919["Latin"][40]
                            self._delete_schwa()
                        elif self._get_character_position(text[index]) in [42, 43, 44, 45, 46]:
                            self.transliterated_text += charmap_iso15919["Latin"][46]
                            self._delete_schwa()
                        else:
                            self.transliterated_text += charmap_iso15919["Latin"][character_position]
                    elif character_position == 28 and self._get_character_position(text[index]) == 60:
                        self.transliterated_text += charmap_iso15919["Latin"][91]
                    elif character_position == 43 and self._get_character_position(text[index]) == 60:
                        self.transliterated_text += charmap_iso15919["Latin"][94]
                    else:
                        self.transliterated_text += charmap_iso15919["Latin"][character_position]
                except:
                    self.transliterated_text += charmap_iso15919["Latin"][character_position]

            else:
                self.transliterated_text += character
        try:
            result = self.transliterated_text.decode("utf-8")
        except BaseException:
            result = self.transliterated_text
        return result

    def _get_character_position(self, character, lang=None):
        if lang is None:
            lang=self.lang
        start_char = None
        if lang == "Tamil":
            start_char = 0x0B80
        if lang == "Telugu":
            start_char = 0x0C00
        if lang == "Kannada":
            start_char = 0x0C80
        if lang == "Malayalam":
            start_char = 0x0D00
        character_position = ord(character) - start_char
        return character_position

    def _delete_schwa(self):
        if self.transliterated_text[-1:] == "a":
            self.transliterated_text = self.transliterated_text[:-1]



    # # latn_to_drvda DOESN'T WORK. DON'T USE
    # def latn_to_drvda(self, text, lang):
    #     """Transliterate Latin characters to Dravida unicode string as per ISO 15919.

    #     Args:
    #         text (string): Original text in Latin characters.
    #         lang (string): Language to transliterate

    #     Returns:
    #         string: DeTransliterated text.
    #     """
    #     self.transliterated_text = ""
    #     index = 0
    #     while index < len(text):
    #         char = text[index]
    #         try:
    #             char_position = charmap_iso15919["Latin"].index(char)
    #         except ValueError:
    #             char_position = -1

    #         if char_position != -1:
    #             self.transliterated_text += charmap_iso15919[lang][char_position]
    #         else:
    #             self.transliterated_text += char

    #         index += 1

    #     try:
    #         result = self.transliterated_text.decode("utf-8")
    #     except AttributeError:
    #         result = self.transliterated_text
    #     return result

    # special_cases = {
    #     # Add special cases here
    #     # Example: 'ch' : u'చ'
    # }
