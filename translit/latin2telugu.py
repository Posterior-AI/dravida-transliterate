#!/usr/bin/env python
# coding: utf-8

latinized = [
    [u"a", u"ā", u"i", u"ī", u"u", u"ū", u"ṛ", u"ṝ", u"ḷ", u"l̥̄", u"e", u"ē", u"ai", u"o", u"ō", u"au", u"am̐", u"aṁ", u"aḥ", u"—",],
    [u"ka", u"kā", u"ki", u"kī", u"ku", u"kū", u"kṛ", u"kṝ", u"kal̥", u"kal̥̄", u"ke", u"kē", u"kai", u"ko", u"kō", u"kau", u"kam̐", u"kaṁ", u"kaḥ", u"k",],
    [u"kha", u"khā", u"khi", u"khī", u"khu", u"khū", u"khṛ", u"khṝ", u"khal̥", u"khal̥̄", u"khe", u"khē", u"khai", u"kho", u"khō", u"khau", u"kham̐", u"khaṁ", u"khaḥ", u"kh",],
    [u"ga", u"gā", u"gi", u"gī", u"gu", u"gū", u"gṛ", u"gṝ", u"gal̥", u"gal̥̄", u"ge", u"gē", u"gai", u"go", u"gō", u"gau", u"gam̐", u"gaṁ", u"gaḥ", u"g",],
    [u"gha", u"ghā", u"ghi", u"ghī", u"ghu", u"ghū", u"ghṛ", u"ghṝ", u"ghal̥", u"ghal̥̄", u"ghe", u"ghē", u"ghai", u"gho", u"ghō", u"ghau", u"gham̐", u"ghaṁ", u"ghaḥ", u"gh",],
    [u"ṅa", u"ṅā", u"ṅi", u"ṅī", u"ṅu", u"ṅū", u"ṅṛ", u"ṅṝ", u"ṅal̥", u"ṅal̥̄", u"ṅe", u"ṅē", u"ṅai", u"ṅo", u"ṅō", u"ṅau", u"ṅam̐", u"ṅaṁ", u"ṅaḥ", u"ṅ",],
    [u"ca", u"cā", u"ci", u"cī", u"cu", u"cū", u"cṛ", u"cṝ", u"cal̥", u"cal̥̄", u"ce", u"cē", u"cai", u"co", u"cō", u"cau", u"cam̐", u"caṁ", u"caḥ", u"c",],
    [u"cha", u"chā", u"chi", u"chī", u"chu", u"chū", u"chṛ", u"chṝ", u"chal̥", u"chal̥̄", u"che", u"chē", u"chai", u"cho", u"chō", u"chau", u"cham̐", u"chaṁ", u"chaḥ", u"ch",],
    [u"ja", u"jā", u"ji", u"jī", u"ju", u"jū", u"jṛ", u"jṝ", u"jal̥", u"jal̥̄", u"je", u"jē", u"jai", u"jo", u"jō", u"jau", u"jam̐", u"jaṁ", u"jaḥ", u"j",],
    [u"jha", u"jhā", u"jhi", u"jhī", u"jhu", u"jhū", u"jhṛ", u"jhṝ", u"jhal̥", u"jhal̥̄", u"jhe", u"jhē", u"jhai", u"jho", u"jhō", u"jhau", u"jham̐", u"jhaṁ", u"jhaḥ", u"jh",],
    [u"ña", u"ñā", u"ñi", u"ñī", u"ñu", u"ñū", u"ñṛ", u"ñṝ", u"ñal̥", u"ñal̥̄", u"ñe", u"ñē", u"ñai", u"ño", u"ñō", u"ñau", u"ñam̐", u"ñaṁ", u"ñaḥ", u"ñ",],
    [u"ṭa", u"ṭā", u"ṭi", u"ṭī", u"ṭu", u"ṭū", u"ṭṛ", u"ṭṝ", u"ṭal̥", u"ṭal̥̄", u"ṭe", u"ṭē", u"ṭai", u"ṭo", u"ṭō", u"ṭau", u"ṭam̐", u"ṭaṁ", u"ṭaḥ", u"ṭ",],
    [u"ṭha", u"ṭhā", u"ṭhi", u"ṭhī", u"ṭhu", u"ṭhū", u"ṭhṛ", u"ṭhṝ", u"ṭhal̥", u"ṭhal̥̄", u"ṭhe", u"ṭhē", u"ṭhai", u"ṭho", u"ṭhō", u"ṭhau", u"ṭham̐", u"ṭhaṁ", u"ṭhaḥ", u"ṭh",],
    [u"ḍa", u"ḍā", u"ḍi", u"ḍī", u"ḍu", u"ḍū", u"ḍṛ", u"ḍṝ", u"ḍal̥", u"ḍal̥̄", u"ḍe", u"ḍē", u"ḍai", u"ḍo", u"ḍō", u"ḍau", u"ḍam̐", u"ḍaṁ", u"ḍaḥ", u"ḍ",],
    [u"ḍha", u"ḍhā", u"ḍhi", u"ḍhī", u"ḍhu", u"ḍhū", u"ḍhṛ", u"ḍhṝ", u"ḍhal̥", u"ḍhal̥̄", u"ḍhe", u"ḍhē", u"ḍhai", u"ḍho", u"ḍhō", u"ḍhau", u"ḍham̐", u"ḍhaṁ", u"ḍhaḥ", u"ḍh",],
    [u"ṇa", u"ṇā", u"ṇi", u"ṇī", u"ṇu", u"ṇū", u"ṇṛ", u"ṇṝ", u"ṇal̥", u"ṇal̥̄", u"ṇe", u"ṇē", u"ṇai", u"ṇo", u"ṇō", u"ṇau", u"ṇam̐", u"ṇaṁ", u"ṇaḥ", u"ṇ",],
    [u"ta", u"tā", u"ti", u"tī", u"tu", u"tū", u"tṛ", u"tṝ", u"tal̥", u"tal̥̄", u"te", u"tē", u"tai", u"to", u"tō", u"tau", u"tam̐", u"taṁ", u"taḥ", u"t",],
    [u"tha", u"thā", u"thi", u"thī", u"thu", u"thū", u"thṛ", u"thṝ", u"thal̥", u"thal̥̄", u"the", u"thē", u"thai", u"tho", u"thō", u"thau", u"tham̐", u"thaṁ", u"thaḥ", u"th",],
    [u"da", u"dā", u"di", u"dī", u"du", u"dū", u"dṛ", u"dṝ", u"dal̥", u"dal̥̄", u"de", u"dē", u"dai", u"do", u"dō", u"dau", u"dam̐", u"daṁ", u"daḥ", u"d",],
    [u"dha", u"dhā", u"dhi", u"dhī", u"dhu", u"dhū", u"dhṛ", u"dhṝ", u"dhal̥", u"dhal̥̄", u"dhe", u"dhē", u"dhai", u"dho", u"dhō", u"dhau", u"dham̐", u"dhaṁ", u"dhaḥ", u"dh",],
    [u"na", u"nā", u"ni", u"nī", u"nu", u"nū", u"nṛ", u"nṝ", u"nal̥", u"nal̥̄", u"ne", u"nē", u"nai", u"no", u"nō", u"nau", u"nam̐", u"naṁ", u"naḥ", u"n",],
    [u"pa", u"pā", u"pi", u"pī", u"pu", u"pū", u"pṛ", u"pṝ", u"pal̥", u"pal̥̄", u"pe", u"pē", u"pai", u"po", u"pō", u"pau", u"pam̐", u"paṁ", u"paḥ", u"p",],
    [u"pha", u"phā", u"phi", u"phī", u"phu", u"phū", u"phṛ", u"phṝ", u"phal̥", u"phal̥̄", u"phe", u"phē", u"phai", u"pho", u"phō", u"phau", u"pham̐", u"phaṁ", u"phaḥ", u"ph",],
    [u"ba", u"bā", u"bi", u"bī", u"bu", u"bū", u"bṛ", u"bṝ", u"bal̥", u"bal̥̄", u"be", u"bē", u"bai", u"bo", u"bō", u"bau", u"bam̐", u"baṁ", u"baḥ", u"b",],
    [u"bha", u"bhā", u"bhi", u"bhī", u"bhu", u"bhū", u"bhṛ", u"bhṝ", u"bhal̥", u"bhal̥̄", u"bhe", u"bhē", u"bhai", u"bho", u"bhō", u"bhau", u"bham̐", u"bhaṁ", u"bhaḥ", u"bh",],
    [u"ma", u"mā", u"mi", u"mī", u"mu", u"mū", u"mṛ", u"mṝ", u"mal̥", u"mal̥̄", u"me", u"mē", u"mai", u"mo", u"mō", u"mau", u"mam̐", u"maṁ", u"maḥ", u"m",],
    [u"ya", u"yā", u"yi", u"yī", u"yu", u"yū", u"yṛ", u"yṝ", u"yal̥", u"yal̥̄", u"ye", u"yē", u"yai", u"yo", u"yō", u"yau", u"yam̐", u"yaṁ", u"yaḥ", u"y",],
    [u"ra", u"rā", u"ri", u"rī", u"ru", u"rū", u"rṛ", u"rṝ", u"ral̥", u"ral̥̄", u"re", u"rē", u"rai", u"ro", u"rō", u"rau", u"ram̐", u"raṁ", u"raḥ", u"r",],
    [u"la", u"lā", u"li", u"lī", u"lu", u"lū", u"lṛ", u"lṝ", u"lal̥", u"lal̥̄", u"le", u"lē", u"lai", u"lo", u"lō", u"lau", u"lam̐", u"laṁ", u"laḥ", u"l",],
    [u"va", u"vā", u"vi", u"vī", u"vu", u"vū", u"vṛ", u"vṝ", u"val̥", u"val̥̄", u"ve", u"vē", u"vai", u"vo", u"vō", u"vau", u"vam̐", u"vaṁ", u"vaḥ", u"v",],
    [u"śa", u"śā", u"śi", u"śī", u"śu", u"śū", u"śṛ", u"śṝ", u"śal̥", u"śal̥̄", u"śe", u"śē", u"śai", u"śo", u"śō", u"śau", u"śam̐", u"śaṁ", u"śaḥ", u"ś",],
    [u"ṣa", u"ṣā", u"ṣi", u"ṣī", u"ṣu", u"ṣū", u"ṣṛ", u"ṣṝ", u"ṣal̥", u"ṣal̥̄", u"ṣe", u"ṣē", u"ṣai", u"ṣo", u"ṣō", u"ṣau", u"ṣam̐", u"ṣaṁ", u"ṣaḥ", u"ṣ",],
    [u"sa", u"sā", u"si", u"sī", u"su", u"sū", u"sṛ", u"sṝ", u"sal̥", u"sal̥̄", u"se", u"sē", u"sai", u"so", u"sō", u"sau", u"sam̐", u"saṁ", u"saḥ", u"s",],
    [u"ha", u"hā", u"hi", u"hī", u"hu", u"hū", u"hṛ", u"hṝ", u"hal̥", u"hal̥̄", u"he", u"hē", u"hai", u"ho", u"hō", u"hau", u"ham̐", u"haṁ", u"haḥ", u"h",],
    [u"ḷa", u"ḷā", u"ḷi", u"ḷī", u"ḷu", u"ḷū", u"ḷṛ", u"ḷṝ", u"ḷal̥", u"ḷal̥̄", u"ḷe", u"ḷē", u"ḷai", u"ḷo", u"ḷō", u"ḷau", u"ḷam̐", u"ḷaṁ", u"ḷaḥ", u"ḷ",],
    [u"kṣa", u"kṣā", u"kṣi", u"kṣī", u"kṣu", u"kṣū", u"kṣṛ", u"kṣṝ", u"kṣal̥", u"kṣal̥̄", u"kṣe", u"kṣē", u"kṣai", u"kṣo", u"kṣō", u"kṣau", u"kṣam̐", u"kṣaṁ", u"kṣaḥ", u"kṣ",],
    [u"ṟa", u"ṟā", u"ṟi", u"ṟī", u"ṟu", u"ṟū", u"ṟṛ", u"ṟṝ", u"ṟal̥", u"ṟal̥̄", u"ṟe", u"ṟē", u"ṟai", u"ṟo", u"ṟō", u"ṟau", u"ṟam̐", u"ṟaṁ", u"ṟaḥ", u"ṟ",],
    [u"aṁ", u"āṁ", u"iṁ", u"īṁ", u"uṁ", u"ūṁ", u"ṛṁ", u"ṝṁ", u"l̥ṁ", u"l̥̄ṁ", u"eṁ", u"ēṁ", u"aiṁ", u"oṁ", u"ōṁ", u"auṁ",],
    [u"kaṁ", u"kāṁ", u"kiṁ", u"kīṁ", u"kuṁ", u"kūṁ", u"kṛṁ", u"kṝṁ", u"kal̥ṁ", u"kal̥̄ṁ", u"keṁ", u"kēṁ", u"kaiṁ", u"koṁ", u"kōṁ", u"kauṁ",],
    [u"khaṁ", u"khāṁ", u"khiṁ", u"khīṁ", u"khuṁ", u"khūṁ", u"khṛṁ", u"khṝṁ", u"khal̥ṁ", u"khal̥̄ṁ", u"kheṁ", u"khēṁ", u"khaiṁ", u"khoṁ", u"khōṁ", u"khauṁ",],
    [u"gaṁ", u"gāṁ", u"giṁ", u"gīṁ", u"guṁ", u"gūṁ", u"gṛṁ", u"gṝṁ", u"gal̥ṁ", u"gal̥̄ṁ", u"geṁ", u"gēṁ", u"gaiṁ", u"goṁ", u"gōṁ", u"gauṁ",],
    [u"ghaṁ", u"ghāṁ", u"ghiṁ", u"ghīṁ", u"ghuṁ", u"ghūṁ", u"ghṛṁ", u"ghṝṁ", u"ghal̥ṁ", u"ghal̥̄ṁ", u"gheṁ", u"ghēṁ", u"ghaiṁ", u"ghoṁ", u"ghōṁ", u"ghauṁ",],
    [u"ṅaṁ", u"ṅāṁ", u"ṅiṁ", u"ṅīṁ", u"ṅuṁ", u"ṅūṁ", u"ṅṛṁ", u"ṅṝṁ", u"ṅal̥ṁ", u"ṅal̥̄ṁ", u"ṅeṁ", u"ṅēṁ", u"ṅaiṁ", u"ṅoṁ", u"ṅōṁ", u"ṅauṁ",],
    [u"caṁ", u"cāṁ", u"ciṁ", u"cīṁ", u"cuṁ", u"cūṁ", u"cṛṁ", u"cṝṁ", u"cal̥ṁ", u"cal̥̄ṁ", u"ceṁ", u"cēṁ", u"caiṁ", u"coṁ", u"cōṁ", u"cauṁ",],
    [u"chaṁ", u"chāṁ", u"chiṁ", u"chīṁ", u"chuṁ", u"chūṁ", u"chṛṁ", u"chṝṁ", u"chal̥ṁ", u"chal̥̄ṁ", u"cheṁ", u"chēṁ", u"chaiṁ", u"choṁ", u"chōṁ", u"chauṁ",],
    [u"jaṁ", u"jāṁ", u"jiṁ", u"jīṁ", u"juṁ", u"jūṁ", u"jṛṁ", u"jṝṁ", u"jal̥ṁ", u"jal̥̄ṁ", u"jeṁ", u"jēṁ", u"jaiṁ", u"joṁ", u"jōṁ", u"jauṁ",],
    [u"jhaṁ", u"jhāṁ", u"jhiṁ", u"jhīṁ", u"jhuṁ", u"jhūṁ", u"jhṛṁ", u"jhṝṁ", u"jhal̥ṁ", u"jhal̥̄ṁ", u"jheṁ", u"jhēṁ", u"jhaiṁ", u"jhoṁ", u"jhōṁ", u"jhauṁ",],
    [u"ñaṁ", u"ñāṁ", u"ñiṁ", u"ñīṁ", u"ñuṁ", u"ñūṁ", u"ñṛṁ", u"ñṝṁ", u"ñal̥ṁ", u"ñal̥̄ṁ", u"ñeṁ", u"ñēṁ", u"ñaiṁ", u"ñoṁ", u"ñōṁ", u"ñauṁ",],
    [u"ṭaṁ", u"ṭāṁ", u"ṭiṁ", u"ṭīṁ", u"ṭuṁ", u"ṭūṁ", u"ṭṛṁ", u"ṭṝṁ", u"ṭal̥ṁ", u"ṭal̥̄ṁ", u"ṭeṁ", u"ṭēṁ", u"ṭaiṁ", u"ṭoṁ", u"ṭōṁ", u"ṭauṁ",],
    [u"ṭhaṁ", u"ṭhāṁ", u"ṭhiṁ", u"ṭhīṁ", u"ṭhuṁ", u"ṭhūṁ", u"ṭhṛṁ", u"ṭhṝṁ", u"ṭhal̥ṁ", u"ṭhal̥̄ṁ", u"ṭheṁ", u"ṭhēṁ", u"ṭhaiṁ", u"ṭhoṁ", u"ṭhōṁ", u"ṭhauṁ",],
    [u"ḍaṁ", u"ḍāṁ", u"ḍiṁ", u"ḍīṁ", u"ḍuṁ", u"ḍūṁ", u"ḍṛṁ", u"ḍṝṁ", u"ḍal̥ṁ", u"ḍal̥̄ṁ", u"ḍeṁ", u"ḍēṁ", u"ḍaiṁ", u"ḍoṁ", u"ḍōṁ", u"ḍauṁ",],
    [u"ḍhaṁ", u"ḍhāṁ", u"ḍhiṁ", u"ḍhīṁ", u"ḍhuṁ", u"ḍhūṁ", u"ḍhṛṁ", u"ḍhṝṁ", u"ḍhal̥ṁ", u"ḍhal̥̄ṁ", u"ḍheṁ", u"ḍhēṁ", u"ḍhaiṁ", u"ḍhoṁ", u"ḍhōṁ", u"ḍhauṁ",],
    [u"ṇaṁ", u"ṇāṁ", u"ṇiṁ", u"ṇīṁ", u"ṇuṁ", u"ṇūṁ", u"ṇṛṁ", u"ṇṝṁ", u"ṇal̥ṁ", u"ṇal̥̄ṁ", u"ṇeṁ", u"ṇēṁ", u"ṇaiṁ", u"ṇoṁ", u"ṇōṁ", u"ṇauṁ",],
    [u"taṁ", u"tāṁ", u"tiṁ", u"tīṁ", u"tuṁ", u"tūṁ", u"tṛṁ", u"tṝṁ", u"tal̥ṁ", u"tal̥̄ṁ", u"teṁ", u"tēṁ", u"taiṁ", u"toṁ", u"tōṁ", u"tauṁ",],
    [u"thaṁ", u"thāṁ", u"thiṁ", u"thīṁ", u"thuṁ", u"thūṁ", u"thṛṁ", u"thṝṁ", u"thal̥ṁ", u"thal̥̄ṁ", u"theṁ", u"thēṁ", u"thaiṁ", u"thoṁ", u"thōṁ", u"thauṁ",],
    [u"daṁ", u"dāṁ", u"diṁ", u"dīṁ", u"duṁ", u"dūṁ", u"dṛṁ", u"dṝṁ", u"dal̥ṁ", u"dal̥̄ṁ", u"deṁ", u"dēṁ", u"daiṁ", u"doṁ", u"dōṁ", u"dauṁ",],
    [u"dhaṁ", u"dhāṁ", u"dhiṁ", u"dhīṁ", u"dhuṁ", u"dhūṁ", u"dhṛṁ", u"dhṝṁ", u"dhal̥ṁ", u"dhal̥̄ṁ", u"dheṁ", u"dhēṁ", u"dhaiṁ", u"dhoṁ", u"dhōṁ", u"dhauṁ",],
    [u"naṁ", u"nāṁ", u"niṁ", u"nīṁ", u"nuṁ", u"nūṁ", u"nṛṁ", u"nṝṁ", u"nal̥ṁ", u"nal̥̄ṁ", u"neṁ", u"nēṁ", u"naiṁ", u"noṁ", u"nōṁ", u"nauṁ",],
    [u"paṁ", u"pāṁ", u"piṁ", u"pīṁ", u"puṁ", u"pūṁ", u"pṛṁ", u"pṝṁ", u"pal̥ṁ", u"pal̥̄ṁ", u"peṁ", u"pēṁ", u"paiṁ", u"poṁ", u"pōṁ", u"pauṁ",],
    [u"phaṁ", u"phāṁ", u"phiṁ", u"phīṁ", u"phuṁ", u"phūṁ", u"phṛṁ", u"phṝṁ", u"phal̥ṁ", u"phal̥̄ṁ", u"pheṁ", u"phēṁ", u"phaiṁ", u"phoṁ", u"phōṁ", u"phauṁ",],
    [u"baṁ", u"bāṁ", u"biṁ", u"bīṁ", u"buṁ", u"būṁ", u"bṛṁ", u"bṝṁ", u"bal̥ṁ", u"bal̥̄ṁ", u"beṁ", u"bēṁ", u"baiṁ", u"boṁ", u"bōṁ", u"bauṁ",],
    [u"bhaṁ", u"bhāṁ", u"bhiṁ", u"bhīṁ", u"bhuṁ", u"bhūṁ", u"bhṛṁ", u"bhṝṁ", u"bhal̥ṁ", u"bhal̥̄ṁ", u"bheṁ", u"bhēṁ", u"bhaiṁ", u"bhoṁ", u"bhōṁ", u"bhauṁ",],
    [u"maṁ", u"māṁ", u"miṁ", u"mīṁ", u"muṁ", u"mūṁ", u"mṛṁ", u"mṝṁ", u"mal̥ṁ", u"mal̥̄ṁ", u"meṁ", u"mēṁ", u"maiṁ", u"moṁ", u"mōṁ", u"mauṁ",],
    [u"yaṁ", u"yāṁ", u"yiṁ", u"yīṁ", u"yuṁ", u"yūṁ", u"yṛṁ", u"yṝṁ", u"yal̥ṁ", u"yal̥̄ṁ", u"yeṁ", u"yēṁ", u"yaiṁ", u"yoṁ", u"yōṁ", u"yauṁ",],
    [u"raṁ", u"rāṁ", u"riṁ", u"rīṁ", u"ruṁ", u"rūṁ", u"rṛṁ", u"rṝṁ", u"ral̥ṁ", u"ral̥̄ṁ", u"reṁ", u"rēṁ", u"raiṁ", u"roṁ", u"rōṁ", u"rauṁ",],
    [u"laṁ", u"lāṁ", u"liṁ", u"līṁ", u"luṁ", u"lūṁ", u"lṛṁ", u"lṝṁ", u"lal̥ṁ", u"lal̥̄ṁ", u"leṁ", u"lēṁ", u"laiṁ", u"loṁ", u"lōṁ", u"lauṁ",],
    [u"vaṁ", u"vāṁ", u"viṁ", u"vīṁ", u"vuṁ", u"vūṁ", u"vṛṁ", u"vṝṁ", u"val̥ṁ", u"val̥̄ṁ", u"veṁ", u"vēṁ", u"vaiṁ", u"voṁ", u"vōṁ", u"vauṁ",],
    [u"śaṁ", u"śāṁ", u"śiṁ", u"śīṁ", u"śuṁ", u"śūṁ", u"śṛṁ", u"śṝṁ", u"śal̥ṁ", u"śal̥̄ṁ", u"śeṁ", u"śēṁ", u"śaiṁ", u"śoṁ", u"śōṁ", u"śauṁ",],
    [u"ṣaṁ", u"ṣāṁ", u"ṣiṁ", u"ṣīṁ", u"ṣuṁ", u"ṣūṁ", u"ṣṛṁ", u"ṣṝṁ", u"ṣal̥ṁ", u"ṣal̥̄ṁ", u"ṣeṁ", u"ṣēṁ", u"ṣaiṁ", u"ṣoṁ", u"ṣōṁ", u"ṣauṁ",],
    [u"saṁ", u"sāṁ", u"siṁ", u"sīṁ", u"suṁ", u"sūṁ", u"sṛṁ", u"sṝṁ", u"sal̥ṁ", u"sal̥̄ṁ", u"seṁ", u"sēṁ", u"saiṁ", u"soṁ", u"sōṁ", u"sauṁ",],
    [u"haṁ", u"hāṁ", u"hiṁ", u"hīṁ", u"huṁ", u"hūṁ", u"hṛṁ", u"hṝṁ", u"hal̥ṁ", u"hal̥̄ṁ", u"heṁ", u"hēṁ", u"haiṁ", u"hoṁ", u"hōṁ", u"hauṁ",],
    [u"ḷaṁ", u"ḷāṁ", u"ḷiṁ", u"ḷīṁ", u"ḷuṁ", u"ḷūṁ", u"ḷṛṁ", u"ḷṝṁ", u"ḷal̥ṁ", u"ḷal̥̄ṁ", u"ḷeṁ", u"ḷēṁ", u"ḷaiṁ", u"ḷoṁ", u"ḷōṁ", u"ḷauṁ",],
    [u"ṟaṁ", u"ṟāṁ", u"ṟiṁ", u"ṟīṁ", u"ṟuṁ", u"ṟūṁ", u"ṟṛṁ", u"ṟṝṁ", u"ṟal̥ṁ", u"ṟal̥̄ṁ", u"ṟeṁ", u"ṟēṁ", u"ṟaiṁ", u"ṟoṁ", u"ṟōṁ", u"ṟauṁ",],
    [u"kṣaṁ", u"kṣāṁ", u"kṣiṁ", u"kṣīṁ", u"kṣuṁ", u"kṣūṁ", u"kṣṛṁ", u"kṣṝṁ", u"kṣal̥ṁ", u"kṣal̥̄ṁ", u"kṣeṁ", u"kṣēṁ", u"kṣaiṁ", u"kṣoṁ", u"kṣōṁ", u"kṣauṁ",],
    [u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10",],
]

lang = [
    [u"అ", u"ఆ", u"ఇ", u"ఈ", u"ఉ", u"ఊ", u"ఋ", u"ౠ", u"ఌ", u"ౡ", u"ఎ", u"ఏ", u"ఐ", u"ఒ", u"ఓ", u"ఔ", u"అఁ", u"అం", u"అః", u"—",],
    [u"క", u"కా", u"కి", u"కీ", u"కు", u"కూ", u"కృ", u"కౄ", u"కౢ", u"కౣ", u"కె", u"కే", u"కై", u"కొ", u"కో", u"కౌ", u"కఁ", u"కం", u"కః", u"క్",],
    [u"ఖ", u"ఖా", u"ఖి", u"ఖీ", u"ఖు", u"ఖూ", u"ఖృ", u"ఖౄ", u"ఖౢ", u"ఖౣ", u"ఖె", u"ఖే", u"ఖై", u"ఖొ", u"ఖో", u"ఖౌ", u"ఖఁ", u"ఖం", u"ఖః", u"ఖ్",],
    [u"గ", u"గా", u"గి", u"గీ", u"గు", u"గూ", u"గృ", u"గౄ", u"గౢ", u"గౣ", u"గె", u"గే", u"గై", u"గొ", u"గో", u"గౌ", u"గఁ", u"గం", u"గః", u"గ్",],
    [u"ఘ", u"ఘా", u"ఘి", u"ఘీ", u"ఘు", u"ఘూ", u"ఘృ", u"ఘౄ", u"ఘౢ", u"ఘౣ", u"ఘె", u"ఘే", u"ఘై", u"ఘొ", u"ఘో", u"ఘౌ", u"ఘఁ", u"ఘం", u"ఘః", u"ఘ్",],
    [u"ఙ", u"ఙా", u"ఙి", u"ఙీ", u"ఙు", u"ఙూ", u"ఙృ", u"ఙౄ", u"ఙౢ", u"ఙౣ", u"ఙె", u"ఙే", u"ఙై", u"ఙొ", u"ఙో", u"ఙౌ", u"ఙఁ", u"ఙం", u"ఙః", u"ఙ్",],
    [u"చ", u"చా", u"చి", u"చీ", u"చు", u"చూ", u"చృ", u"చౄ", u"చౢ", u"చౣ", u"చె", u"చే", u"చై", u"చొ", u"చో", u"చౌ", u"చఁ", u"చం", u"చః", u"చ్",],
    [u"ఛ", u"ఛా", u"ఛి", u"ఛీ", u"ఛు", u"ఛూ", u"ఛృ", u"ఛౄ", u"ఛౢ", u"ఛౣ", u"ఛె", u"ఛే", u"ఛై", u"ఛొ", u"ఛో", u"ఛౌ", u"ఛఁ", u"ఛం", u"ఛః", u"ఛ్",],
    [u"జ", u"జా", u"జి", u"జీ", u"జు", u"జూ", u"జృ", u"జౄ", u"జౢ", u"జౣ", u"జె", u"జే", u"జై", u"జొ", u"జో", u"జౌ", u"జఁ", u"జం", u"జః", u"జ్",],
    [u"ఝ", u"ఝా", u"ఝి", u"ఝీ", u"ఝు", u"ఝూ", u"ఝృ", u"ఝౄ", u"ఝౢ", u"ఝౣ", u"ఝె", u"ఝే", u"ఝై", u"ఝొ", u"ఝో", u"ఝౌ", u"ఝఁ", u"ఝం", u"ఝః", u"ఝ్",],
    [u"ఞ", u"ఞా", u"ఞి", u"ఞీ", u"ఞు", u"ఞూ", u"ఞృ", u"ఞౄ", u"ఞౢ", u"ఞౣ", u"ఞె", u"ఞే", u"ఞై", u"ఞొ", u"ఞో", u"ఞౌ", u"ఞఁ", u"ఞం", u"ఞః", u"ఞ్",],
    [u"ట", u"టా", u"టి", u"టీ", u"టు", u"టూ", u"టృ", u"టౄ", u"టౢ", u"టౣ", u"టె", u"టే", u"టై", u"టొ", u"టో", u"టౌ", u"టఁ", u"టం", u"టః", u"ట్",],
    [u"ఠ", u"ఠా", u"ఠి", u"ఠీ", u"ఠు", u"ఠూ", u"ఠృ", u"ఠౄ", u"ఠౢ", u"ఠౣ", u"ఠె", u"ఠే", u"ఠై", u"ఠొ", u"ఠో", u"ఠౌ", u"ఠఁ", u"ఠం", u"ఠః", u"ఠ్",],
    [u"డ", u"డా", u"డి", u"డీ", u"డు", u"డూ", u"డృ", u"డౄ", u"డౢ", u"డౣ", u"డె", u"డే", u"డై", u"డొ", u"డో", u"డౌ", u"డఁ", u"డం", u"డః", u"డ్",],
    [u"ఢ", u"ఢా", u"ఢి", u"ఢీ", u"ఢు", u"ఢూ", u"ఢృ", u"ఢౄ", u"ఢౢ", u"ఢౣ", u"ఢె", u"ఢే", u"ఢై", u"ఢొ", u"ఢో", u"ఢౌ", u"ఢఁ", u"ఢం", u"ఢః", u"ఢ్",],
    [u"ణ", u"ణా", u"ణి", u"ణీ", u"ణు", u"ణూ", u"ణృ", u"ణౄ", u"ణౢ", u"ణౣ", u"ణె", u"ణే", u"ణై", u"ణొ", u"ణో", u"ణౌ", u"ణఁ", u"ణం", u"ణః", u"ణ్",],
    [u"త", u"తా", u"తి", u"తీ", u"తు", u"తూ", u"తృ", u"తౄ", u"తౢ", u"తౣ", u"తె", u"తే", u"తై", u"తొ", u"తో", u"తౌ", u"తఁ", u"తం", u"తః", u"త్",],
    [u"థ", u"థా", u"థి", u"థీ", u"థు", u"థూ", u"థృ", u"థౄ", u"థౢ", u"థౣ", u"థె", u"థే", u"థై", u"థొ", u"థో", u"థౌ", u"థఁ", u"థం", u"థః", u"థ్",],
    [u"ద", u"దా", u"ది", u"దీ", u"దు", u"దూ", u"దృ", u"దౄ", u"దౢ", u"దౣ", u"దె", u"దే", u"దై", u"దొ", u"దో", u"దౌ", u"దఁ", u"దం", u"దః", u"ద్",],
    [u"ధ", u"ధా", u"ధి", u"ధీ", u"ధు", u"ధూ", u"ధృ", u"ధౄ", u"ధౢ", u"ధౣ", u"ధె", u"ధే", u"ధై", u"ధొ", u"ధో", u"ధౌ", u"ధఁ", u"ధం", u"ధః", u"ధ్",],
    [u"న", u"నా", u"ని", u"నీ", u"ను", u"నూ", u"నృ", u"నౄ", u"నౢ", u"నౣ", u"నె", u"నే", u"నై", u"నొ", u"నో", u"నౌ", u"నఁ", u"నం", u"నః", u"న్",],
    [u"ప", u"పా", u"పి", u"పీ", u"పు", u"పూ", u"పృ", u"పౄ", u"పౢ", u"పౣ", u"పె", u"పే", u"పై", u"పొ", u"పో", u"పౌ", u"పఁ", u"పం", u"పః", u"ప్",],
    [u"ఫ", u"ఫా", u"ఫి", u"ఫీ", u"ఫు", u"ఫూ", u"ఫృ", u"ఫౄ", u"ఫౢ", u"ఫౣ", u"ఫె", u"ఫే", u"ఫై", u"ఫొ", u"ఫో", u"ఫౌ", u"ఫఁ", u"ఫం", u"ఫః", u"ఫ్",],
    [u"బ", u"బా", u"బి", u"బీ", u"బు", u"బూ", u"బృ", u"బౄ", u"బౢ", u"బౣ", u"బె", u"బే", u"బై", u"బొ", u"బో", u"బౌ", u"బఁ", u"బం", u"బః", u"బ్",],
    [u"భ", u"భా", u"భి", u"భీ", u"భు", u"భూ", u"భృ", u"భౄ", u"భౢ", u"భౣ", u"భె", u"భే", u"భై", u"భొ", u"భో", u"భౌ", u"భఁ", u"భం", u"భః", u"భ్",],
    [u"మ", u"మా", u"మి", u"మీ", u"ము", u"మూ", u"మృ", u"మౄ", u"మౢ", u"మౣ", u"మె", u"మే", u"మై", u"మొ", u"మో", u"మౌ", u"మఁ", u"మం", u"మః", u"మ్",],
    [u"య", u"యా", u"యి", u"యీ", u"యు", u"యూ", u"యృ", u"యౄ", u"యౢ", u"యౣ", u"యె", u"యే", u"యై", u"యొ", u"యో", u"యౌ", u"యఁ", u"యం", u"యః", u"య్",],
    [u"ర", u"రా", u"రి", u"రీ", u"రు", u"రూ", u"రృ", u"రౄ", u"రౢ", u"రౣ", u"రె", u"రే", u"రై", u"రొ", u"రో", u"రౌ", u"రఁ", u"రం", u"రః", u"ర్",],
    [u"ల", u"లా", u"లి", u"లీ", u"లు", u"లూ", u"లృ", u"లౄ", u"లౢ", u"లౣ", u"లె", u"లే", u"లై", u"లొ", u"లో", u"లౌ", u"లఁ", u"లం", u"లః", u"ల్",],
    [u"వ", u"వా", u"వి", u"వీ", u"వు", u"వూ", u"వృ", u"వౄ", u"వౢ", u"వౣ", u"వె", u"వే", u"వై", u"వొ", u"వో", u"వౌ", u"వఁ", u"వం", u"వః", u"వ్",],
    [u"శ", u"శా", u"శి", u"శీ", u"శు", u"శూ", u"శృ", u"శౄ", u"శౢ", u"శౣ", u"శె", u"శే", u"శై", u"శొ", u"శో", u"శౌ", u"శఁ", u"శం", u"శః", u"శ్",],
    [u"ష", u"షా", u"షి", u"షీ", u"షు", u"షూ", u"షృ", u"షౄ", u"షౢ", u"షౣ", u"షె", u"షే", u"షై", u"షొ", u"షో", u"షౌ", u"షఁ", u"షం", u"షః", u"ష్",],
    [u"స", u"సా", u"సి", u"సీ", u"సు", u"సూ", u"సృ", u"సౄ", u"సౢ", u"సౣ", u"సె", u"సే", u"సై", u"సొ", u"సో", u"సౌ", u"సఁ", u"సం", u"సః", u"స్",],
    [u"హ", u"హా", u"హి", u"హీ", u"హు", u"హూ", u"హృ", u"హౄ", u"హౢ", u"హౣ", u"హె", u"హే", u"హై", u"హొ", u"హో", u"హౌ", u"హఁ", u"హం", u"హః", u"హ్",],
    [u"ళ", u"ళా", u"ళి", u"ళీ", u"ళు", u"ళూ", u"ళృ", u"ళౄ", u"ళౢ", u"ళౣ", u"ళె", u"ళే", u"ళై", u"ళొ", u"ళో", u"ళౌ", u"ళఁ", u"ళం", u"ళః", u"ళ్",],
    [u"క్ష", u"క్షా", u"క్షి", u"క్షీ", u"క్షు", u"క్షూ", u"క్షృ", u"క్షౄ", u"క్షౢ", u"క్షౣ", u"క్షె", u"క్షే", u"క్షై", u"క్షొ", u"క్షో", u"క్షౌ", u"క్షఁ", u"క్షం", u"క్షః", u"క్ష్",],
    [u"ఱ", u"ఱా", u"ఱి", u"ఱీ", u"ఱు", u"ఱూ", u"ఱృ", u"ఱౄ", u"ఱౢ", u"ఱౣ", u"ఱె", u"ఱే", u"ఱై", u"ఱొ", u"ఱో", u"ఱౌ", u"ఱఁ", u"ఱం", u"ఱః", u"ఱ్",],
    [u"అం", u"ఆం", u"ఇం", u"ఈం", u"ఉం", u"ఊం", u"ఋం", u"ౠం", u"ఌం", u"ౡం", u"ఎం", u"ఏం", u"ఐం", u"ఒం", u"ఓం", u"ఔం",],
    [u"కం", u"కాం", u"కిం", u"కీం", u"కుం", u"కూం", u"కృం", u"కౄం", u"కౢం", u"కౣం", u"కెం", u"కేం", u"కైం", u"కొం", u"కోం", u"కౌం",],
    [u"ఖం", u"ఖాం", u"ఖిం", u"ఖీం", u"ఖుం", u"ఖూం", u"ఖృం", u"ఖౄం", u"ఖౢం", u"ఖౣం", u"ఖెం", u"ఖేం", u"ఖైం", u"ఖొం", u"ఖోం", u"ఖౌం",],
    [u"గం", u"గాం", u"గిం", u"గీం", u"గుం", u"గూం", u"గృం", u"గౄం", u"గౢం", u"గౣం", u"గెం", u"గేం", u"గైం", u"గొం", u"గోం", u"గౌం",],
    [u"ఘం", u"ఘాం", u"ఘిం", u"ఘీం", u"ఘుం", u"ఘూం", u"ఘృం", u"ఘౄం", u"ఘౢం", u"ఘౣం", u"ఘెం", u"ఘేం", u"ఘైం", u"ఘొం", u"ఘోం", u"ఘౌం",],
    [u"ఙం", u"ఙాం", u"ఙిం", u"ఙీం", u"ఙుం", u"ఙూం", u"ఙృం", u"ఙౄం", u"ఙౢం", u"ఙౣం", u"ఙెం", u"ఙేం", u"ఙైం", u"ఙొం", u"ఙోం", u"ఙౌం",],
    [u"చం", u"చాం", u"చిం", u"చీం", u"చుం", u"చూం", u"చృం", u"చౄం", u"చౢం", u"చౣం", u"చెం", u"చేం", u"చైం", u"చొం", u"చోం", u"చౌం",],
    [u"ఛం", u"ఛాం", u"ఛిం", u"ఛీం", u"ఛుం", u"ఛూం", u"ఛృం", u"ఛౄం", u"ఛౢం", u"ఛౣం", u"ఛెం", u"ఛేం", u"ఛైం", u"ఛొం", u"ఛోం", u"ఛౌం",],
    [u"జం", u"జాం", u"జిం", u"జీం", u"జుం", u"జూం", u"జృం", u"జౄం", u"జౢం", u"జౣం", u"జెం", u"జేం", u"జైం", u"జొం", u"జోం", u"జౌం",],
    [u"ఝం", u"ఝాం", u"ఝిం", u"ఝీం", u"ఝుం", u"ఝూం", u"ఝృం", u"ఝౄం", u"ఝౢం", u"ఝౣం", u"ఝెం", u"ఝేం", u"ఝైం", u"ఝొం", u"ఝోం", u"ఝౌం",],
    [u"ఞం", u"ఞాం", u"ఞిం", u"ఞీం", u"ఞుం", u"ఞూం", u"ఞృం", u"ఞౄం", u"ఞౢం", u"ఞౣం", u"ఞెం", u"ఞేం", u"ఞైం", u"ఞొం", u"ఞోం", u"ఞౌం",],
    [u"టం", u"టాం", u"టిం", u"టీం", u"టుం", u"టూం", u"టృం", u"టౄం", u"టౢం", u"టౣం", u"టెం", u"టేం", u"టైం", u"టొం", u"టోం", u"టౌం",],
    [u"ఠం", u"ఠాం", u"ఠిం", u"ఠీం", u"ఠుం", u"ఠూం", u"ఠృం", u"ఠౄం", u"ఠౢం", u"ఠౣం", u"ఠెం", u"ఠేం", u"ఠైం", u"ఠొం", u"ఠోం", u"ఠౌం",],
    [u"డం", u"డాం", u"డిం", u"డీం", u"డుం", u"డూం", u"డృం", u"డౄం", u"డౢం", u"డౣం", u"డెం", u"డేం", u"డైం", u"డొం", u"డోం", u"డౌం",],
    [u"ఢం", u"ఢాం", u"ఢిం", u"ఢీం", u"ఢుం", u"ఢూం", u"ఢృం", u"ఢౄం", u"ఢౢం", u"ఢౣం", u"ఢెం", u"ఢేం", u"ఢైం", u"ఢొం", u"ఢోం", u"ఢౌం",],
    [u"ణం", u"ణాం", u"ణిం", u"ణీం", u"ణుం", u"ణూం", u"ణృం", u"ణౄం", u"ణౢం", u"ణౣం", u"ణెం", u"ణేం", u"ణైం", u"ణొం", u"ణోం", u"ణౌం",],
    [u"తం", u"తాం", u"తిం", u"తీం", u"తుం", u"తూం", u"తృం", u"తౄం", u"తౢం", u"తౣం", u"తెం", u"తేం", u"తైం", u"తొం", u"తోం", u"తౌం",],
    [u"థం", u"థాం", u"థిం", u"థీం", u"థుం", u"థూం", u"థృం", u"థౄం", u"థౢం", u"థౣం", u"థెం", u"థేం", u"థైం", u"థొం", u"థోం", u"థౌం",],
    [u"దం", u"దాం", u"దిం", u"దీం", u"దుం", u"దూం", u"దృం", u"దౄం", u"దౢం", u"దౣం", u"దెం", u"దేం", u"దైం", u"దొం", u"దోం", u"దౌం",],
    [u"ధం", u"ధాం", u"ధిం", u"ధీం", u"ధుం", u"ధూం", u"ధృం", u"ధౄం", u"ధౢం", u"ధౣం", u"ధెం", u"ధేం", u"ధైం", u"ధొం", u"ధోం", u"ధౌం",],
    [u"నం", u"నాం", u"నిం", u"నీం", u"నుం", u"నూం", u"నృం", u"నౄం", u"నౢం", u"నౣం", u"నెం", u"నేం", u"నైం", u"నొం", u"నోం", u"నౌం",],
    [u"పం", u"పాం", u"పిం", u"పీం", u"పుం", u"పూం", u"పృం", u"పౄం", u"పౢం", u"పౣం", u"పెం", u"పేం", u"పైం", u"పొం", u"పోం", u"పౌం",],
    [u"ఫం", u"ఫాం", u"ఫిం", u"ఫీం", u"ఫుం", u"ఫూం", u"ఫృం", u"ఫౄం", u"ఫౢం", u"ఫౣం", u"ఫెం", u"ఫేం", u"ఫైం", u"ఫొం", u"ఫోం", u"ఫౌం",],
    [u"బం", u"బాం", u"బిం", u"బీం", u"బుం", u"బూం", u"బృం", u"బౄం", u"బౢం", u"బౣం", u"బెం", u"బేం", u"బైం", u"బొం", u"బోం", u"బౌం",],
    [u"భం", u"భాం", u"భిం", u"భీం", u"భుం", u"భూం", u"భృం", u"భౄం", u"భౢం", u"భౣం", u"భెం", u"భేం", u"భైం", u"భొం", u"భోం", u"భౌం",],
    [u"మం", u"మాం", u"మిం", u"మీం", u"ముం", u"మూం", u"మృం", u"మౄం", u"మౢం", u"మౣం", u"మెం", u"మేం", u"మైం", u"మొం", u"మోం", u"మౌం",],
    [u"యం", u"యాం", u"యిం", u"యీం", u"యుం", u"యూం", u"యృం", u"యౄం", u"యౢం", u"యౣం", u"యెం", u"యేం", u"యైం", u"యొం", u"యోం", u"యౌం",],
    [u"రం", u"రాం", u"రిం", u"రీం", u"రుం", u"రూం", u"రృం", u"రౄం", u"రౢం", u"రౣం", u"రెం", u"రేం", u"రైం", u"రొం", u"రోం", u"రౌం",],
    [u"లం", u"లాం", u"లిం", u"లీం", u"లుం", u"లూం", u"లృం", u"లౄం", u"లౢం", u"లౣం", u"లెం", u"లేం", u"లైం", u"లొం", u"లోం", u"లౌం",],
    [u"వం", u"వాం", u"విం", u"వీం", u"వుం", u"వూం", u"వృం", u"వౄం", u"వౢం", u"వౣం", u"వెం", u"వేం", u"వైం", u"వొం", u"వోం", u"వౌం",],
    [u"శం", u"శాం", u"శిం", u"శీం", u"శుం", u"శూం", u"శృం", u"శౄం", u"శౢం", u"శౣం", u"శెం", u"శేం", u"శైం", u"శొం", u"శోం", u"శౌం",],
    [u"షం", u"షాం", u"షిం", u"షీం", u"షుం", u"షూం", u"షృం", u"షౄం", u"షౢం", u"షౣం", u"షెం", u"షేం", u"షైం", u"షొం", u"షోం", u"షౌం",],
    [u"సం", u"సాం", u"సిం", u"సీం", u"సుం", u"సూం", u"సృం", u"సౄం", u"సౢం", u"సౣం", u"సెం", u"సేం", u"సైం", u"సొం", u"సోం", u"సౌం",],
    [u"హం", u"హాం", u"హిం", u"హీం", u"హుం", u"హూం", u"హృం", u"హౄం", u"హౢం", u"హౣం", u"హెం", u"హేం", u"హైం", u"హొం", u"హోం", u"హౌం",],
    [u"ళం", u"ళాం", u"ళిం", u"ళీం", u"ళుం", u"ళూం", u"ళృం", u"ళౄం", u"ళౢం", u"ళౣం", u"ళెం", u"ళేం", u"ళైం", u"ళొం", u"ళోం", u"ళౌం",],
    [u"ఱం", u"ఱాం", u"ఱిం", u"ఱీం", u"ఱుం", u"ఱూం", u"ఱృం", u"ఱౄం", u"ఱౢం", u"ఱౣం", u"ఱెం", u"ఱేం", u"ఱైం", u"ఱొం", u"ఱోం", u"ఱౌం",],
    [u"క్షం", u"క్షాం", u"క్షిం", u"క్షీం", u"క్షుం", u"క్షూం", u"క్షృం", u"క్షౄం", u"క్షౢం", u"క్షౣం", u"క్షెం", u"క్షేం", u"క్షైం", u"క్షొం", u"క్షోం", u"క్షౌం",],
    [u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10"],
]


# x = u'priyāṁka vippārita nētrālatō trinādh kēsē maunaṁgā cūstuṁḍi pōyiṁdi.\n\n sarīggā ā samayaṁlō trinādh cūstunna pēpars sudarśan rāvuki saṁbaṁdhiṁcinavi. ā pēparsu aṁdavalasina vāriki aṁditē adē sudarśan rāvu patanāniki civari aṁkaṁ avutuṁdi.\n\n vāraṁ rōjulugā priyāṁka udayānnē bayaludēri trinādh daggaraku rāvaḍaṁ, rōjaṁtā atanitō vuṁṭū, parsanal sekraṭarī padavi samardavaṁtaṁgā nirvahiṁcaḍaṁ jarugutuṁdi.\n\n "mā nānnagāru, annayya cēsē ennō mōsālaku nēnu pratyakṣasākṣini. vāṭi dvārā nī kuṭuṁbāniki jarigina anyāyānni sarididdukōvaccugadā?" priyāṁka anna māṭalaku trinādh taletti cirunavvutō cūśāḍu.\n\n "alā vaddu...'

# y = u'ప్రియాంక విప్పారిత నేత్రాలతో త్రినాధ్ కేసే మౌనంగా చూస్తుండి పోయింది.\n\n సరీగ్గా ఆ సమయంలో త్రినాధ్ చూస్తున్న పేపర్స్ సుదర్శన్ రావుకి సంబంధించినవి. ఆ పేపర్సు అందవలసిన వారికి అందితే అదే సుదర్శన్ రావు పతనానికి చివరి అంకం అవుతుంది.\n\n వారం రోజులుగా ప్రియాంక ఉదయాన్నే బయలుదేరి త్రినాధ్ దగ్గరకు రావడం, రోజంతా అతనితో వుంటూ, పర్సనల్ సెక్రటరీ పదవి సమర్దవంతంగా నిర్వహించడం జరుగుతుంది.\n\n "మా నాన్నగారు, అన్నయ్య చేసే ఎన్నో మోసాలకు నేను ప్రత్యక్షసాక్షిని. వాటి ద్వారా నీ కుటుంబానికి జరిగిన అన్యాయాన్ని సరిదిద్దుకోవచ్చుగదా?" ప్రియాంక అన్న మాటలకు త్రినాధ్ తలెత్తి చిరునవ్వుతో చూశాడు.\n\n "అలా వద్దు...'


# dict_of_letters = {}
# for j in range(len(telugu)):
#     dict_of_letters[latinized[j]] = telugu[j]


# def replace_substrings(text, dictionary):
#     sorted_keys = sorted(dictionary.keys(), key=len, reverse=True)
#     for key in sorted_keys:
#         if key in text:
#             text = text.replace(key, dictionary[key])
#     return text


# print(replace_substrings(x, dict_of_letters))


# def convert_latin_to_telugu(latin_text, latin_list, telugu_list):
#     # Create a dictionary for mapping from Latin to Telugu
#     latin_to_telugu = dict(zip(latin_list, telugu_list))

#     # Split the text into words
#     words = latin_text.split()

#     # Convert each word using the mapping
#     converted_words = []
#     for word in words:
#         # Handle punctuation by separating it from the word
#         prefix = ''
#         suffix = ''
#         while word and not word[0].isalnum():
#             prefix += word[0]
#             word = word[1:]
#         while word and not word[-1].isalnum():
#             suffix = word[-1] + suffix
#             word = word[:-1]

#         # Convert the word
#         if word in latin_to_telugu:
#             converted_word = latin_to_telugu[word]
#         else:
#             # If the word is not found, keep it as is
#             converted_word = word

#         # Reattach any punctuation
#         converted_words.append(prefix + converted_word + suffix)

#     # Join the converted words back into a single string
#     converted_text = ' '.join(converted_words)

#     # Replace newlines
#     converted_text = converted_text.replace(' \n', '\n')

#     return converted_text


# # Test the function
# converted_x = convert_latin_to_telugu(x, latinized, telugu)
# print(converted_x)
# print(converted_x == y)  # Should output True if the conversion is correct
