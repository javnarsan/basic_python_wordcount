import pandas as pd
from collections import Counter
import re
import chardet

# Detect the file encoding using the chardet module
with open('el_quijote.txt', 'rb') as f:
    result = chardet.detect(f.read())

# Read the file with the detected encoding
with open('el_quijote.txt', 'r', encoding=result['encoding']) as f:
    text = f.read()

# Remove punctuation and convert words to lowercase
text = re.sub(r'[^\w\s]', ' ', text).lower()

# Split the text into words
words = text.split()

# Filter words to exclude numbers and words beginning with "http" or "www" (possible links)
words = [word for word in words if word.isalpha() and not word.startswith(("http", "www"))]

# Count the words
count = Counter(words)

# Convert the count to a pandas DataFrame
df = pd.DataFrame.from_dict(count, orient='index').reset_index()

# Rename the columns
df = df.rename(columns={'index':'Word', 0:'Occurrences'})

# Order by word count and reset indices
df = df.sort_values('Occurrences', ascending=False).reset_index(drop=True)

# Count the total of different words used
total_different_words = len(df)

# Print the total of unique words
print(f'Total different words used: {total_different_words}')

# Save the result to a text file
df.to_csv('result.txt', sep='\t', index=False)
