# Transliterate Dravida

Tools to transliterate from and detransliterate to Dravida languages (Kannada, Malayalam, Tamil, and Telugu).

## Files Organization:
### Main files:
1. transliterate.py: Given file (text or pickle) and the script, transliterates from provided script and saves it in specified file.
2. detransliterate.py: Given file (text or pickle) and the script, detransliterates to required script and saves it in specified file.

### Class files:
1. MyTransliterator.py: Defined the class Transliterator. Transliterates TaKaMaTe into latin.
2. Transliterator.py: Initial version of Transliterator. Not in use now because it wasn't possible to get back the original script using DeTransliterator.
3. DeTransliterator.py: Defined the class DeTransliterator. DeTransliterates TaKaMaTe from latin.

### Helper files: 
1. latin2kannada.py - Kannada Latin pairs
2. latin2tamil.py - Tamil Latin pairs
3. latin2malayalam.py - Malayalam Latin pairs
4. latin2telugu.py - Telugu Latin pairs

### Test files:
1. test_tools.sh - Tests Transliteratiion and DeTransliteration for all scripts.
    - Generates kn_transliterated.txt, ml_transliterated.txt, ta_transliterated.txt, te_transliterated.txt
    - Generates kn_detransliterated.txt, ml_detransliterated.txt, ta_detransliterated.txt, te_detransliterated.txt
2. tests/kn_head.txt, tests/ml_head.txt, tests/ta_head.txt, tests/te_head.txt - 5 lines for each script. For testing.
3. tests/latin2dravida_test.py - Tests Transliteratiion and DeTransliteration, one for each script.
    - Generates latin2dravida_test.txt
4. tests/transliterate_for_lat2dravida.py - Checks if the pairs from helper files have same number of elements.


## quick start

```python
from translit.Transliterator import Transliterator
from translit.DeTransliterator import DeTransliterator
transliterator = Transliterator("Telugu")
text = u'ప్రియాంక విప్పారిత నేత్రాలతో త్రినాధ్ కేసే మౌనంగా చూస్తుండి పోయింది.'
trans_text = transliterator.transliterate(text)
print(trans_text)
# priyāṁka vippārita nētrālatō trinādh kēsē maunaṁgā cūstuṁḍi pōyiṁdi.
detransliterator = DeTransliterator("Telugu")
re_text = detransliterator.detransliterate(trans_text)
print(re_text)
# ప్రియాంక విప్పారిత నేత్రాలతో త్రినాధ్ కేసే మౌనంగా చూస్తుండి పోయింది.
```

## Known issues
1. The (de)transliterations output for Malayalam are not one-to-one due to different representations for same sound.
    Ex: ൿ and ക്, ർ and റ്, ൻ and ന്.
    We seek feedback for the correctness of the current state, and what needs to be done to make them correct.
No known issues for remaining languages. We encourage the community to report more issues.

## License

MIT
