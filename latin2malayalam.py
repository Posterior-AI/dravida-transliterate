#!/usr/bin/env python
# coding: utf-8

lang = [
    [u"അ", u"ആ", u"ഇ", u"ഈ", u"ഉ", u"ഊ", u"ഋ", u"ൠ", u"ഌ", u"ൡ", u"എ", u"ഏ", u"ഐ", u"ഒ", u"ഓ", u"ഔ", u"അ◌ഁ", u"അം", u"അഃ", u"-",],
    [u"ക", u"കാ", u"കി", u"കീ", u"കു", u"കൂ", u"കൃ", u"കൄ", u"കൢ", u"കൣ", u"കെ", u"കേ", u"കൈ", u"കൊ", u"കോ", u"കൗ", u"ക◌ഁ", u"കം", u"കഃ", u"ക്", u"ൿ"],
    [u"ഖ", u"ഖാ", u"ഖി", u"ഖീ", u"ഖു", u"ഖൂ", u"ഖൃ", u"ഖൄ", u"ഖൢ", u"ഖൣ", u"ഖെ", u"ഖേ", u"ഖൈ", u"ഖൊ", u"ഖോ", u"ഖൗ", u"ഖ◌ഁ", u"ഖം", u"ഖഃ", u"ഖ്", ],
    [u"ഗ", u"ഗാ", u"ഗി", u"ഗീ", u"ഗു", u"ഗൂ", u"ഗൃ", u"ഗൄ", u"ഗൢ", u"ഗൣ", u"ഗെ", u"ഗേ", u"ഗൈ", u"ഗൊ", u"ഗോ", u"ഗൗ", u"ഗ◌ഁ", u"ഗം", u"ഗഃ", u"ഗ്", ],
    [u"ഘ", u"ഘാ", u"ഘി", u"ഘീ", u"ഘു", u"ഘൂ", u"ഘൃ", u"ഘൄ", u"ഘൢ", u"ഘൣ", u"ഘെ", u"ഘേ", u"ഘൈ", u"ഘൊ", u"ഘോ", u"ഘൗ", u"ഘ◌ഁ", u"ഘം", u"ഘഃ", u"ഘ്", ],
    [u"ങ", u"ങാ", u"ങി", u"ങീ", u"ങു", u"ങൂ", u"ങൃ", u"ങൄ", u"ങൢ", u"ങൣ", u"ങെ", u"ങേ", u"ങൈ", u"ങൊ", u"ങോ", u"ങൗ", u"ങ◌ഁ", u"ങം", u"ങഃ", u"ങ്", ],
    [u"ച", u"ചാ", u"ചി", u"ചീ", u"ചു", u"ചൂ", u"ചൃ", u"ചൄ", u"ചൢ", u"ചൣ", u"ചെ", u"ചേ", u"ചൈ", u"ചൊ", u"ചോ", u"ചൗ", u"ച◌ഁ", u"ചം", u"ചഃ", u"ച്", ],
    [u"ഛ", u"ഛാ", u"ഛി", u"ഛീ", u"ഛു", u"ഛൂ", u"ഛൃ", u"ഛൄ", u"ഛൢ", u"ഛൣ", u"ഛെ", u"ഛേ", u"ഛൈ", u"ഛൊ", u"ഛോ", u"ഛൗ", u"ഛ◌ഁ", u"ഛം", u"ഛഃ", u"ഛ്", ],
    [u"ജ", u"ജാ", u"ജി", u"ജീ", u"ജു", u"ജൂ", u"ജൃ", u"ജൄ", u"ജൢ", u"ജൣ", u"ജെ", u"ജേ", u"ജൈ", u"ജൊ", u"ജോ", u"ജൗ", u"ജ◌ഁ", u"ജം", u"ജഃ", u"ജ്", ],
    [u"ഝ", u"ഝാ", u"ഝി", u"ഝീ", u"ഝു", u"ഝൂ", u"ഝൃ", u"ഝൄ", u"ഝൢ", u"ഝൣ", u"ഝെ", u"ഝേ", u"ഝൈ", u"ഝൊ", u"ഝോ", u"ഝൗ", u"ഝ◌ഁ", u"ഝം", u"ഝഃ", u"ഝ്", ],
    [u"ഞ", u"ഞാ", u"ഞി", u"ഞീ", u"ഞു", u"ഞൂ", u"ഞൃ", u"ഞൄ", u"ഞൢ", u"ഞൣ", u"ഞെ", u"ഞേ", u"ഞൈ", u"ഞൊ", u"ഞോ", u"ഞൗ", u"ഞ◌ഁ", u"ഞം", u"ഞഃ", u"ഞ്", ],
    [u"ട", u"ടാ", u"ടി", u"ടീ", u"ടു", u"ടൂ", u"ടൃ", u"ടൄ", u"ടൢ", u"ടൣ", u"ടെ", u"ടേ", u"ടൈ", u"ടൊ", u"ടോ", u"ടൗ", u"ട◌ഁ", u"ടം", u"ടഃ", u"ട്", ],
    [u"ഠ", u"ഠാ", u"ഠി", u"ഠീ", u"ഠു", u"ഠൂ", u"ഠൃ", u"ഠൄ", u"ഠൢ", u"ഠൣ", u"ഠെ", u"ഠേ", u"ഠൈ", u"ഠൊ", u"ഠോ", u"ഠൗ", u"ഠ◌ഁ", u"ഠം", u"ഠഃ", u"ഠ്", ],
    [u"ഡ", u"ഡാ", u"ഡി", u"ഡീ", u"ഡു", u"ഡൂ", u"ഡൃ", u"ഡൄ", u"ഡൢ", u"ഡൣ", u"ഡെ", u"ഡേ", u"ഡൈ", u"ഡൊ", u"ഡോ", u"ഡൗ", u"ഡ◌ഁ", u"ഡം", u"ഡഃ", u"ഡ്", ],
    [u"ഢ", u"ഢാ", u"ഢി", u"ഢീ", u"ഢു", u"ഢൂ", u"ഢൃ", u"ഢൄ", u"ഢൢ", u"ഢൣ", u"ഢെ", u"ഢേ", u"ഢൈ", u"ഢൊ", u"ഢോ", u"ഢൗ", u"ഢ◌ഁ", u"ഢം", u"ഢഃ", u"ഢ്", ],
    [u"ണ", u"ണാ", u"ണി", u"ണീ", u"ണു", u"ണൂ", u"ണൃ", u"ണൄ", u"ണൢ", u"ണൣ", u"ണെ", u"ണേ", u"ണൈ", u"ണൊ", u"ണോ", u"ണൗ", u"ണ◌ഁ", u"ണം", u"ണഃ", u"ണ്", u"ൺ ", u"ൺ.", u"ൺ?", u"ൺ ", u"ൺ!", ],
    [u"ത", u"താ", u"തി", u"തീ", u"തു", u"തൂ", u"തൃ", u"തൄ", u"തൢ", u"തൣ", u"തെ", u"തേ", u"തൈ", u"തൊ", u"തോ", u"തൗ", u"ത◌ഁ", u"തം", u"തഃ", u"ത്", ],
    [u"ഥ", u"ഥാ", u"ഥി", u"ഥീ", u"ഥു", u"ഥൂ", u"ഥൃ", u"ഥൄ", u"ഥൢ", u"ഥൣ", u"ഥെ", u"ഥേ", u"ഥൈ", u"ഥൊ", u"ഥോ", u"ഥൗ", u"ഥ◌ഁ", u"ഥം", u"ഥഃ", u"ഥ്", ],
    [u"ദ", u"ദാ", u"ദി", u"ദീ", u"ദു", u"ദൂ", u"ദൃ", u"ദൄ", u"ദൢ", u"ദൣ", u"ദെ", u"ദേ", u"ദൈ", u"ദൊ", u"ദോ", u"ദൗ", u"ദ◌ഁ", u"ദം", u"ദഃ", u"ദ്", ],
    [u"ധ", u"ധാ", u"ധി", u"ധീ", u"ധു", u"ധൂ", u"ധൃ", u"ധൄ", u"ധൢ", u"ധൣ", u"ധെ", u"ധേ", u"ധൈ", u"ധൊ", u"ധോ", u"ധൗ", u"ധ◌ഁ", u"ധം", u"ധഃ", u"ധ്", ],
    [u"ന", u"നാ", u"നി", u"നീ", u"നു", u"നൂ", u"നൃ", u"നൄ", u"നൢ", u"നൣ", u"നെ", u"നേ", u"നൈ", u"നൊ", u"നോ", u"നൗ", u"ന◌ഁ", u"നം", u"നഃ", u"ന്", u"ൻ ", u"ൻ.", u"ൻ?", u"ൻ ", u"ൻ!",],
    [u"പ", u"പാ", u"പി", u"പീ", u"പു", u"പൂ", u"പൃ", u"പൄ", u"പൢ", u"പൣ", u"പെ", u"പേ", u"പൈ", u"പൊ", u"പോ", u"പൗ", u"പ◌ഁ", u"പം", u"പഃ", u"പ്", ],
    [u"ഫ", u"ഫാ", u"ഫി", u"ഫീ", u"ഫു", u"ഫൂ", u"ഫൃ", u"ഫൄ", u"ഫൢ", u"ഫൣ", u"ഫെ", u"ഫേ", u"ഫൈ", u"ഫൊ", u"ഫോ", u"ഫൗ", u"ഫ◌ഁ", u"ഫം", u"ഫഃ", u"ഫ്", ],
    [u"ബ", u"ബാ", u"ബി", u"ബീ", u"ബു", u"ബൂ", u"ബൃ", u"ബൄ", u"ബൢ", u"ബൣ", u"ബെ", u"ബേ", u"ബൈ", u"ബൊ", u"ബോ", u"ബൗ", u"ബ◌ഁ", u"ബം", u"ബഃ", u"ബ്", ],
    [u"ഭ", u"ഭാ", u"ഭി", u"ഭീ", u"ഭു", u"ഭൂ", u"ഭൃ", u"ഭൄ", u"ഭൢ", u"ഭൣ", u"ഭെ", u"ഭേ", u"ഭൈ", u"ഭൊ", u"ഭോ", u"ഭൗ", u"ഭ◌ഁ", u"ഭം", u"ഭഃ", u"ഭ്", ],
    [u"മ", u"മാ", u"മി", u"മീ", u"മു", u"മൂ", u"മൃ", u"മൄ", u"മൢ", u"മൣ", u"മെ", u"മേ", u"മൈ", u"മൊ", u"മോ", u"മൗ", u"മ◌ഁ", u"മം", u"മഃ", u"മ്", ],
    [u"യ", u"യാ", u"യി", u"യീ", u"യു", u"യൂ", u"യൃ", u"യൄ", u"യൢ", u"യൣ", u"യെ", u"യേ", u"യൈ", u"യൊ", u"യോ", u"യൗ", u"യ◌ഁ", u"യം", u"യഃ", u"യ്", ],
    [u"ര", u"രാ", u"രി", u"രീ", u"രു", u"രൂ", u"രൃ", u"രൄ", u"രൢ", u"രൣ", u"രെ", u"രേ", u"രൈ", u"രൊ", u"രോ", u"രൗ", u"ര◌ഁ", u"രം", u"രഃ", u"ര്", ],
    [u"റ", u"റാ", u"റി", u"റീ", u"റു", u"റൂ", u"റൃ", u"റൄ", u"റൢ", u"റൣ", u"റെ", u"റേ", u"റൈ", u"റൊ", u"റോ", u"റൗ", u"റ◌ഁ", u"റം", u"റഃ", u"റ്", u"ർ ", u"ർ.", u"ർ?", u"ർ ", u"ർ!", ],
    [u"ല", u"ലാ", u"ലി", u"ലീ", u"ലു", u"ലൂ", u"ലൃ", u"ലൄ", u"ലൢ", u"ലൣ", u"ലെ", u"ലേ", u"ലൈ", u"ലൊ", u"ലോ", u"ലൗ", u"ല◌ഁ", u"ലം", u"ലഃ", u"ല്", u"ൽ ", u"ൽ.", u"ൽ?", u"ൽ ", u"ൽ!", ],
    [u"ള", u"ളാ", u"ളി", u"ളീ", u"ളു", u"ളൂ", u"ളൃ", u"ളൄ", u"ളൢ", u"ളൣ", u"ളെ", u"ളേ", u"ളൈ", u"ളൊ", u"ളോ", u"ളൗ", u"ള◌ഁ", u"ളം", u"ളഃ", u"ള്", "ൾ ", u"ൾ.", u"ൾ?", u"ൾ ", u"ൾ!",],
    [u"ഴ", u"ഴാ", u"ഴി", u"ഴീ", u"ഴു", u"ഴൂ", u"ഴൃ", u"ഴൄ", u"ഴൢ", u"ഴൣ", u"ഴെ", u"ഴേ", u"ഴൈ", u"ഴൊ", u"ഴോ", u"ഴൗ", u"ഴ◌ഁ", u"ഴം", u"ഴഃ", u"ഴ്", ],
    [u"വ", u"വാ", u"വി", u"വീ", u"വു", u"വൂ", u"വൃ", u"വൄ", u"വൢ", u"വൣ", u"വെ", u"വേ", u"വൈ", u"വൊ", u"വോ", u"വൗ", u"വ◌ഁ", u"വം", u"വഃ", u"വ്", ],
    [u"ശ", u"ശാ", u"ശി", u"ശീ", u"ശു", u"ശൂ", u"ശൃ", u"ശൄ", u"ശൢ", u"ശൣ", u"ശെ", u"ശേ", u"ശൈ", u"ശൊ", u"ശോ", u"ശൗ", u"ശ◌ഁ", u"ശം", u"ശഃ", u"ശ്", ],
    [u"ഷ", u"ഷാ", u"ഷി", u"ഷീ", u"ഷു", u"ഷൂ", u"ഷൃ", u"ഷൄ", u"ഷൢ", u"ഷൣ", u"ഷെ", u"ഷേ", u"ഷൈ", u"ഷൊ", u"ഷോ", u"ഷൗ", u"ഷ◌ഁ", u"ഷം", u"ഷഃ", u"ഷ്", ],
    [u"സ", u"സാ", u"സി", u"സീ", u"സു", u"സൂ", u"സൃ", u"സൄ", u"സൢ", u"സൣ", u"സെ", u"സേ", u"സൈ", u"സൊ", u"സോ", u"സൗ", u"സ◌ഁ", u"സം", u"സഃ", u"സ്", ],
    [u"ഹ", u"ഹാ", u"ഹി", u"ഹീ", u"ഹു", u"ഹൂ", u"ഹൃ", u"ഹൄ", u"ഹൢ", u"ഹൣ", u"ഹെ", u"ഹേ", u"ഹൈ", u"ഹൊ", u"ഹോ", u"ഹൗ", u"ഹ◌ഁ", u"ഹം", u"ഹഃ", u"ഹ്", ],    
    [u"അം", u"ആം", u"ഇം", u"ഈം", u"ഉം", u"ഊം", u"ഋം", u"ൠം", u"ഌം", u"ൡം", u"എം", u"ഏം", u"ഐം", u"ഒം", u"ഓം", u"ഔം", ],
    [u"കം", u"കാം", u"കിം", u"കീം", u"കും", u"കൂം", u"കൃം", u"കൄം", u"കൢം", u"കൣം", u"കെം", u"കേം", u"കൈം", u"കൊം", u"കോം", u"കൗം", ],
    [u"ഖം", u"ഖാം", u"ഖിം", u"ഖീം", u"ഖും", u"ഖൂം", u"ഖൃം", u"ഖൄം", u"ഖൢം", u"ഖൣം", u"ഖെം", u"ഖേം", u"ഖൈം", u"ഖൊം", u"ഖോം", u"ഖൗം", ],
    [u"ഗം", u"ഗാം", u"ഗിം", u"ഗീം", u"ഗും", u"ഗൂം", u"ഗൃം", u"ഗൄം", u"ഗൢം", u"ഗൣം", u"ഗെം", u"ഗേം", u"ഗൈം", u"ഗൊം", u"ഗോം", u"ഗൗം", ],
    [u"ഘം", u"ഘാം", u"ഘിം", u"ഘീം", u"ഘും", u"ഘൂം", u"ഘൃം", u"ഘൄം", u"ഘൢം", u"ഘൣം", u"ഘെം", u"ഘേം", u"ഘൈം", u"ഘൊം", u"ഘോം", u"ഘൗം", ],
    [u"ങം", u"ങാം", u"ങിം", u"ങീം", u"ങും", u"ങൂം", u"ങൃം", u"ങൄം", u"ങൢം", u"ങൣം", u"ങെം", u"ങേം", u"ങൈം", u"ങൊം", u"ങോം", u"ങൗം", ],
    [u"ചം", u"ചാം", u"ചിം", u"ചീം", u"ചും", u"ചൂം", u"ചൃം", u"ചൄം", u"ചൢം", u"ചൣം", u"ചെം", u"ചേം", u"ചൈം", u"ചൊം", u"ചോം", u"ചൗം", ],
    [u"ഛം", u"ഛാം", u"ഛിം", u"ഛീം", u"ഛും", u"ഛൂം", u"ഛൃം", u"ഛൄം", u"ഛൢം", u"ഛൣം", u"ഛെം", u"ഛേം", u"ഛൈം", u"ഛൊം", u"ഛോം", u"ഛൗം", ],
    [u"ജം", u"ജാം", u"ജിം", u"ജീം", u"ജും", u"ജൂം", u"ജൃം", u"ജൄം", u"ജൢം", u"ജൣം", u"ജെം", u"ജേം", u"ജൈം", u"ജൊം", u"ജോം", u"ജൗം", ],
    [u"ഝം", u"ഝാം", u"ഝിം", u"ഝീം", u"ഝും", u"ഝൂം", u"ഝൃം", u"ഝൄം", u"ഝൢം", u"ഝൣം", u"ഝെം", u"ഝേം", u"ഝൈം", u"ഝൊം", u"ഝോം", u"ഝൗം", ],
    [u"ഞം", u"ഞാം", u"ഞിം", u"ഞീം", u"ഞും", u"ഞൂം", u"ഞൃം", u"ഞൄം", u"ഞൢം", u"ഞൣം", u"ഞെം", u"ഞേം", u"ഞൈം", u"ഞൊം", u"ഞോം", u"ഞൗം", ],
    [u"ടം", u"ടാം", u"ടിം", u"ടീം", u"ടും", u"ടൂം", u"ടൃം", u"ടൄം", u"ടൢം", u"ടൣം", u"ടെം", u"ടേം", u"ടൈം", u"ടൊം", u"ടോം", u"ടൗം", ],
    [u"ഠം", u"ഠാം", u"ഠിം", u"ഠീം", u"ഠും", u"ഠൂം", u"ഠൃം", u"ഠൄം", u"ഠൢം", u"ഠൣം", u"ഠെം", u"ഠേം", u"ഠൈം", u"ഠൊം", u"ഠോം", u"ഠൗം", ],
    [u"ഡം", u"ഡാം", u"ഡിം", u"ഡീം", u"ഡും", u"ഡൂം", u"ഡൃം", u"ഡൄം", u"ഡൢം", u"ഡൣം", u"ഡെം", u"ഡേം", u"ഡൈം", u"ഡൊം", u"ഡോം", u"ഡൗം", ],
    [u"ഢം", u"ഢാം", u"ഢിം", u"ഢീം", u"ഢും", u"ഢൂം", u"ഢൃം", u"ഢൄം", u"ഢൢം", u"ഢൣം", u"ഢെം", u"ഢേം", u"ഢൈം", u"ഢൊം", u"ഢോം", u"ഢൗം", ],
    [u"ണം", u"ണാം", u"ണിം", u"ണീം", u"ണും", u"ണൂം", u"ണൃം", u"ണൄം", u"ണൢം", u"ണൣം", u"ണെം", u"ണേം", u"ണൈം", u"ണൊം", u"ണോം", u"ണൗം", ],
    [u"തം", u"താം", u"തിം", u"തീം", u"തും", u"തൂം", u"തൃം", u"തൄം", u"തൢം", u"തൣം", u"തെം", u"തേം", u"തൈം", u"തൊം", u"തോം", u"തൗം", ],
    [u"ഥം", u"ഥാം", u"ഥിം", u"ഥീം", u"ഥും", u"ഥൂം", u"ഥൃം", u"ഥൄം", u"ഥൢം", u"ഥൣം", u"ഥെം", u"ഥേം", u"ഥൈം", u"ഥൊം", u"ഥോം", u"ഥൗം", ],
    [u"ദം", u"ദാം", u"ദിം", u"ദീം", u"ദും", u"ദൂം", u"ദൃം", u"ദൄം", u"ദൢം", u"ദൣം", u"ദെം", u"ദേം", u"ദൈം", u"ദൊം", u"ദോം", u"ദൗം", ],
    [u"ധം", u"ധാം", u"ധിം", u"ധീം", u"ധും", u"ധൂം", u"ധൃം", u"ധൄം", u"ധൢം", u"ധൣം", u"ധെം", u"ധേം", u"ധൈം", u"ധൊം", u"ധോം", u"ധൗം", ],
    [u"നം", u"നാം", u"നിം", u"നീം", u"നും", u"നൂം", u"നൃം", u"നൄം", u"നൢം", u"നൣം", u"നെം", u"നേം", u"നൈം", u"നൊം", u"നോം", u"നൗം", ],
    [u"പം", u"പാം", u"പിം", u"പീം", u"പും", u"പൂം", u"പൃം", u"പൄം", u"പൢം", u"പൣം", u"പെം", u"പേം", u"പൈം", u"പൊം", u"പോം", u"പൗം", ],
    [u"ഫം", u"ഫാം", u"ഫിം", u"ഫീം", u"ഫും", u"ഫൂം", u"ഫൃം", u"ഫൄം", u"ഫൢം", u"ഫൣം", u"ഫെം", u"ഫേം", u"ഫൈം", u"ഫൊം", u"ഫോം", u"ഫൗം", ],
    [u"ബം", u"ബാം", u"ബിം", u"ബീം", u"ബും", u"ബൂം", u"ബൃം", u"ബൄം", u"ബൢം", u"ബൣം", u"ബെം", u"ബേം", u"ബൈം", u"ബൊം", u"ബോം", u"ബൗം", ],
    [u"ഭം", u"ഭാം", u"ഭിം", u"ഭീം", u"ഭും", u"ഭൂം", u"ഭൃം", u"ഭൄം", u"ഭൢം", u"ഭൣം", u"ഭെം", u"ഭേം", u"ഭൈം", u"ഭൊം", u"ഭോം", u"ഭൗം", ],
    [u"മം", u"മാം", u"മിം", u"മീം", u"മും", u"മൂം", u"മൃം", u"മൄം", u"മൢം", u"മൣം", u"മെം", u"മേം", u"മൈം", u"മൊം", u"മോം", u"മൗം", ],
    [u"യം", u"യാം", u"യിം", u"യീം", u"യും", u"യൂം", u"യൃം", u"യൄം", u"യൢം", u"യൣം", u"യെം", u"യേം", u"യൈം", u"യൊം", u"യോം", u"യൗം", ],
    [u"രം", u"രാം", u"രിം", u"രീം", u"രും", u"രൂം", u"രൃം", u"രൄം", u"രൢം", u"രൣം", u"രെം", u"രേം", u"രൈം", u"രൊം", u"രോം", u"രൗം", ],
    [u"റം", u"റാം", u"റിം", u"റീം", u"റും", u"റൂം", u"റൃം", u"റൄം", u"റൢം", u"റൣം", u"റെം", u"റേം", u"റൈം", u"റൊം", u"റോം", u"റൗം", ],
    [u"ലം", u"ലാം", u"ലിം", u"ലീം", u"ലും", u"ലൂം", u"ലൃം", u"ലൄം", u"ലൢം", u"ലൣം", u"ലെം", u"ലേം", u"ലൈം", u"ലൊം", u"ലോം", u"ലൗം", ],
    [u"ളം", u"ളാം", u"ളിം", u"ളീം", u"ളും", u"ളൂം", u"ളൃം", u"ളൄം", u"ളൢം", u"ളൣം", u"ളെം", u"ളേം", u"ളൈം", u"ളൊം", u"ളോം", u"ളൗം", ],
    [u"ഴം", u"ഴാം", u"ഴിം", u"ഴീം", u"ഴും", u"ഴൂം", u"ഴൃം", u"ഴൄം", u"ഴൢം", u"ഴൣം", u"ഴെം", u"ഴേം", u"ഴൈം", u"ഴൊം", u"ഴോം", u"ഴൗം", ],
    [u"വം", u"വാം", u"വിം", u"വീം", u"വും", u"വൂം", u"വൃം", u"വൄം", u"വൢം", u"വൣം", u"വെം", u"വേം", u"വൈം", u"വൊം", u"വോം", u"വൗം", ],
    [u"ശം", u"ശാം", u"ശിം", u"ശീം", u"ശും", u"ശൂം", u"ശൃം", u"ശൄം", u"ശൢം", u"ശൣം", u"ശെം", u"ശേം", u"ശൈം", u"ശൊം", u"ശോം", u"ശൗം", ],
    [u"ഷം", u"ഷാം", u"ഷിം", u"ഷീം", u"ഷും", u"ഷൂം", u"ഷൃം", u"ഷൄം", u"ഷൢം", u"ഷൣം", u"ഷെം", u"ഷേം", u"ഷൈം", u"ഷൊം", u"ഷോം", u"ഷൗം", ],
    [u"സം", u"സാം", u"സിം", u"സീം", u"സും", u"സൂം", u"സൃം", u"സൄം", u"സൢം", u"സൣം", u"സെം", u"സേം", u"സൈം", u"സൊം", u"സോം", u"സൗം", ],
    [u"ഹം", u"ഹാം", u"ഹിം", u"ഹീം", u"ഹും", u"ഹൂം", u"ഹൃം", u"ഹൄം", u"ഹൢം", u"ഹൣം", u"ഹെം", u"ഹേം", u"ഹൈം", u"ഹൊം", u"ഹോം", u"ഹൗം", ],
    [u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10",],
    # [u"ന്റ", ],
    # [u"ക്ക", u"ങ്ക", u"ങ്ങ", u"ച്ച", u"ഞ്ച", u"ഞ്ഞ", u"ട്ട", u"ണ്ട", u"ണ്ണ", u"ത്ത", u"ന്ത", u"ന്ന", u"പ്പ", u"മ്പ", u"മ്മ,", u"ച്ച", u"ബ്ബ", u"യ്യ", u"വ്വ", u"റ്റ", u"ന്റ",],
    [u"ക്കാ", u"ക്കി", u"ക്കീ", u"ക്കു", u"ക്കൂ", u"ക്കൃ", u"ക്കൄ", u"ക്കൢ", u"ക്കൣ", u"ക്കെ", u"ക്കേ", u"ക്കൈ", u"ക്കൊ", u"ക്കോ", u"ക്കൗ", u"ക്ക◌ഁ", u"ക്കം", u"ക്കഃ", u"ക്ക്", u"ക്ക"],
    [u"ങ്കാ", u"ങ്കി", u"ങ്കീ", u"ങ്കു", u"ങ്കൂ", u"ങ്കൃ", u"ങ്കൄ", u"ങ്കൢ", u"ങ്കൣ", u"ങ്കെ", u"ങ്കേ", u"ങ്കൈ", u"ങ്കൊ", u"ങ്കോ", u"ങ്കൗ", u"ങ്ക◌ഁ", u"ങ്കം", u"ങ്കഃ", u"ങ്ക്", u"ങ്ക"],
    [u"ങ്ങാ", u"ങ്ങി", u"ങ്ങീ", u"ങ്ങു", u"ങ്ങൂ", u"ങ്ങൃ", u"ങ്ങൄ", u"ങ്ങൢ", u"ങ്ങൣ", u"ങ്ങെ", u"ങ്ങേ", u"ങ്ങൈ", u"ങ്ങൊ", u"ങ്ങോ", u"ങ്ങൗ", u"ങ്ങ◌ഁ", u"ങ്ങം", u"ങ്ങഃ", u"ങ്ങ്", u"ങ്ങ"],
    [u"ച്ചാ", u"ച്ചി", u"ച്ചീ", u"ച്ചു", u"ച്ചൂ", u"ച്ചൃ", u"ച്ചൄ", u"ച്ചൢ", u"ച്ചൣ", u"ച്ചെ", u"ച്ചേ", u"ച്ചൈ", u"ച്ചൊ", u"ച്ചോ", u"ച്ചൗ", u"ച്ച◌ഁ", u"ച്ചം", u"ച്ചഃ", u"ച്ച്", u"ച്ച"],
    [u"ഞ്ചാ", u"ഞ്ചി", u"ഞ്ചീ", u"ഞ്ചു", u"ഞ്ചൂ", u"ഞ്ചൃ", u"ഞ്ചൄ", u"ഞ്ചൢ", u"ഞ്ചൣ", u"ഞ്ചെ", u"ഞ്ചേ", u"ഞ്ചൈ", u"ഞ്ചൊ", u"ഞ്ചോ", u"ഞ്ചൗ", u"ഞ്ച◌ഁ", u"ഞ്ചം", u"ഞ്ചഃ", u"ഞ്ച്", u"ഞ്ച"],
    [u"ഞ്ഞാ", u"ഞ്ഞി", u"ഞ്ഞീ", u"ഞ്ഞു", u"ഞ്ഞൂ", u"ഞ്ഞൃ", u"ഞ്ഞൄ", u"ഞ്ഞൢ", u"ഞ്ഞൣ", u"ഞ്ഞെ", u"ഞ്ഞേ", u"ഞ്ഞൈ", u"ഞ്ഞൊ", u"ഞ്ഞോ", u"ഞ്ഞൗ", u"ഞ്ഞ◌ഁ", u"ഞ്ഞം", u"ഞ്ഞഃ", u"ഞ്ഞ്", u"ഞ്ഞ"],
    [u"ട്ടാ", u"ട്ടി", u"ട്ടീ", u"ട്ടു", u"ട്ടൂ", u"ട്ടൃ", u"ട്ടൄ", u"ട്ടൢ", u"ട്ടൣ", u"ട്ടെ", u"ട്ടേ", u"ട്ടൈ", u"ട്ടൊ", u"ട്ടോ", u"ട്ടൗ", u"ട്ട◌ഁ", u"ട്ടം", u"ട്ടഃ", u"ട്ട്", u"ട്ട"],
    [u"ണ്ടാ", u"ണ്ടി", u"ണ്ടീ", u"ണ്ടു", u"ണ്ടൂ", u"ണ്ടൃ", u"ണ്ടൄ", u"ണ്ടൢ", u"ണ്ടൣ", u"ണ്ടെ", u"ണ്ടേ", u"ണ്ടൈ", u"ണ്ടൊ", u"ണ്ടോ", u"ണ്ടൗ", u"ണ്ട◌ഁ", u"ണ്ടം", u"ണ്ടഃ", u"ണ്ട്", u"ണ്ട"],
    [u"ണ്ണാ", u"ണ്ണി", u"ണ്ണീ", u"ണ്ണു", u"ണ്ണൂ", u"ണ്ണൃ", u"ണ്ണൄ", u"ണ്ണൢ", u"ണ്ണൣ", u"ണ്ണെ", u"ണ്ണേ", u"ണ്ണൈ", u"ണ്ണൊ", u"ണ്ണോ", u"ണ്ണൗ", u"ണ്ണ◌ഁ", u"ണ്ണം", u"ണ്ണഃ", u"ണ്ണ്", u"ണ്ണ"],
    [u"ത്താ", u"ത്തി", u"ത്തീ", u"ത്തു", u"ത്തൂ", u"ത്തൃ", u"ത്തൄ", u"ത്തൢ", u"ത്തൣ", u"ത്തെ", u"ത്തേ", u"ത്തൈ", u"ത്തൊ", u"ത്തോ", u"ത്തൗ", u"ത്ത◌ഁ", u"ത്തം", u"ത്തഃ", u"ത്ത്", u"ത്ത"],
    [u"ന്താ", u"ന്തി", u"ന്തീ", u"ന്തു", u"ന്തൂ", u"ന്തൃ", u"ന്തൄ", u"ന്തൢ", u"ന്തൣ", u"ന്തെ", u"ന്തേ", u"ന്തൈ", u"ന്തൊ", u"ന്തോ", u"ന്തൗ", u"ന്ത◌ഁ", u"ന്തം", u"ന്തഃ", u"ന്ത്", u"ന്ത"],
    [u"ന്നാ", u"ന്നി", u"ന്നീ", u"ന്നു", u"ന്നൂ", u"ന്നൃ", u"ന്നൄ", u"ന്നൢ", u"ന്നൣ", u"ന്നെ", u"ന്നേ", u"ന്നൈ", u"ന്നൊ", u"ന്നോ", u"ന്നൗ", u"ന്ന◌ഁ", u"ന്നം", u"ന്നഃ", u"ന്ന്", u"ന്ന"],
    [u"പ്പാ", u"പ്പി", u"പ്പീ", u"പ്പു", u"പ്പൂ", u"പ്പൃ", u"പ്പൄ", u"പ്പൢ", u"പ്പൣ", u"പ്പെ", u"പ്പേ", u"പ്പൈ", u"പ്പൊ", u"പ്പോ", u"പ്പൗ", u"പ്പ◌ഁ", u"പ്പം", u"പ്പഃ", u"പ്പ്", u"പ്പ"],
    [u"മ്പാ", u"മ്പി", u"മ്പീ", u"മ്പു", u"മ്പൂ", u"മ്പൃ", u"മ്പൄ", u"മ്പൢ", u"മ്പൣ", u"മ്പെ", u"മ്പേ", u"മ്പൈ", u"മ്പൊ", u"മ്പോ", u"മ്പൗ", u"മ്പ◌ഁ", u"മ്പം", u"മ്പഃ", u"മ്പ്", u"മ്പ"],
    [u"മ്മാ,", u"മ്മി", u"മ്മീ", u"മ്മു", u"മ്മൂ", u"മ്മൃ", u"മ്മൄ", u"മ്മൢ", u"മ്മൣ", u"മ്മെ", u"മ്മേ", u"മ്മൈ", u"മ്മൊ", u"മ്മോ", u"മ്മൗ", u"മ്മ◌ഁ", u"മ്മം", u"മ്മഃ", u"മ്മ്", u"മ്മ"],
    [u"ച്ചാ", u"ച്ചി", u"ച്ചീ", u"ച്ചു", u"ച്ചൂ", u"ച്ചൃ", u"ച്ചൄ", u"ച്ചൢ", u"ച്ചൣ", u"ച്ചെ", u"ച്ചേ", u"ച്ചൈ", u"ച്ചൊ", u"ച്ചോ", u"ച്ചൗ", u"ച്ച◌ഁ", u"ച്ചം", u"ച്ചഃ", u"ച്ച്", u"ച്ച"],
    [u"ബ്ബാ", u"ബ്ബി", u"ബ്ബീ", u"ബ്ബു", u"ബ്ബൂ", u"ബ്ബൃ", u"ബ്ബൄ", u"ബ്ബൢ", u"ബ്ബൣ", u"ബ്ബെ", u"ബ്ബേ", u"ബ്ബൈ", u"ബ്ബൊ", u"ബ്ബോ", u"ബ്ബൗ", u"ബ്ബ◌ഁ", u"ബ്ബം", u"ബ്ബഃ", u"ബ്ബ്", u"ബ്ബ"],
    [u"യ്യാ", u"യ്യി", u"യ്യീ", u"യ്യു", u"യ്യൂ", u"യ്യൃ", u"യ്യൄ", u"യ്യൢ", u"യ്യൣ", u"യ്യെ", u"യ്യേ", u"യ്യൈ", u"യ്യൊ", u"യ്യോ", u"യ്യൗ", u"യ്യ◌ഁ", u"യ്യം", u"യ്യഃ", u"യ്യ്", u"യ്യ"],
    [u"വ്വാ", u"വ്വി", u"വ്വീ", u"വ്വു", u"വ്വൂ", u"വ്വൃ", u"വ്വൄ", u"വ്വൢ", u"വ്വൣ", u"വ്വെ", u"വ്വേ", u"വ്വൈ", u"വ്വൊ", u"വ്വോ", u"വ്വൗ", u"വ്വ◌ഁ", u"വ്വം", u"വ്വഃ", u"വ്വ്", u"വ്വ"],
    [u"റ്റാ", u"റ്റി", u"റ്റീ", u"റ്റു", u"റ്റൂ", u"റ്റൃ", u"റ്റൄ", u"റ്റൢ", u"റ്റൣ", u"റ്റെ", u"റ്റേ", u"റ്റൈ", u"റ്റൊ", u"റ്റോ", u"റ്റൗ", u"റ്റ◌ഁ", u"റ്റം", u"റ്റഃ", u"റ്റ്", u"റ്റ"],
    [u"ന്റാ", u"ന്റി", u"ന്റീ", u"ന്റു", u"ന്റൂ", u"ന്റൃ", u"ന്റൄ", u"ന്റൢ", u"ന്റൣ", u"ന്റെ", u"ന്റേ", u"ന്റൈ", u"ന്റൊ", u"ന്റോ", u"ന്റൗ", u"ന്റ◌ഁ", u"ന്റം", u"ന്റഃ", u"ന്റ്", u"ന്റ"],
    [u"ക്കാം", u"ക്കിം", u"ക്കീം", u"ക്കും", u"ക്കൂം", u"ക്കൃം", u"ക്കൄം", u"ക്കൢം", u"ക്കൣം", u"ക്കെം", u"ക്കേം", u"ക്കൈം", u"ക്കൊം", u"ക്കോം", u"ക്കൗം", u"ക്കം"],
    [u"ങ്കാം", u"ങ്കിം", u"ങ്കീം", u"ങ്കും", u"ങ്കൂം", u"ങ്കൃം", u"ങ്കൄം", u"ങ്കൢം", u"ങ്കൣം", u"ങ്കെം", u"ങ്കേം", u"ങ്കൈം", u"ങ്കൊം", u"ങ്കോം", u"ങ്കൗം", u"ങ്കം"],
    [u"ങ്ങാം", u"ങ്ങിം", u"ങ്ങീം", u"ങ്ങും", u"ങ്ങൂം", u"ങ്ങൃം", u"ങ്ങൄം", u"ങ്ങൢം", u"ങ്ങൣം", u"ങ്ങെം", u"ങ്ങേം", u"ങ്ങൈം", u"ങ്ങൊം", u"ങ്ങോം", u"ങ്ങൗം", u"ങ്ങം"],
    [u"ച്ചാം", u"ച്ചിം", u"ച്ചീം", u"ച്ചും", u"ച്ചൂം", u"ച്ചൃം", u"ച്ചൄം", u"ച്ചൢം", u"ച്ചൣം", u"ച്ചെം", u"ച്ചേം", u"ച്ചൈം", u"ച്ചൊം", u"ച്ചോം", u"ച്ചൗം", u"ച്ചം"],
    [u"ഞ്ചാം", u"ഞ്ചിം", u"ഞ്ചീം", u"ഞ്ചും", u"ഞ്ചൂം", u"ഞ്ചൃം", u"ഞ്ചൄം", u"ഞ്ചൢം", u"ഞ്ചൣം", u"ഞ്ചെം", u"ഞ്ചേം", u"ഞ്ചൈം", u"ഞ്ചൊം", u"ഞ്ചോം", u"ഞ്ചൗം", u"ഞ്ചം"],
    [u"ഞ്ഞാം", u"ഞ്ഞിം", u"ഞ്ഞീം", u"ഞ്ഞും", u"ഞ്ഞൂം", u"ഞ്ഞൃം", u"ഞ്ഞൄം", u"ഞ്ഞൢം", u"ഞ്ഞൣം", u"ഞ്ഞെം", u"ഞ്ഞേം", u"ഞ്ഞൈം", u"ഞ്ഞൊം", u"ഞ്ഞോം", u"ഞ്ഞൗം", u"ഞ്ഞം"],
    [u"ട്ടാം", u"ട്ടിം", u"ട്ടീം", u"ട്ടും", u"ട്ടൂം", u"ട്ടൃം", u"ട്ടൄം", u"ട്ടൢം", u"ട്ടൣം", u"ട്ടെം", u"ട്ടേം", u"ട്ടൈം", u"ട്ടൊം", u"ട്ടോം", u"ട്ടൗം", u"ട്ടം"],
    [u"ണ്ടാം", u"ണ്ടിം", u"ണ്ടീം", u"ണ്ടും", u"ണ്ടൂം", u"ണ്ടൃം", u"ണ്ടൄം", u"ണ്ടൢം", u"ണ്ടൣം", u"ണ്ടെം", u"ണ്ടേം", u"ണ്ടൈം", u"ണ്ടൊം", u"ണ്ടോം", u"ണ്ടൗം", u"ണ്ടം"],
    [u"ണ്ണാം", u"ണ്ണിം", u"ണ്ണീം", u"ണ്ണും", u"ണ്ണൂം", u"ണ്ണൃം", u"ണ്ണൄം", u"ണ്ണൢം", u"ണ്ണൣം", u"ണ്ണെം", u"ണ്ണേം", u"ണ്ണൈം", u"ണ്ണൊം", u"ണ്ണോം", u"ണ്ണൗം", u"ണ്ണം"],
    [u"ത്താം", u"ത്തിം", u"ത്തീം", u"ത്തും", u"ത്തൂം", u"ത്തൃം", u"ത്തൄം", u"ത്തൢം", u"ത്തൣം", u"ത്തെം", u"ത്തേം", u"ത്തൈം", u"ത്തൊം", u"ത്തോം", u"ത്തൗം", u"ത്തം"],
    [u"ന്താം", u"ന്തിം", u"ന്തീം", u"ന്തും", u"ന്തൂം", u"ന്തൃം", u"ന്തൄം", u"ന്തൢം", u"ന്തൣം", u"ന്തെം", u"ന്തേം", u"ന്തൈം", u"ന്തൊം", u"ന്തോം", u"ന്തൗം", u"ന്തം"],
    [u"ന്നാം", u"ന്നിം", u"ന്നീം", u"ന്നും", u"ന്നൂം", u"ന്നൃം", u"ന്നൄം", u"ന്നൢം", u"ന്നൣം", u"ന്നെം", u"ന്നേം", u"ന്നൈം", u"ന്നൊം", u"ന്നോം", u"ന്നൗം", u"ന്നം"],
    [u"പ്പാം", u"പ്പിം", u"പ്പീം", u"പ്പും", u"പ്പൂം", u"പ്പൃം", u"പ്പൄം", u"പ്പൢം", u"പ്പൣം", u"പ്പെം", u"പ്പേം", u"പ്പൈം", u"പ്പൊം", u"പ്പോം", u"പ്പൗം", u"പ്പം"],
    [u"മ്പാം", u"മ്പിം", u"മ്പീം", u"മ്പും", u"മ്പൂം", u"മ്പൃം", u"മ്പൄം", u"മ്പൢം", u"മ്പൣം", u"മ്പെം", u"മ്പേം", u"മ്പൈം", u"മ്പൊം", u"മ്പോം", u"മ്പൗം", u"മ്പം"],
    [u"മ്മം", u"മ്മിം", u"മ്മീം", u"മ്മും", u"മ്മൂം", u"മ്മൃം", u"മ്മൄം", u"മ്മൢം", u"മ്മൣം", u"മ്മെം", u"മ്മേം", u"മ്മൈം", u"മ്മൊം", u"മ്മോം", u"മ്മൗം", u"മ്മം"],
    [u"ച്ചാം", u"ച്ചിം", u"ച്ചീം", u"ച്ചും", u"ച്ചൂം", u"ച്ചൃം", u"ച്ചൄം", u"ച്ചൢം", u"ച്ചൣം", u"ച്ചെം", u"ച്ചേം", u"ച്ചൈം", u"ച്ചൊം", u"ച്ചോം", u"ച്ചൗം", u"ച്ചം"],
    [u"ബ്ബാം", u"ബ്ബിം", u"ബ്ബീം", u"ബ്ബും", u"ബ്ബൂം", u"ബ്ബൃം", u"ബ്ബൄം", u"ബ്ബൢം", u"ബ്ബൣം", u"ബ്ബെം", u"ബ്ബേം", u"ബ്ബൈം", u"ബ്ബൊം", u"ബ്ബോം", u"ബ്ബൗം", u"ബ്ബം"],
    [u"യ്യാം", u"യ്യിം", u"യ്യീം", u"യ്യും", u"യ്യൂം", u"യ്യൃം", u"യ്യൄം", u"യ്യൢം", u"യ്യൣം", u"യ്യെം", u"യ്യേം", u"യ്യൈം", u"യ്യൊം", u"യ്യോം", u"യ്യൗം", u"യ്യം"],
    [u"വ്വാം", u"വ്വിം", u"വ്വീം", u"വ്വും", u"വ്വൂം", u"വ്വൃം", u"വ്വൄം", u"വ്വൢം", u"വ്വൣം", u"വ്വെം", u"വ്വേം", u"വ്വൈം", u"വ്വൊം", u"വ്വോം", u"വ്വൗം", u"വ്വം"],
    [u"റ്റാം", u"റ്റിം", u"റ്റീം", u"റ്റും", u"റ്റൂം", u"റ്റൃം", u"റ്റൄം", u"റ്റൢം", u"റ്റൣം", u"റ്റെം", u"റ്റേം", u"റ്റൈം", u"റ്റൊം", u"റ്റോം", u"റ്റൗം", u"റ്റം"],
    [u"ന്റാം", u"ന്റിം", u"ന്റീം", u"ന്റും", u"ന്റൂം", u"ന്റൃം", u"ന്റൄം", u"ന്റൢം", u"ന്റൣം", u"ന്റെം", u"ന്റേം", u"ന്റൈം", u"ന്റൊം", u"ന്റോം", u"ന്റൗം", u"ന്റം"]

]

latinized = [
    [u'a', u'ā', u'i', u'ī', u'u', u'ū', u'ṛ', u'ṝ', u'l̥', u'ḹ', u'e', u'ē', u'ai', u'o', u'ō', u'au', u'am̐', u'aṁ', u'aḥ', u'—'],
    [u'ka', u'kā', u'ki', u'kī', u'ku', u'kū', u'kṛ', u'kṝ', u'kal̥', u'kaḹ', u'ke', u'kē', u'kai', u'ko', u'kō', u'kau', u'kam̐', u'kaṁ', u'kaḥ', u'k', u'k'],
    [u'kha', u'khā', u'khi', u'khī', u'khu', u'khū', u'khṛ', u'khṝ', u'khal̥', u'khaḹ', u'khe', u'khē', u'khai', u'kho', u'khō', u'khau', u'kham̐', u'khaṁ', u'khaḥ', u'kh'],
    [u'ga', u'gā', u'gi', u'gī', u'gu', u'gū', u'gṛ', u'gṝ', u'gal̥', u'gaḹ', u'ge', u'gē', u'gai', u'go', u'gō', u'gau', u'gam̐', u'gaṁ', u'gaḥ', u'g'],
    [u'gha', u'ghā', u'ghi', u'ghī', u'ghu', u'ghū', u'ghṛ', u'ghṝ', u'ghal̥', u'ghaḹ', u'ghe', u'ghē', u'ghai', u'gho', u'ghō', u'ghau', u'gham̐', u'ghaṁ', u'ghaḥ', u'gh'],
    [u'ṅa', u'ṅā', u'ṅi', u'ṅī', u'ṅu', u'ṅū', u'ṅṛ', u'ṅṝ', u'ṅal̥', u'ṅaḹ', u'ṅe', u'ṅē', u'ṅai', u'ṅo', u'ṅō', u'ṅau', u'ṅam̐', u'ṅaṁ', u'ṅaḥ', u'ṅ'],
    [u'ca', u'cā', u'ci', u'cī', u'cu', u'cū', u'cṛ', u'cṝ', u'cal̥', u'caḹ', u'ce', u'cē', u'cai', u'co', u'cō', u'cau', u'cam̐', u'caṁ', u'caḥ', u'c'],
    [u'cha', u'chā', u'chi', u'chī', u'chu', u'chū', u'chṛ', u'chṝ', u'chal̥', u'chaḹ', u'che', u'chē', u'chai', u'cho', u'chō', u'chau', u'cham̐', u'chaṁ', u'chaḥ', u'ch'],
    [u'ja', u'jā', u'ji', u'jī', u'ju', u'jū', u'jṛ', u'jṝ', u'jal̥', u'jaḹ', u'je', u'jē', u'jai', u'jo', u'jō', u'jau', u'jam̐', u'jaṁ', u'jaḥ', u'j'],
    [u'jha', u'jhā', u'jhi', u'jhī', u'jhu', u'jhū', u'jhṛ', u'jhṝ', u'jhal̥', u'jhaḹ', u'jhe', u'jhē', u'jhai', u'jho', u'jhō', u'jhau', u'jham̐', u'jhaṁ', u'jhaḥ', u'jh'],
    [u'ña', u'ñā', u'ñi', u'ñī', u'ñu', u'ñū', u'ñṛ', u'ñṝ', u'ñal̥', u'ñaḹ', u'ñe', u'ñē', u'ñai', u'ño', u'ñō', u'ñau', u'ñam̐', u'ñaṁ', u'ñaḥ', u'ñ'],
    [u'ṭa', u'ṭā', u'ṭi', u'ṭī', u'ṭu', u'ṭū', u'ṭṛ', u'ṭṝ', u'ṭal̥', u'ṭaḹ', u'ṭe', u'ṭē', u'ṭai', u'ṭo', u'ṭō', u'ṭau', u'ṭam̐', u'ṭaṁ', u'ṭaḥ', u'ṭ'],
    [u'ṭha', u'ṭhā', u'ṭhi', u'ṭhī', u'ṭhu', u'ṭhū', u'ṭhṛ', u'ṭhṝ', u'ṭhal̥', u'ṭhaḹ', u'ṭhe', u'ṭhē', u'ṭhai', u'ṭho', u'ṭhō', u'ṭhau', u'ṭham̐', u'ṭhaṁ', u'ṭhaḥ', u'ṭh'],
    [u'ḍa', u'ḍā', u'ḍi', u'ḍī', u'ḍu', u'ḍū', u'ḍṛ', u'ḍṝ', u'ḍal̥', u'ḍaḹ', u'ḍe', u'ḍē', u'ḍai', u'ḍo', u'ḍō', u'ḍau', u'ḍam̐', u'ḍaṁ', u'ḍaḥ', u'ḍ'],
    [u'ḍha', u'ḍhā', u'ḍhi', u'ḍhī', u'ḍhu', u'ḍhū', u'ḍhṛ', u'ḍhṝ', u'ḍhal̥', u'ḍhaḹ', u'ḍhe', u'ḍhē', u'ḍhai', u'ḍho', u'ḍhō', u'ḍhau', u'ḍham̐', u'ḍhaṁ', u'ḍhaḥ', u'ḍh'],
    [u'ṇa', u'ṇā', u'ṇi', u'ṇī', u'ṇu', u'ṇū', u'ṇṛ', u'ṇṝ', u'ṇal̥', u'ṇaḹ', u'ṇe', u'ṇē', u'ṇai', u'ṇo', u'ṇō', u'ṇau', u'ṇam̐', u'ṇaṁ', u'ṇaḥ', u'ṇ', u'ṇ ', u"ṇ.", u"ṇ?", u"ṇ ", u"ṇ!",],
    [u'ta', u'tā', u'ti', u'tī', u'tu', u'tū', u'tṛ', u'tṝ', u'tal̥', u'taḹ', u'te', u'tē', u'tai', u'to', u'tō', u'tau', u'tam̐', u'taṁ', u'taḥ', u't'],
    [u'tha', u'thā', u'thi', u'thī', u'thu', u'thū', u'thṛ', u'thṝ', u'thal̥', u'thaḹ', u'the', u'thē', u'thai', u'tho', u'thō', u'thau', u'tham̐', u'thaṁ', u'thaḥ', u'th'],
    [u'da', u'dā', u'di', u'dī', u'du', u'dū', u'dṛ', u'dṝ', u'dal̥', u'daḹ', u'de', u'dē', u'dai', u'do', u'dō', u'dau', u'dam̐', u'daṁ', u'daḥ', u'd'],
    [u'dha', u'dhā', u'dhi', u'dhī', u'dhu', u'dhū', u'dhṛ', u'dhṝ', u'dhal̥', u'dhaḹ', u'dhe', u'dhē', u'dhai', u'dho', u'dhō', u'dhau', u'dham̐', u'dhaṁ', u'dhaḥ', u'dh'],
    [u'na', u'nā', u'ni', u'nī', u'nu', u'nū', u'nṛ', u'nṝ', u'nal̥', u'naḹ', u'ne', u'nē', u'nai', u'no', u'nō', u'nau', u'nam̐', u'naṁ', u'naḥ', u'n', u'n ', u"n.", u"n?", u"n ", u"n!",],
    [u'pa', u'pā', u'pi', u'pī', u'pu', u'pū', u'pṛ', u'pṝ', u'pal̥', u'paḹ', u'pe', u'pē', u'pai', u'po', u'pō', u'pau', u'pam̐', u'paṁ', u'paḥ', u'p'],
    [u'pha', u'phā', u'phi', u'phī', u'phu', u'phū', u'phṛ', u'phṝ', u'phal̥', u'phaḹ', u'phe', u'phē', u'phai', u'pho', u'phō', u'phau', u'pham̐', u'phaṁ', u'phaḥ', u'ph'],
    [u'ba', u'bā', u'bi', u'bī', u'bu', u'bū', u'bṛ', u'bṝ', u'bal̥', u'baḹ', u'be', u'bē', u'bai', u'bo', u'bō', u'bau', u'bam̐', u'baṁ', u'baḥ', u'b'],
    [u'bha', u'bhā', u'bhi', u'bhī', u'bhu', u'bhū', u'bhṛ', u'bhṝ', u'bhal̥', u'bhaḹ', u'bhe', u'bhē', u'bhai', u'bho', u'bhō', u'bhau', u'bham̐', u'bhaṁ', u'bhaḥ', u'bh'],
    [u'ma', u'mā', u'mi', u'mī', u'mu', u'mū', u'mṛ', u'mṝ', u'mal̥', u'maḹ', u'me', u'mē', u'mai', u'mo', u'mō', u'mau', u'mam̐', u'maṁ', u'maḥ', u'm'],
    [u'ya', u'yā', u'yi', u'yī', u'yu', u'yū', u'yṛ', u'yṝ', u'yal̥', u'yaḹ', u'ye', u'yē', u'yai', u'yo', u'yō', u'yau', u'yam̐', u'yaṁ', u'yaḥ', u'y'],
    [u'ra', u'rā', u'ri', u'rī', u'ru', u'rū', u'rṛ', u'rṝ', u'ral̥', u'raḹ', u're', u'rē', u'rai', u'ro', u'rō', u'rau', u'ram̐', u'raṁ', u'raḥ', u'r'],
    [u'ṟa', u'ṟā', u'ṟi', u'ṟī', u'ṟu', u'ṟū', u'ṟṛ', u'ṟṝ', u'ṟal̥', u'ṟaḹ', u'ṟe', u'ṟē', u'ṟai', u'ṟo', u'ṟō', u'ṟau', u'ṟam̐', u'ṟaṁ', u'ṟaḥ', u'ṟ', u'ṟ ', u"ṟ.", u"ṟ?", u"ṟ ", u"ṟ!",],
    [u'la', u'lā', u'li', u'lī', u'lu', u'lū', u'lṛ', u'lṝ', u'lal̥', u'laḹ', u'le', u'lē', u'lai', u'lo', u'lō', u'lau', u'lam̐', u'laṁ', u'laḥ', u'l', u'l ', u"l.", u"l?", u"l ", u"l!",],
    [u'ḷa', u'ḷā', u'ḷi', u'ḷī', u'ḷu', u'ḷū', u'ḷṛ', u'ḷṝ', u'ḷal̥', u'ḷaḹ', u'ḷe', u'ḷē', u'ḷai', u'ḷo', u'ḷō', u'ḷau', u'ḷam̐', u'ḷaṁ', u'ḷaḥ', u'ḷ', u'ḷ ', u"ḷ.", u"ḷ?", u"ḷ ", u"ḷ!",],
    [u'ḻa', u'ḻā', u'ḻi', u'ḻī', u'ḻu', u'ḻū', u'ḻṛ', u'ḻṝ', u'ḻal̥', u'ḻaḹ', u'ḻe', u'ḻē', u'ḻai', u'ḻo', u'ḻō', u'ḻau', u'ḻam̐', u'ḻaṁ', u'ḻaḥ', u'ḻ'],    
    [u'va', u'vā', u'vi', u'vī', u'vu', u'vū', u'vṛ', u'vṝ', u'val̥', u'vaḹ', u've', u'vē', u'vai', u'vo', u'vō', u'vau', u'vam̐', u'vaṁ', u'vaḥ', u'v'],
    [u'śa', u'śā', u'śi', u'śī', u'śu', u'śū', u'śṛ', u'śṝ', u'śal̥', u'śaḹ', u'śe', u'śē', u'śai', u'śo', u'śō', u'śau', u'śam̐', u'śaṁ', u'śaḥ', u'ś'],
    [u'ṣa', u'ṣā', u'ṣi', u'ṣī', u'ṣu', u'ṣū', u'ṣṛ', u'ṣṝ', u'ṣal̥', u'ṣaḹ', u'ṣe', u'ṣē', u'ṣai', u'ṣo', u'ṣō', u'ṣau', u'ṣam̐', u'ṣaṁ', u'ṣaḥ', u'ṣ'],
    [u'sa', u'sā', u'si', u'sī', u'su', u'sū', u'sṛ', u'sṝ', u'sal̥', u'saḹ', u'se', u'sē', u'sai', u'so', u'sō', u'sau', u'sam̐', u'saṁ', u'saḥ', u's'],
    [u'ha', u'hā', u'hi', u'hī', u'hu', u'hū', u'hṛ', u'hṝ', u'hal̥', u'haḹ', u'he', u'hē', u'hai', u'ho', u'hō', u'hau', u'ham̐', u'haṁ', u'haḥ', u'h'],
    # [u'fa', u'fā', u'fi', u'fī', u'fu', u'fū', u'fṛ', u'fṝ', u'fal̥', u'faḹ', u'fe', u'fē', u'fai', u'fo', u'fō', u'fau', u'fam̐', u'faṁ', u'faḥ', u'f'],
    [u'aṁ', u'āṁ', u'iṁ', u'īṁ', u'uṁ', u'ūṁ', u'ṛṁ', u'ṝṁ', u'l̥ṁ', u'ḹṁ', u'eṁ', u'ēṁ', u'aiṁ', u'oṁ', u'ōṁ', u'auṁ'],
    [u'kaṁ', u'kāṁ', u'kiṁ', u'kīṁ', u'kuṁ', u'kūṁ', u'kṛṁ', u'kṝṁ', u'kal̥ṁ', u'kaḹṁ', u'keṁ', u'kēṁ', u'kaiṁ', u'koṁ', u'kōṁ', u'kauṁ'],
    [u'khaṁ', u'khāṁ', u'khiṁ', u'khīṁ', u'khuṁ', u'khūṁ', u'khṛṁ', u'khṝṁ', u'khal̥ṁ', u'khaḹṁ', u'kheṁ', u'khēṁ', u'khaiṁ', u'khoṁ', u'khōṁ', u'khauṁ'],
    [u'gaṁ', u'gāṁ', u'giṁ', u'gīṁ', u'guṁ', u'gūṁ', u'gṛṁ', u'gṝṁ', u'gal̥ṁ', u'gaḹṁ', u'geṁ', u'gēṁ', u'gaiṁ', u'goṁ', u'gōṁ', u'gauṁ'],
    [u'ghaṁ', u'ghāṁ', u'ghiṁ', u'ghīṁ', u'ghuṁ', u'ghūṁ', u'ghṛṁ', u'ghṝṁ', u'ghal̥ṁ', u'ghaḹṁ', u'gheṁ', u'ghēṁ', u'ghaiṁ', u'ghoṁ', u'ghōṁ', u'ghauṁ'],
    [u'ṅaṁ', u'ṅāṁ', u'ṅiṁ', u'ṅīṁ', u'ṅuṁ', u'ṅūṁ', u'ṅṛṁ', u'ṅṝṁ', u'ṅal̥ṁ', u'ṅaḹṁ', u'ṅeṁ', u'ṅēṁ', u'ṅaiṁ', u'ṅoṁ', u'ṅōṁ', u'ṅauṁ'],
    [u'caṁ', u'cāṁ', u'ciṁ', u'cīṁ', u'cuṁ', u'cūṁ', u'cṛṁ', u'cṝṁ', u'cal̥ṁ', u'caḹṁ', u'ceṁ', u'cēṁ', u'caiṁ', u'coṁ', u'cōṁ', u'cauṁ'],
    [u'chaṁ', u'chāṁ', u'chiṁ', u'chīṁ', u'chuṁ', u'chūṁ', u'chṛṁ', u'chṝṁ', u'chal̥ṁ', u'chaḹṁ', u'cheṁ', u'chēṁ', u'chaiṁ', u'choṁ', u'chōṁ', u'chauṁ'],
    [u'jaṁ', u'jāṁ', u'jiṁ', u'jīṁ', u'juṁ', u'jūṁ', u'jṛṁ', u'jṝṁ', u'jal̥ṁ', u'jaḹṁ', u'jeṁ', u'jēṁ', u'jaiṁ', u'joṁ', u'jōṁ', u'jauṁ'],
    [u'jhaṁ', u'jhāṁ', u'jhiṁ', u'jhīṁ', u'jhuṁ', u'jhūṁ', u'jhṛṁ', u'jhṝṁ', u'jhal̥ṁ', u'jhaḹṁ', u'jheṁ', u'jhēṁ', u'jhaiṁ', u'jhoṁ', u'jhōṁ', u'jhauṁ'],
    [u'ñaṁ', u'ñāṁ', u'ñiṁ', u'ñīṁ', u'ñuṁ', u'ñūṁ', u'ñṛṁ', u'ñṝṁ', u'ñal̥ṁ', u'ñaḹṁ', u'ñeṁ', u'ñēṁ', u'ñaiṁ', u'ñoṁ', u'ñōṁ', u'ñauṁ'],
    [u'ṭaṁ', u'ṭāṁ', u'ṭiṁ', u'ṭīṁ', u'ṭuṁ', u'ṭūṁ', u'ṭṛṁ', u'ṭṝṁ', u'ṭal̥ṁ', u'ṭaḹṁ', u'ṭeṁ', u'ṭēṁ', u'ṭaiṁ', u'ṭoṁ', u'ṭōṁ', u'ṭauṁ'],
    [u'ṭhaṁ', u'ṭhāṁ', u'ṭhiṁ', u'ṭhīṁ', u'ṭhuṁ', u'ṭhūṁ', u'ṭhṛṁ', u'ṭhṝṁ', u'ṭhal̥ṁ', u'ṭhaḹṁ', u'ṭheṁ', u'ṭhēṁ', u'ṭhaiṁ', u'ṭhoṁ', u'ṭhōṁ', u'ṭhauṁ'],
    [u'ḍaṁ', u'ḍāṁ', u'ḍiṁ', u'ḍīṁ', u'ḍuṁ', u'ḍūṁ', u'ḍṛṁ', u'ḍṝṁ', u'ḍal̥ṁ', u'ḍaḹṁ', u'ḍeṁ', u'ḍēṁ', u'ḍaiṁ', u'ḍoṁ', u'ḍōṁ', u'ḍauṁ'],
    [u'ḍhaṁ', u'ḍhāṁ', u'ḍhiṁ', u'ḍhīṁ', u'ḍhuṁ', u'ḍhūṁ', u'ḍhṛṁ', u'ḍhṝṁ', u'ḍhal̥ṁ', u'ḍhaḹṁ', u'ḍheṁ', u'ḍhēṁ', u'ḍhaiṁ', u'ḍhoṁ', u'ḍhōṁ', u'ḍhauṁ'],
    [u'ṇaṁ', u'ṇāṁ', u'ṇiṁ', u'ṇīṁ', u'ṇuṁ', u'ṇūṁ', u'ṇṛṁ', u'ṇṝṁ', u'ṇal̥ṁ', u'ṇaḹṁ', u'ṇeṁ', u'ṇēṁ', u'ṇaiṁ', u'ṇoṁ', u'ṇōṁ', u'ṇauṁ'],
    [u'taṁ', u'tāṁ', u'tiṁ', u'tīṁ', u'tuṁ', u'tūṁ', u'tṛṁ', u'tṝṁ', u'tal̥ṁ', u'taḹṁ', u'teṁ', u'tēṁ', u'taiṁ', u'toṁ', u'tōṁ', u'tauṁ'],
    [u'thaṁ', u'thāṁ', u'thiṁ', u'thīṁ', u'thuṁ', u'thūṁ', u'thṛṁ', u'thṝṁ', u'thal̥ṁ', u'thaḹṁ', u'theṁ', u'thēṁ', u'thaiṁ', u'thoṁ', u'thōṁ', u'thauṁ'],
    [u'daṁ', u'dāṁ', u'diṁ', u'dīṁ', u'duṁ', u'dūṁ', u'dṛṁ', u'dṝṁ', u'dal̥ṁ', u'daḹṁ', u'deṁ', u'dēṁ', u'daiṁ', u'doṁ', u'dōṁ', u'dauṁ'],
    [u'dhaṁ', u'dhāṁ', u'dhiṁ', u'dhīṁ', u'dhuṁ', u'dhūṁ', u'dhṛṁ', u'dhṝṁ', u'dhal̥ṁ', u'dhaḹṁ', u'dheṁ', u'dhēṁ', u'dhaiṁ', u'dhoṁ', u'dhōṁ', u'dhauṁ'],
    [u'naṁ', u'nāṁ', u'niṁ', u'nīṁ', u'nuṁ', u'nūṁ', u'nṛṁ', u'nṝṁ', u'nal̥ṁ', u'naḹṁ', u'neṁ', u'nēṁ', u'naiṁ', u'noṁ', u'nōṁ', u'nauṁ'],
    [u'paṁ', u'pāṁ', u'piṁ', u'pīṁ', u'puṁ', u'pūṁ', u'pṛṁ', u'pṝṁ', u'pal̥ṁ', u'paḹṁ', u'peṁ', u'pēṁ', u'paiṁ', u'poṁ', u'pōṁ', u'pauṁ'],
    [u'phaṁ', u'phāṁ', u'phiṁ', u'phīṁ', u'phuṁ', u'phūṁ', u'phṛṁ', u'phṝṁ', u'phal̥ṁ', u'phaḹṁ', u'pheṁ', u'phēṁ', u'phaiṁ', u'phoṁ', u'phōṁ', u'phauṁ'],
    [u'baṁ', u'bāṁ', u'biṁ', u'bīṁ', u'buṁ', u'būṁ', u'bṛṁ', u'bṝṁ', u'bal̥ṁ', u'baḹṁ', u'beṁ', u'bēṁ', u'baiṁ', u'boṁ', u'bōṁ', u'bauṁ'],
    [u'bhaṁ', u'bhāṁ', u'bhiṁ', u'bhīṁ', u'bhuṁ', u'bhūṁ', u'bhṛṁ', u'bhṝṁ', u'bhal̥ṁ', u'bhaḹṁ', u'bheṁ', u'bhēṁ', u'bhaiṁ', u'bhoṁ', u'bhōṁ', u'bhauṁ'],
    [u'maṁ', u'māṁ', u'miṁ', u'mīṁ', u'muṁ', u'mūṁ', u'mṛṁ', u'mṝṁ', u'mal̥ṁ', u'maḹṁ', u'meṁ', u'mēṁ', u'maiṁ', u'moṁ', u'mōṁ', u'mauṁ'],
    [u'yaṁ', u'yāṁ', u'yiṁ', u'yīṁ', u'yuṁ', u'yūṁ', u'yṛṁ', u'yṝṁ', u'yal̥ṁ', u'yaḹṁ', u'yeṁ', u'yēṁ', u'yaiṁ', u'yoṁ', u'yōṁ', u'yauṁ'],
    [u'raṁ', u'rāṁ', u'riṁ', u'rīṁ', u'ruṁ', u'rūṁ', u'rṛṁ', u'rṝṁ', u'ral̥ṁ', u'raḹṁ', u'reṁ', u'rēṁ', u'raiṁ', u'roṁ', u'rōṁ', u'rauṁ'],
    [u'ṟaṁ', u'ṟāṁ', u'ṟiṁ', u'ṟīṁ', u'ṟuṁ', u'ṟūṁ', u'ṟṛṁ', u'ṟṝṁ', u'ṟal̥ṁ', u'ṟaḹṁ', u'ṟeṁ', u'ṟēṁ', u'ṟaiṁ', u'ṟoṁ', u'ṟōṁ', u'ṟauṁ'],
    [u'laṁ', u'lāṁ', u'liṁ', u'līṁ', u'luṁ', u'lūṁ', u'lṛṁ', u'lṝṁ', u'lal̥ṁ', u'laḹṁ', u'leṁ', u'lēṁ', u'laiṁ', u'loṁ', u'lōṁ', u'lauṁ'],
    [u'ḷaṁ', u'ḷāṁ', u'ḷiṁ', u'ḷīṁ', u'ḷuṁ', u'ḷūṁ', u'ḷṛṁ', u'ḷṝṁ', u'ḷal̥ṁ', u'ḷaḹṁ', u'ḷeṁ', u'ḷēṁ', u'ḷaiṁ', u'ḷoṁ', u'ḷōṁ', u'ḷauṁ'],
    [u'ḻaṁ', u'ḻāṁ', u'ḻiṁ', u'ḻīṁ', u'ḻuṁ', u'ḻūṁ', u'ḻṛṁ', u'ḻṝṁ', u'ḻal̥ṁ', u'ḻaḹṁ', u'ḻeṁ', u'ḻēṁ', u'ḻaiṁ', u'ḻoṁ', u'ḻōṁ', u'ḻauṁ'],
    [u'vaṁ', u'vāṁ', u'viṁ', u'vīṁ', u'vuṁ', u'vūṁ', u'vṛṁ', u'vṝṁ', u'val̥ṁ', u'vaḹṁ', u'veṁ', u'vēṁ', u'vaiṁ', u'voṁ', u'vōṁ', u'vauṁ'],
    [u'śaṁ', u'śāṁ', u'śiṁ', u'śīṁ', u'śuṁ', u'śūṁ', u'śṛṁ', u'śṝṁ', u'śal̥ṁ', u'śaḹṁ', u'śeṁ', u'śēṁ', u'śaiṁ', u'śoṁ', u'śōṁ', u'śauṁ'],
    [u'ṣaṁ', u'ṣāṁ', u'ṣiṁ', u'ṣīṁ', u'ṣuṁ', u'ṣūṁ', u'ṣṛṁ', u'ṣṝṁ', u'ṣal̥ṁ', u'ṣaḹṁ', u'ṣeṁ', u'ṣēṁ', u'ṣaiṁ', u'ṣoṁ', u'ṣōṁ', u'ṣauṁ'],
    [u'saṁ', u'sāṁ', u'siṁ', u'sīṁ', u'suṁ', u'sūṁ', u'sṛṁ', u'sṝṁ', u'sal̥ṁ', u'saḹṁ', u'seṁ', u'sēṁ', u'saiṁ', u'soṁ', u'sōṁ', u'sauṁ'],
    [u'haṁ', u'hāṁ', u'hiṁ', u'hīṁ', u'huṁ', u'hūṁ', u'hṛṁ', u'hṝṁ', u'hal̥ṁ', u'haḹṁ', u'heṁ', u'hēṁ', u'haiṁ', u'hoṁ', u'hōṁ', u'hauṁ'],
    # [u'faṁ', u'fāṁ', u'fiṁ', u'fīṁ', u'fuṁ', u'fūṁ', u'fṛṁ', u'fṝṁ', u'fal̥ṁ', u'faḹṁ', u'feṁ', u'fēṁ', u'faiṁ', u'foṁ', u'fōṁ', u'fauṁ'],
    [u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10",],
    # [u"kka", u"ṅka", u"ṅṅa", u"cca", u"ñca", u"ñña", u"ṭṭa", u"ṇṭa", u"ṇṇa", u"tta", u"nta", u"nna", u"ppa", u"mpa", u"mma,", u"cca", u"bba", u"yya", u"vva,", u"ṯṯa", u"nṯa"],
    [u'kkā', u'kki', u'kkī', u'kku', u'kkū', u'kkṛ', u'kkṝ', u'kkal̥', u'kkaḹ', u'kke', u'kkē', u'kkhai', u'kko', u'kkō', u'kkau', u'kkam̐', u'kkaṁ', u'kkaḥ', u'kk' , u'kka'],
    [u'ṅkā', u'ṅki', u'ṅkī', u'ṅku', u'ṅkū', u'ṅkṛ', u'ṅkṝ', u'ṅkal̥', u'ṅkaḹ', u'ṅke', u'ṅkē', u'ṅkhai', u'ṅko', u'ṅkō', u'ṅkau', u'ṅkam̐', u'ṅkaṁ', u'ṅkaḥ', u'ṅk' , u'ṅka'],
    [u'ṅṅā', u'ṅṅi', u'ṅṅī', u'ṅṅu', u'ṅṅū', u'ṅṅṛ', u'ṅṅṝ', u'ṅṅal̥', u'ṅṅaḹ', u'ṅṅe', u'ṅṅē', u'ṅṅhai', u'ṅṅo', u'ṅṅō', u'ṅṅau', u'ṅṅam̐', u'ṅṅaṁ', u'ṅṅaḥ', u'ṅṅ' , u'ṅṅa'],
    [u'ccā', u'cci', u'ccī', u'ccu', u'ccū', u'ccṛ', u'ccṝ', u'ccal̥', u'ccaḹ', u'cce', u'ccē', u'cchai', u'cco', u'ccō', u'ccau', u'ccam̐', u'ccaṁ', u'ccaḥ', u'cc' , u'cca'],
    [u'ñcā', u'ñci', u'ñcī', u'ñcu', u'ñcū', u'ñcṛ', u'ñcṝ', u'ñcal̥', u'ñcaḹ', u'ñce', u'ñcē', u'ñchai', u'ñco', u'ñcō', u'ñcau', u'ñcam̐', u'ñcaṁ', u'ñcaḥ', u'ñc' , u'ñca'],
    [u'ññā', u'ññi', u'ññī', u'ññu', u'ññū', u'ññṛ', u'ññṝ', u'ññal̥', u'ññaḹ', u'ññe', u'ññē', u'ññhai', u'ñño', u'ññō', u'ññau', u'ññam̐', u'ññaṁ', u'ññaḥ', u'ññ' , u'ñña'],
    [u'ṭṭā', u'ṭṭi', u'ṭṭī', u'ṭṭu', u'ṭṭū', u'ṭṭṛ', u'ṭṭṝ', u'ṭṭal̥', u'ṭṭaḹ', u'ṭṭe', u'ṭṭē', u'ṭṭhai', u'ṭṭo', u'ṭṭō', u'ṭṭau', u'ṭṭam̐', u'ṭṭaṁ', u'ṭṭaḥ', u'ṭṭ' , u'ṭṭa'],
    [u'ṇṭā', u'ṇṭi', u'ṇṭī', u'ṇṭu', u'ṇṭū', u'ṇṭṛ', u'ṇṭṝ', u'ṇṭal̥', u'ṇṭaḹ', u'ṇṭe', u'ṇṭē', u'ṇṭhai', u'ṇṭo', u'ṇṭō', u'ṇṭau', u'ṇṭam̐', u'ṇṭaṁ', u'ṇṭaḥ', u'ṇṭ' , u'ṇṭa'],
    [u'ṇṇā', u'ṇṇi', u'ṇṇī', u'ṇṇu', u'ṇṇū', u'ṇṇṛ', u'ṇṇṝ', u'ṇṇal̥', u'ṇṇaḹ', u'ṇṇe', u'ṇṇē', u'ṇṇhai', u'ṇṇo', u'ṇṇō', u'ṇṇau', u'ṇṇam̐', u'ṇṇaṁ', u'ṇṇaḥ', u'ṇṇ' , u'ṇṇa'],
    [u'ttā', u'tti', u'ttī', u'ttu', u'ttū', u'ttṛ', u'ttṝ', u'ttal̥', u'ttaḹ', u'tte', u'ttē', u'tthai', u'tto', u'ttō', u'ttau', u'ttam̐', u'ttaṁ', u'ttaḥ', u'tt' , u'tta'],
    [u'ntā', u'nti', u'ntī', u'ntu', u'ntū', u'ntṛ', u'ntṝ', u'ntal̥', u'ntaḹ', u'nte', u'ntē', u'nthai', u'nto', u'ntō', u'ntau', u'ntam̐', u'ntaṁ', u'ntaḥ', u'nt' , u'nta'],
    [u'nnā', u'nni', u'nnī', u'nnu', u'nnū', u'nnṛ', u'nnṝ', u'nnal̥', u'nnaḹ', u'nne', u'nnē', u'nnhai', u'nno', u'nnō', u'nnau', u'nnam̐', u'nnaṁ', u'nnaḥ', u'nn' , u'nna'],
    [u'ppā', u'ppi', u'ppī', u'ppu', u'ppū', u'ppṛ', u'ppṝ', u'ppal̥', u'ppaḹ', u'ppe', u'ppē', u'pphai', u'ppo', u'ppō', u'ppau', u'ppam̐', u'ppaṁ', u'ppaḥ', u'pp' , u'ppa'],
    [u'mpā', u'mpi', u'mpī', u'mpu', u'mpū', u'mpṛ', u'mpṝ', u'mpal̥', u'mpaḹ', u'mpe', u'mpē', u'mphai', u'mpo', u'mpō', u'mpau', u'mpam̐', u'mpaṁ', u'mpaḥ', u'mp' , u'mpa'],
    [u'mmā', u'mmi', u'mmī', u'mmu', u'mmū', u'mmṛ', u'mmṝ', u'mmal̥', u'mmaḹ', u'mme', u'mmē', u'mmhai', u'mmo', u'mmō', u'mmau', u'mmam̐', u'mmaṁ', u'mmaḥ', u'mm' , u'mma'],
    [u'ccā', u'cci', u'ccī', u'ccu', u'ccū', u'ccṛ', u'ccṝ', u'ccal̥', u'ccaḹ', u'cce', u'ccē', u'cchai', u'cco', u'ccō', u'ccau', u'ccam̐', u'ccaṁ', u'ccaḥ', u'cc' , u'cca'],
    [u'bbā', u'bbi', u'bbī', u'bbu', u'bbū', u'bbṛ', u'bbṝ', u'bbal̥', u'bbaḹ', u'bbe', u'bbē', u'bbhai', u'bbo', u'bbō', u'bbau', u'bbam̐', u'bbaṁ', u'bbaḥ', u'bb' , u'bba'],
    [u'yyā', u'yyi', u'yyī', u'yyu', u'yyū', u'yyṛ', u'yyṝ', u'yyal̥', u'yyaḹ', u'yye', u'yyē', u'yyhai', u'yyo', u'yyō', u'yyau', u'yyam̐', u'yyaṁ', u'yyaḥ', u'yy' , u'yya'],
    [u'vvā', u'vvi', u'vvī', u'vvu', u'vvū', u'vvṛ', u'vvṝ', u'vval̥', u'vvaḹ', u'vve', u'vvē', u'vvhai', u'vvo', u'vvō', u'vvau', u'vvam̐', u'vvaṁ', u'vvaḥ', u'vv' , u'vva'],
    [u'ṯṯā', u'ṯṯi', u'ṯṯī', u'ṯṯu', u'ṯṯū', u'ṯṯṛ', u'ṯṯṝ', u'ṯṯal̥', u'ṯṯaḹ', u'ṯṯe', u'ṯṯē', u'ṯṯhai', u'ṯṯo', u'ṯṯō', u'ṯṯau', u'ṯṯam̐', u'ṯṯaṁ', u'ṯṯaḥ', u'ṯṯ' , u'ṯṯa'],
    [u'nṯā', u'nṯi', u'nṯī', u'nṯu', u'nṯū', u'nṯṛ', u'nṯṝ', u'nṯal̥', u'nṯaḹ', u'nṯe', u'nṯē', u'nṯhai', u'nṯo', u'nṯō', u'nṯau', u'nṯam̐', u'nṯaṁ', u'nṯaḥ', u'nṯ' , u'nṯa'],
    # [u"nṯa"],
    [u'kkāṁ', u'kkiṁ', u'kkīṁ', u'kkuṁ', u'kkūṁ', u'kkṛṁ', u'kkṝṁ', u'kkal̥ṁ', u'kkaḹṁ', u'kkeṁ', u'kkēṁ', u'kkhaiṁ', u'kkoṁ', u'kkōṁ', u'kkauṁ', u'kkaṁ'],
    [u'ṅkāṁ', u'ṅkiṁ', u'ṅkīṁ', u'ṅkuṁ', u'ṅkūṁ', u'ṅkṛṁ', u'ṅkṝṁ', u'ṅkal̥ṁ', u'ṅkaḹṁ', u'ṅkeṁ', u'ṅkēṁ', u'ṅkhaiṁ', u'ṅkoṁ', u'ṅkōṁ', u'ṅkauṁ', u'ṅkaṁ'],
    [u'ṅṅāṁ', u'ṅṅiṁ', u'ṅṅīṁ', u'ṅṅuṁ', u'ṅṅūṁ', u'ṅṅṛṁ', u'ṅṅṝṁ', u'ṅṅal̥ṁ', u'ṅṅaḹṁ', u'ṅṅeṁ', u'ṅṅēṁ', u'ṅṅhaiṁ', u'ṅṅoṁ', u'ṅṅōṁ', u'ṅṅauṁ', u'ṅṅaṁ'],
    [u'ccāṁ', u'cciṁ', u'ccīṁ', u'ccuṁ', u'ccūṁ', u'ccṛṁ', u'ccṝṁ', u'ccal̥ṁ', u'ccaḹṁ', u'cceṁ', u'ccēṁ', u'cchaiṁ', u'ccoṁ', u'ccōṁ', u'ccauṁ', u'ccaṁ'],
    [u'ñcāṁ', u'ñciṁ', u'ñcīṁ', u'ñcuṁ', u'ñcūṁ', u'ñcṛṁ', u'ñcṝṁ', u'ñcal̥ṁ', u'ñcaḹṁ', u'ñceṁ', u'ñcēṁ', u'ñchaiṁ', u'ñcoṁ', u'ñcōṁ', u'ñcauṁ', u'ñcaṁ'],
    [u'ññāṁ', u'ññiṁ', u'ññīṁ', u'ññuṁ', u'ññūṁ', u'ññṛṁ', u'ññṝṁ', u'ññal̥ṁ', u'ññaḹṁ', u'ññeṁ', u'ññēṁ', u'ññhaiṁ', u'ññoṁ', u'ññōṁ', u'ññauṁ', u'ññaṁ'],
    [u'ṭṭāṁ', u'ṭṭiṁ', u'ṭṭīṁ', u'ṭṭuṁ', u'ṭṭūṁ', u'ṭṭṛṁ', u'ṭṭṝṁ', u'ṭṭal̥ṁ', u'ṭṭaḹṁ', u'ṭṭeṁ', u'ṭṭēṁ', u'ṭṭhaiṁ', u'ṭṭoṁ', u'ṭṭōṁ', u'ṭṭauṁ', u'ṭṭaṁ'],
    [u'ṇṭāṁ', u'ṇṭiṁ', u'ṇṭīṁ', u'ṇṭuṁ', u'ṇṭūṁ', u'ṇṭṛṁ', u'ṇṭṝṁ', u'ṇṭal̥ṁ', u'ṇṭaḹṁ', u'ṇṭeṁ', u'ṇṭēṁ', u'ṇṭhaiṁ', u'ṇṭoṁ', u'ṇṭōṁ', u'ṇṭauṁ', u'ṇṭaṁ'],
    [u'ṇṇāṁ', u'ṇṇiṁ', u'ṇṇīṁ', u'ṇṇuṁ', u'ṇṇūṁ', u'ṇṇṛṁ', u'ṇṇṝṁ', u'ṇṇal̥ṁ', u'ṇṇaḹṁ', u'ṇṇeṁ', u'ṇṇēṁ', u'ṇṇhaiṁ', u'ṇṇoṁ', u'ṇṇōṁ', u'ṇṇauṁ', u'ṇṇaṁ'],
    [u'ttāṁ', u'ttiṁ', u'ttīṁ', u'ttuṁ', u'ttūṁ', u'ttṛṁ', u'ttṝṁ', u'ttal̥ṁ', u'ttaḹṁ', u'tteṁ', u'ttēṁ', u'tthaiṁ', u'ttoṁ', u'ttōṁ', u'ttauṁ', u'ttaṁ'],
    [u'ntāṁ', u'ntiṁ', u'ntīṁ', u'ntuṁ', u'ntūṁ', u'ntṛṁ', u'ntṝṁ', u'ntal̥ṁ', u'ntaḹṁ', u'nteṁ', u'ntēṁ', u'nthaiṁ', u'ntoṁ', u'ntōṁ', u'ntauṁ', u'ntaṁ'],
    [u'nnāṁ', u'nniṁ', u'nnīṁ', u'nnuṁ', u'nnūṁ', u'nnṛṁ', u'nnṝṁ', u'nnal̥ṁ', u'nnaḹṁ', u'nneṁ', u'nnēṁ', u'nnhaiṁ', u'nnoṁ', u'nnōṁ', u'nnauṁ', u'nnaṁ'],
    [u'ppāṁ', u'ppiṁ', u'ppīṁ', u'ppuṁ', u'ppūṁ', u'ppṛṁ', u'ppṝṁ', u'ppal̥ṁ', u'ppaḹṁ', u'ppeṁ', u'ppēṁ', u'pphaiṁ', u'ppoṁ', u'ppōṁ', u'ppauṁ', u'ppaṁ'],
    [u'mpāṁ', u'mpiṁ', u'mpīṁ', u'mpuṁ', u'mpūṁ', u'mpṛṁ', u'mpṝṁ', u'mpal̥ṁ', u'mpaḹṁ', u'mpeṁ', u'mpēṁ', u'mphaiṁ', u'mpoṁ', u'mpōṁ', u'mpauṁ', u'mpaṁ'],
    [u'mmāṁ', u'mmiṁ', u'mmīṁ', u'mmuṁ', u'mmūṁ', u'mmṛṁ', u'mmṝṁ', u'mmal̥ṁ', u'mmaḹṁ', u'mmeṁ', u'mmēṁ', u'mmhaiṁ', u'mmoṁ', u'mmōṁ', u'mmauṁ', u'mmaṁ'],
    [u'ccāṁ', u'cciṁ', u'ccīṁ', u'ccuṁ', u'ccūṁ', u'ccṛṁ', u'ccṝṁ', u'ccal̥ṁ', u'ccaḹṁ', u'cceṁ', u'ccēṁ', u'cchaiṁ', u'ccoṁ', u'ccōṁ', u'ccauṁ', u'ccaṁ'],
    [u'bbāṁ', u'bbiṁ', u'bbīṁ', u'bbuṁ', u'bbūṁ', u'bbṛṁ', u'bbṝṁ', u'bbal̥ṁ', u'bbaḹṁ', u'bbeṁ', u'bbēṁ', u'bbhaiṁ', u'bboṁ', u'bbōṁ', u'bbauṁ', u'bbaṁ'],
    [u'yyāṁ', u'yyiṁ', u'yyīṁ', u'yyuṁ', u'yyūṁ', u'yyṛṁ', u'yyṝṁ', u'yyal̥ṁ', u'yyaḹṁ', u'yyeṁ', u'yyēṁ', u'yyhaiṁ', u'yyoṁ', u'yyōṁ', u'yyauṁ', u'yyaṁ'],
    [u'vvāṁ', u'vviṁ', u'vvīṁ', u'vvuṁ', u'vvūṁ', u'vvṛṁ', u'vvṝṁ', u'vval̥ṁ', u'vvaḹṁ', u'vveṁ', u'vvēṁ', u'vvhaiṁ', u'vvoṁ', u'vvōṁ', u'vvauṁ', u'vvaṁ'],
    [u'ṯṯāṁ', u'ṯṯiṁ', u'ṯṯīṁ', u'ṯṯuṁ', u'ṯṯūṁ', u'ṯṯṛṁ', u'ṯṯṝṁ', u'ṯṯal̥ṁ', u'ṯṯaḹṁ', u'ṯṯeṁ', u'ṯṯēṁ', u'ṯṯhaiṁ', u'ṯṯoṁ', u'ṯṯōṁ', u'ṯṯauṁ', u'ṯṯaṁ'],
    [u'nṯāṁ', u'nṯiṁ', u'nṯīṁ', u'nṯuṁ', u'nṯūṁ', u'nṯṛṁ', u'nṯṝṁ', u'nṯal̥ṁ', u'nṯaḹṁ', u'nṯeṁ', u'nṯēṁ', u'nṯhaiṁ', u'nṯoṁ', u'nṯōṁ', u'nṯauṁ', u'nṯaṁ'],
]



