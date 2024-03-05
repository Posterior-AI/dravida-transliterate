
import argparse
import pickle as pkl
from DeTransliterator import DeTransliterator


def detransliterate(all_data, lang):
    """
    "all_data": a list of lists.
                Each list has text to be transliterated.
    "lang": "Telugu", "Kannada", "Tamil", "Malayalam"

    returns transliterated lists
    """
    detransliterator = DeTransliterator(lang)

    detransliterated = []
    for each_data in all_data:
        detransliterated.append(detransliterator.detransliterate(each_data))

    return detransliterated


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DeTransliterate given text.')
    parser.add_argument('--data_file', type=str,
                        help='File containing all data')
    parser.add_argument('--lang', type=str,
                        help='Language to DeTransliterate to')
    parser.add_argument('--out_file', type=str, default="data_detransliterated.txt", required=False,
                        help='Output file')

    args = parser.parse_args()

    # Load all_data from a file
    if args.data_file.endswith(".pkl"):
        all_data = pkl.load(open(args.data_file, "rb"))
    else:
        # Load all_data from a text file
        with open(args.data_file, 'r', encoding="utf-8") as file:
            all_data = [line.strip() for line in file]

    detransliterated = detransliterate(all_data, args.lang)

    # Save all_tokens to a text file
    with open(args.out_file, 'w') as file:
        for each_line in detransliterated:
            file.write(each_line.replace("\n", "\\n") + "\n")
