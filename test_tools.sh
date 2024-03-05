python transliterate.py --data_file tests/kn_head.txt --lang Kannada --out_file tests/kn_transliterated.txt
python transliterate.py --data_file tests/ml_head.txt --lang Malayalam --out_file tests/ml_transliterated.txt
python transliterate.py --data_file tests/ta_head.txt --lang Tamil --out_file tests/ta_transliterated.txt

python detransliterate.py --data_file tests/kn_transliterated.txt --lang Kannada --out_file tests/kn_detransliterated.txt
python detransliterate.py --data_file tests/ml_transliterated.txt --lang Malayalam --out_file tests/ml_detransliterated.txt
python detransliterate.py --data_file tests/ta_transliterated.txt --lang Tamil --out_file tests/ta_detransliterated.txt


