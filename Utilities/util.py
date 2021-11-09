PRONUNCIATION_CSV_PATH = "data/pronunciation.csv"

import csv, re

# Convert raw user input to a list of words
def tokenize(data):
  word = []
  word = data.split(" ")
  word = re.split('; |, |\*|\n| ',data)
  return word
	

def get_pronunciation(word):
  with open(PRONUNCIATION_CSV_PATH, 'rt',encoding="utf8") as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
      if word == row[0]:
        numbers = row[1].strip().split(' ')
        # map string to integers
        return list(map(int, numbers))
      