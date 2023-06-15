# basic_python_wordcount
# Text Analysis Project

This project aims to perform basic text analysis on a plain text file using Python libraries such as `pandas`, `collections`, `re` (regular expressions), and `chardet`.

## Project Description

The Python script reads a text file, performs basic preprocessing such as removing punctuation, converting to lowercase, and splitting the text into individual words. It then filters out numbers and words that start with "http" or "www", counting the frequency of the remaining words.

The output is a pandas DataFrame sorted by word frequency in descending order. The script also calculates and prints the total number of unique words in the text. Finally, the DataFrame is saved to a .txt file for further analysis.

## Usage

1. Ensure you have the required Python libraries installed. You can do this by running `pip install pandas collections re chardet`.
2. Replace `'el_quijote.txt'` in the script with the path to your own .txt file.
3. Run the script with Python3: `python3 script_name.py`

## Results

After running the script, a .txt file named `result.txt` will be created in the same directory. This file contains the DataFrame with each unique word and its frequency. Additionally, the total number of unique words in the text will be printed in the console.

## Possible Extensions

This project can be extended to perform more advanced text analysis, such as using natural language processing techniques to tokenize the text or lemmatize the words. Please feel free to contribute to this project by adding more features or improving the existing ones.

## Contact

Please open an issue if you encounter a problem or have any suggestions. Pull requests are also welcome.
