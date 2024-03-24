import re
import os

def repl(txt):
    return txt.replace("a്‌", "").replace("ർ", "ṟ").replace("ൾ", "ḷ").replace("ൻ", "n").replace("ർ", "ṟ").replace("ൽ", "l").replace("aെ", "e").replace("aേ", "ē").replace("aൊ", "o").replace("aോ", "ō")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Correct transliterated text.')
    parser.add_argument('--data_file', type=str,
                        help='data file')
    parser.add_argument('--out_file', type=str, default="data_corrected.txt", required=False,
                        help='Output file')

    args = parser.parse_args()

    all_data = None
    # Load all_data from a file
    if args.data_file.endswith(".pkl"):
        all_data = pkl.load(open(args.data_file, "rb"))
    else:
        # Load all_data from a text file
        with open(args.data_file, 'r', encoding="utf-8") as file:
            all_data = [line.strip() for line in file]

    corrected = [repl(each) for each in all_data]

    # Save all_tokens to a text file
    with open(args.out_file, 'w') as file:
        for each_line in corrected:
            file.write(each_line.replace("\n", "\\n") + "\n")
