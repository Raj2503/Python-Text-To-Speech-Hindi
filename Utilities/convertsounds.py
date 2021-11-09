# Matches each phoneme from list with appropriate wav file

from Utilities import phonemes
import wave, os

VOICE_PATH = os.path.dirname(__file__) + "/../data/voices/"

def phonemes_to_sounds(phoneme_list, outfile):
	infiles = []
	for phoneme in phoneme_list:
		infiles.append(get_sound_file(phoneme))
	data = []
	for infile in infiles:
		w = wave.open(infile, 'rb')
		data.append( [w.getparams(), w.readframes(w.getnframes())] )
		w.close()

	output = wave.open(outfile, 'wb')
	output.setparams(data[0][0])
	for idx, val in enumerate(data):
		output.writeframes(data[idx][1])
	output.close()

def get_sound_file(phoneme):
	fname = "%02d" % phoneme
	return VOICE_PATH + fname + ".wav"