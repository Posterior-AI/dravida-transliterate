from translit.latin2telugu import lang as telugu
from translit.latin2tamil import lang as tamil
from translit.latin2kannada import lang as kannada
from translit.latin2malayalam import lang as malayalam

from translit.latin2telugu import latinized as latinized_telugu
from translit.latin2tamil import latinized as latinized_tamil
from translit.latin2kannada import latinized as latinized_kannada
from translit.latin2malayalam import latinized as latinized_malayalam

langs = [telugu, tamil, kannada, malayalam]
ltnzd = [latinized_telugu, latinized_tamil,
         latinized_kannada, latinized_malayalam]

for j in range(4):
    list1 = []
    for each in langs[j]:
        list1.append(len(each))
    list2 = []
    for each in ltnzd[j]:
        list2.append(len(each))
    print(sum(list1), sum(list2), sum(list1) == sum(list2))
