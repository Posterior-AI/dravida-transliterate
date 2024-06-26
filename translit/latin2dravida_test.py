# coding: utf-8
# import sys
# sys.path.append('..')

from translit.Transliterator import Transliterator
from translit.DeTransliterator import DeTransliterator

lang_texts = [
    {
        "lang": "Telugu",
        "text": u'ప్రియాంక విప్పారిత నేత్రాలతో త్రినాధ్ కేసే మౌనంగా చూస్తుండి పోయింది.\n\n సరీగ్గా ఆ సమయంలో త్రినాధ్ చూస్తున్న పేపర్స్ సుదర్శన్ రావుకి సంబంధించినవి. ఆ పేపర్సు అందవలసిన వారికి అందితే అదే సుదర్శన్ రావు పతనానికి చివరి అంకం అవుతుంది.\n\n వారం రోజులుగా ప్రియాంక ఉదయాన్నే బయలుదేరి త్రినాధ్ దగ్గరకు రావడం, రోజంతా అతనితో వుంటూ, పర్సనల్ సెక్రటరీ పదవి సమర్దవంతంగా నిర్వహించడం జరుగుతుంది.\n\n "మా నాన్నగారు, అన్నయ్య చేసే ఎన్నో మోసాలకు నేను ప్రత్యక్షసాక్షిని. వాటి ద్వారా నీ కుటుంబానికి జరిగిన అన్యాయాన్ని సరిదిద్దుకోవచ్చుగదా?" ప్రియాంక అన్న మాటలకు త్రినాధ్ తలెత్తి చిరునవ్వుతో చూశాడు.\n\n "అలా వద్దు...',
        "transliterated": u''
    },
    {
        "lang":  u"Kannada",
        "text": u"ಪಾಲ್ಗೊಳ್ಳುವ ಬೆಂಗಳೂರು ಸ್ಕೂಲ್ಸ್ ಸ್ಪೋರ್ಟ್ಸ್ ಫೌಂಡೇಶನ್‌ನ (ಬಿಎಸ್‌ಎಸ್‌ಎಫ್) ತಂಡದ ಪ್ರಾಯೋಜಕತ್ವ ವಹಿಸಲು ಯುಬಿ ಸಮೂಹದ ಮುಖ್ಯಸ್ಥ ವಿಜಯ್ ಮಲ್ಯ ಮುಂದಾಗಿದ್ದಾರೆ. ಈ ಶಾಲಾ ತಂಡ ಕೂಟದಲ್ಲಿ ಕಳೆದ ಮೂರು ವರ್ಷದಿಂದಲೂ ಪಾಲ್ಗೊಳ್ಳುತ್ತಿವೆ. ಆದರೆ ಪ್ರಾಯೋಜಕರ ಕೊರತೆ ಅದರ ಉತ್ಸಾಹಕ್ಕೆ ತಣ್ಣೀರೆರಚುತ್ತಲೇ ಬಂದಿದೆ. ಬಹುತೇಕ ಸಂದರ್ಭಗಳಲ್ಲಿ ಮಕ್ಕಳ ಪೋಷಕರೇ ಲಕ್ಷಾಂತರ ರೂಪಾಯಿ ವೆಚ್ಚ ಭರಿಸುತ್ತಿದ್ದರು. ಈ ಸಲವೂ 7 ಮಕ್ಕಳ ತಂಡಕ್ಕೆ ಹಣದ ಕೊರತೆ ಎದುರಾಗಿತ್ತು. ಇದನ್ನು `ಪ್ರಜಾವಾಣಿ~ ಕ್ರೀಡಾ ಪುರವಣಿ ಬೆಳಕಿಗೆ ತಂದಿತ್ತು. ಈಗ ಮಲ್ಯ ಅವರು ಇದಕ್ಕೆ ಸಹಾಯಹಸ್ತ ನೀಡಿದ್ದಾರೆ. ಮಕ್ಕಳ ಕ್ರೀಡಾಕೂಟಕ್ಕೆ ಅಂತರ‌್ರಾಷ್ಟ್ರೀಯ ಒಲಿಂಪಿಕ್ ಸಮಿತಿಯ (ಐಓಸಿ) ಮಾನ್ಯತೆಯಿದೆ. 50 ದೇಶಗಳ ಸುಮಾರು 3000 ಕ್ರೀಡಾಪಟುಗಳು ಭಾಗವಹಿಸಲಿದ್ದಾರೆ. ಬೆಂಗಳೂರು ತಂಡದಲ್ಲಿ ಹೆಬ್ಬಾಳ ವಿದ್ಯಾನಿಕೇತನ ಶಾಲೆಯ ಆದಿತ್ಯ ಶರ್ಮಾ, ಹೇಮಂತ್ ಮತ್ತು ತೇಜಸ್, ಮಲ್ಯ ಅದಿತಿ ಶಾಲೆಯ ಶಿವ್, ಎಬನೇಜರ್ ಶಾಲೆಯ ಸಿದ್ದಾರ್ಥ, ನ್ಯಾಷನಲ್ ಹಿಲ್‌ವ್ಯೆ ಶಾಲೆಯ ಚಿರಾಗ್, ಗ್ರೀನ್‌ವುಡ್ ಶಾಲೆಯ ರಿಷಬ್ ಇದ್ದಾರೆ",
        "transliterated": u""
    },
    {
        "lang":  u"Tamil",
        "text": u"குழந்தை பராமரிப்பு | தினகரன் குழந்தை பராமரிப்பு குழந்தைகளின் செய்கை மொழியை எளிதில் புரிந்து கொள்ள இயலாது. அழுகையும், சிரிப்புமே குழந்தையின் அழகிய மொழிகள். அதனை உணர்ந்து குழந்தைகளை வளர்ப்பது என்பது பெற்றோருக்கே உண்டான தனிக்கலை. பச்சிளம் குழந்தைகளின் செயல்பாடுகள் புரியாமல் சில நேரங்களில் தாய்மார்கள் எரிச்சல் அடைவதும் உண்டு. இங்கு குழந்தைகளை எவ்வாறு கையாள வேண்டும். 1. குழந்தைகள் முதலில் விரும்புவது தாயின் அரவணைப்பையும், அருகாமையையும் தான். அந்த கதகதப்பு கிடைக்காத பட்சத்தில் அதற்காகவே அழுகையை தொடங்குகிறார்கள். எனவே குழந்தைகள் அழும் போது அவர்களை தூக்கி கொஞ்சினால் குழந்தைகள் உடனே அழுகையை நிறுத்திவிடுவார்கள். அந்த நேரத்தில் குழந்தைகளுக்கு உணவூட்டுதல், மசாஜ் அல்லது குளிக்க வைக்கவோ செய்யலாம். 2. குழந்தையைத் தூக்கும்போது முதுகுப் புறமாக அதிகமாகப் பிடித்துத் தூக்கக்கூடாது, அது குழந்தையின் தண்டுவடத்தைப் பாதிக்கும் என்று சிலர் சொல்வார்கள். ஆனால் உண்மையில்லை. பின்னால் பிடித்துத் தூக்குவது குழந்தையின் ரிப்ளெக்ஸ்' திறனை மேம்படுத்துகிறது. பின்புற மற்றும் கழுத்துத் தசைகளையும், தண்டுவடத்துக்குத் துணையாக உள்ள தசைகளையும் வலுப்படுத்துகிறது 3. குழந்தைக்குப் பாலூட்டும்போது அதை மார்பகத்தை நோக்கி அழுத்த வேண்டாம். அப்போது குழந்தை அதன் இயல்பின்படி தனது தலையைப் பின்னோக்கித் தள்ளும். எனவே கைகளில் லேசாக ஏந்தி அதற்கு ஏற்ற வகையில் பாலூட்டுவதே சிறப்பானது. குழந்தைகளுக்கு மூச்சுத்திணறல் ஏற்படுவதையும் தடுக்கும். ஒரு சிலர் படுத்துக் கொண்டே பாலூட்டுவார்கள். இது சில சமயங்களில் ஆபத்தை ஏற்படுத்தும். 4. இளந்தாய்மார்கள் குழந்தையை எப்படி குளிப்பாட்டுவது என்று தெரியாமல் திகைத்துப் போகிறார்கள். அந்நேரத்தில்",
        "transliterated": u""
    },
    {
        "lang":  u"Malayalam",
        "text": u"നിർമ്മിക്കുന്നതാണ്. അവ മുഴുവൻ ശരീരത്തിലെയും ഇന്ധനമായി ഉപയോഗിക്കുന്നു. മസ്തിഷ്കം പ്രവർത്തിക്കാൻ ധാരാളം ഊർജ്ജം ആവശ്യമുള്ള ഒരു അവയവമാണ്. അത് കൊഴുപ്പ് ഉപയോഗിച്ച് ഊർജ്ജം ഉപയോഗിക്കാൻ കഴിയില്ല. ഗ്ലൂക്കോസ്, കെറ്റോണി എന്നിവ മാത്രമേ മസ്തിഷ്ക പ്രവർത്തിക്കൂ. ഒരു ഭക്ഷണത്തിൽ നിങ്ങളുടെ മുഴുവൻ ശരീരം അതിന്റെ ഇന്ധന സ്രോതസ്സുകൾ പൂർണ്ണമായും കൊഴുപ്പ് പ്രവർത്തിക്കാൻ മാറുന്നു. ഇൻസുലിൻ അളവ് വളരെ താഴ്ന്നതും കൊഴുപ്പ് കത്തുന്നതുമാണ്. നിങ്ങളുടെ കൊഴുപ്പ് കടകളിൽ നിന്ന് അവരെ എരിയുന്നതിനായി എളുപ്പത്തിൽ മാറുന്നു. ശരീരഭാരം കുറയ്ക്കാൻ നിങ്ങൾ ശ്രമിക്കുകയാണെങ്കിൽ, ഇത് വളരെ മികച്ചതാണ്, കൂടാതെ ഇത് കൂടാതെ, കുറഞ്ഞ വിശപ്പ്, നിരന്തരമായ ഊർജ്ജം തുടങ്ങിയ മറ്റ് ആനുകൂല്യങ്ങളും ഉണ്ട്. ശരീരം കിറ്റോണുകൾ ഉത്പാദിപ്പിച്ചാൽ അത് കെറ്റോസിസ് ആയിരിക്കാം. വേഗത്തിൽ പോകാനുള്ള വഴി, എന്തെങ്കിലും കഴിക്കാതെ, ഉപവസിക്കുക, ഉപവസിക്കുക സാധ്യമല്ല. ഒരു ഭക്ഷണത്തിൽ, മറുവശത്ത് എപ്പോഴെങ്കിലും തിന്നു കഴിയും കൂടാതെ ഫലങ്ങൾ. നോമ്പെടുക്കലും ഇല്ലാതെ ഉപവാസത്തിൻറെ അനവധി ഗുണങ്ങളുണ്ട്. ശരീരഭാരം കുറയ്ക്കലും.",
        "transliterated": u""
    }
]


out_file = "tests/latin2dravida_test.txt"
# Save all_tokens to a text file
with open(out_file, 'w') as file:
    for j in range(len(lang_texts)):
        lang, text = lang_texts[j]["lang"], lang_texts[j]["text"]
        trans = Transliterator(lang)
        detrans = DeTransliterator(lang)
        lang_texts[j]["transliterated"] = trans.transliterate(text)
        # print(text)
        # print(replace_substrings(text, lang))
        latned = lang_texts[j]["transliterated"]
        # retext = replace_substrings(text, lang)
        retext = detrans.detransliterate(text)
        for each_line in [text, latned, retext]:
            file.write(each_line.replace("\n", "\\n") + "\n")
        file.write(str(text == retext) + "\n")

        for t in range(len(retext)):
            if text[t] != retext[t]:
                print(t, text[t], retext[t])
