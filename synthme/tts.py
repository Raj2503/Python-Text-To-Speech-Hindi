# tts.py
# Pulls all three pieces together: convertwords, convertphonemes, convertsounds

DATABASE_NAME = "data/pronunciation.db"
OUTPUT_FILE = "output.wav"

from synthme import convertphonemes, convertsounds, util

def text_to_speech(message, output_file=OUTPUT_FILE, debug=False, use_pronunciation_dict=True):
	if debug: print("Text to Speech Generation started.")
	print(message)
	words = util.tokenize(message)
	print(words)
	if debug: print("Words list: " + str(words))
	phonemes = convertphonemes.words_to_phonemes(words, use_pronunciation_dict)
	if debug: print("Phonemes list: " + str(phonemes))
	convertsounds.phonemes_to_sounds(phonemes, output_file)
	if debug: print("File created.")
