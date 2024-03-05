# from MyTransliterator import Transliterator
# from latin2telugu import lang as telugu
# from latin2tamil import lang as tamil
# from latin2kannada import lang as kannada
# from latin2malayalam import lang as malayalam


# x = Transliterator()

# transliterated = []

# langs1 = [tamil, kannada, malayalam]
# langs2 = ["Taml", "Knda", "Mlym"]

# for j in range(3):
#   transliterated_each = []
#   for each in langs1[j]:
#     # print(each)
#     ll = []
#     for each2 in each:
#       ll.append(x.drvda_to_latn(each2, langs2[j]))
#     transliterated_each.append(ll)
#     # print(ll)
#   transliterated.append(transliterated_each)
#   print(transliterated_each)


from ..latin2telugu import lang as telugu
from ..latin2tamil import lang as tamil
from ..latin2kannada import lang as kannada
from ..latin2malayalam import lang as malayalam

from ..latin2telugu import latinized as latinized_telugu
from ..latin2tamil import latinized as latinized_tamil
from ..latin2kannada import latinized as latinized_kannada
from ..latin2malayalam import latinized as latinized_malayalam

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
    # print(list1)
    # print(list2)
    # print()
    print(sum(list1), sum(list2), sum(list1) == sum(list2))
