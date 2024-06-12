import sys
import json

# A simple script to combine two quote files
def combine_quote_files(files):
    combined_quotes = []

    # Extracting and combining quotes from each file
    for file_name in files:
        with open(file_name, 'r') as file:
            data = json.load(file)
            combined_quotes.extend(data['quotes'])

    # Generating the output file name based on input file names
    prefix = '_'.join(f.split('_')[0] for f in files)
    output_filename = f"{prefix}_quotes.json"

    # Writing combined quotes to the output file
    with open(output_filename, 'w') as file:
        json.dump({'quotes': combined_quotes}, file, indent=4)

    print(f"Quotes combined into {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 quote_combiner.py file1.json file2.json [file3.json ...]")
    else:
        combine_quote_files(sys.argv[1:])
