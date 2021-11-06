# convertphones.py
# Takes list of words and finds appropriate phonemes
# If phoneme not found, an educated guess is made

from Utilities import phonemes, util
import ast, re

def words_to_phonemes(words, use_pronunciation_dict=True):
	# Takes list of words and punctuation
	result = []
	for word in words:
		# Check if the word has been learned
		row = False
		if use_pronunciation_dict:
			row = util.get_pronunciation(word)
		if row:
			# Append the syllables in this word
			result.extend(row)
		else:
			# If not recognized, take an (un)educated guess
			blocked = phoneme_scan(word)
			result.extend(phoneme_blocks_to_list(blocked))
		result.append(phonemes.PAUSE_WORD)
	return result

def phoneme_blocks_to_list(blocks):
	blocks_list = re.findall("\[\d+\]", blocks)
	result = []
	for b in blocks_list:
		result.append(int(re.sub(r'\[(\d+)\]', r'\1', b)))
	return result


def phoneme_scan(word):
	# while re.search("[ट]", word): # Keep replacing letters with phonemes in brackets [] until there are no more letters
		# Special patterns
		# while re.search("[a-zA-Z.,;!?]", word):
	while re.search("[अ-ॐ.,;!?]", word):

		# word = replace_with_phoneme(word, r'iew', (phonemes.CONS_Y, phonemes.VOWEL_OO,phonemes.CONS_W))
		
		# word = replace_with_phoneme(word, r'oo', (phonemes.VOWEL_OO,))
		# word = replace_with_phoneme(word, r'ou', (phonemes.VOWEL_OO,))
		# word = replace_with_phoneme(word, r'ea', (phonemes.VOWEL_II,))
		# word = replace_with_phoneme(word, r'ee', (phonemes.VOWEL_II,))

		# word = replace_with_phoneme(word, r'gg', (phonemes.CONS_J,))
		# word = replace_with_phoneme(word, r'dd', (phonemes.CONS_D,))
		# word = replace_with_phoneme(word, r'ph', (phonemes.CONS_F,))
		# word = replace_with_phoneme(word, r'll', (phonemes.CONS_L,))
		# word = replace_with_phoneme(word, r'ss', (phonemes.CONS_S,))
		# word = replace_with_phoneme(word, r'nn', (phonemes.CONS_N,))
		# word = replace_with_phoneme(word, r'ch', (phonemes.CONS_CH,))
		# word = replace_with_phoneme(word, r'sh', (phonemes.CONS_SH,))
		# word = replace_with_phoneme(word, r'th', (phonemes.CONS_TH,))
		# word = replace_with_phoneme(word, r'ck', (phonemes.CONS_K,))

# 		# Default letters
# क
# ख
# ग
# घ
# ङ
# च
# छ
# ज
# झ
# ञ
# ट
# ठ
# ड
# ढ
# ण
# त
# थ
# द
# ध
# न
# ऩ
# प
# फ
# ब
# भ
# म
# य
# र
# ऱ
# ल
# ळ
# ऴ
# व
# श
# ष
# स
# ह

		word = replace_with_phoneme(word, "अ", (phonemes.VOWEL_U,))
		word = replace_with_phoneme(word, "आ", (phonemes.VOWEL_A,))
		word = replace_with_phoneme(word, "ा", (phonemes.VOWEL_A,))

		word = replace_with_phoneme(word, "इ", (phonemes.VOWEL_I,))
		word = replace_with_phoneme(word, "ि", (phonemes.VOWEL_I,))
		word = replace_with_phoneme(word, "ई", (phonemes.VOWEL_II,))
		word = replace_with_phoneme(word, "ी", (phonemes.VOWEL_II,))
	
		word = replace_with_phoneme(word, "उ", (phonemes.VOWEL_PU,))
		word = replace_with_phoneme(word, "ु", (phonemes.VOWEL_PU,))
		word = replace_with_phoneme(word, "ऊ", (phonemes.VOWEL_OO,))
		word = replace_with_phoneme(word, "ू", (phonemes.VOWEL_OO,))
		word = replace_with_phoneme(word, "ृ", (phonemes.CONS_R,))

		word = replace_with_phoneme(word, "ए", (phonemes.VOWEL_AE,))
		word = replace_with_phoneme(word, "े", (phonemes.VOWEL_AE,))
		word = replace_with_phoneme(word, "ॆ", (phonemes.VOWEL_AE,))
		word = replace_with_phoneme(word, "ऐ", (phonemes.VOWEL_E,))
		word = replace_with_phoneme(word, "ै", (phonemes.VOWEL_E,))

		word = replace_with_phoneme(word, "ओ", (phonemes.VOWEL_OH,))
		word = replace_with_phoneme(word, "ऒ", (phonemes.VOWEL_OH,))
		word = replace_with_phoneme(word, "ो", (phonemes.VOWEL_OH,))
		word = replace_with_phoneme(word, "औ", (phonemes.VOWEL_CA,))
		word = replace_with_phoneme(word, "ौ", (phonemes.VOWEL_CA,))
		word = replace_with_phoneme(word, "ऑ", (phonemes.VOWEL_CA,))

		word = replace_with_phoneme(word, "क", (phonemes.CONS_K,))
		word = replace_with_phoneme(word, "ख", (phonemes.CONS_K,))
		word = replace_with_phoneme(word, "ग", (phonemes.CONS_G,))
		word = replace_with_phoneme(word, "घ", (phonemes.CONS_G,))
		word = replace_with_phoneme(word, "ङ", (phonemes.CONS_D,))
		
		word = replace_with_phoneme(word, "च", (phonemes.CONS_CH,))
		word = replace_with_phoneme(word, "छ", (phonemes.CONS_JJ,))
		word = replace_with_phoneme(word, "ज", (phonemes.CONS_J,))
		word = replace_with_phoneme(word, "झ", (phonemes.CONS_JJ,))
		word = replace_with_phoneme(word, "ञ", (phonemes.CONS_N,))


		word = replace_with_phoneme(word, "ट", (phonemes.CONS_T,))
		word = replace_with_phoneme(word, "ठ", (phonemes.CONS_TH,))
		word = replace_with_phoneme(word, "ड", (phonemes.CONS_D,))
		word = replace_with_phoneme(word, "ढ", (phonemes.CONS_D,))
		word = replace_with_phoneme(word, "ण", (phonemes.CONS_N,))

		word = replace_with_phoneme(word, "त", (phonemes.CONS_TH,))
		word = replace_with_phoneme(word, "थ", (phonemes.CONS_TH,))
		word = replace_with_phoneme(word, "ध", (phonemes.CONS_TH,))
		word = replace_with_phoneme(word, "द", (phonemes.CONS_TH2,))
		word = replace_with_phoneme(word, "न", (phonemes.CONS_N,))

		word = replace_with_phoneme(word, "प", (phonemes.CONS_P,))
		word = replace_with_phoneme(word, "फ", (phonemes.CONS_F,))
		word = replace_with_phoneme(word, "ब", (phonemes.CONS_B,))
		word = replace_with_phoneme(word, "भ", (phonemes.CONS_P,))
		word = replace_with_phoneme(word, "म", (phonemes.CONS_M,))
		word = replace_with_phoneme(word, "य", (phonemes.CONS_Y,))

		word = replace_with_phoneme(word, "र", (phonemes.CONS_R,))
		word = replace_with_phoneme(word, "ल", (phonemes.CONS_L,))
		word = replace_with_phoneme(word, "व", (phonemes.CONS_V,))
		word = replace_with_phoneme(word, "श", (phonemes.CONS_SH,))
		word = replace_with_phoneme(word, "ष", (phonemes.CONS_SH,))
		word = replace_with_phoneme(word, "स", (phonemes.CONS_S,))
		word = replace_with_phoneme(word, "ह", (phonemes.CONS_H,))

		word = replace_with_phoneme(word, "ज़", (phonemes.CONS_Z,))


		# word = replace_with_phoneme(word, "q", (phonemes.CONS_K,))

		# word = replace_with_phoneme(word, "w", (phonemes.CONS_W,))
		# word = replace_with_phoneme(word, "x", (phonemes.CONS_K, phonemes.CONS_S))
		word = replace_with_phoneme(word, ".", (phonemes.PUNC_PERIOD,))
		word = replace_with_phoneme(word, ",", (phonemes.PUNC_COMMA,))
		word = replace_with_phoneme(word, ";", (phonemes.PUNC_COMMA,))
		word = replace_with_phoneme(word, "!", (phonemes.PUNC_EXCLAIM,))
		return word

def replace_with_phoneme(word, letters, phoneme_ids):
	result = ""
	for phoneme_id in phoneme_ids:
		result += "["+str(phoneme_id)+"]"
	return word.replace(letters, result)