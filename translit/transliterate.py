import argparse
import pickle as pkl
from translit.Transliterator import Transliterator


def transliterate(all_data, lang):
    """
    "all_data": a list of lists.
                Each list has text to be transliterated.
    "lang": "Telugu", "Kannada", "Tamil", "Malayalam"

    returns transliterated lists
    """
    transliterator = Transliterator(lang)

    transliterated = []
    for each_data in all_data:
        transliterated.append(transliterator.transliterate(each_data.upper()))

    return transliterated


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Transliterate given text.')
    parser.add_argument('--data_file', type=str,
                        help='File containing all data')
    parser.add_argument('--lang', type=str,
                        help='Language to Transliterate')
    parser.add_argument('--out_file', type=str, default="data_transliterated.txt", required=False,
                        help='Output file')

    args = parser.parse_args()

    # Load all_data from a file
    if args.data_file.endswith(".pkl"):
        all_data = pkl.load(open(args.data_file, "rb"))
    else:
        # Load all_data from a text file
        with open(args.data_file, 'r', encoding="utf-8") as file:
            all_data = [line.strip() for line in file]

    transliterated = transliterate(all_data, args.lang)

    # Save all_tokens to a text file
    with open(args.out_file, 'w') as file:
        for each_line in transliterated:
            file.write(each_line.replace("\n", "\\n") + "\n")

