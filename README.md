# synth-me

Synth-me is a concatenative text-to-speech engine implemented in Python.

I started this project in January 2015 because I was intrigued by text-to-speech software and wanted to learn more about how it worked.

A **concatenative** text-to-speech engine creates an audio representation of text by pasting together a bunch of small audio files to form the whole of the output.

There are three steps, including:

* **Text-to-words**, where raw input text is converted into an array of words. This also generally includes converting numerical digits into their word equivalents (ex: turn "5" into "five").
* **Words-to-phonemes**, where the array of words is converted into phonemes. Phonemes are the individual sounds in a language. As English is not a phonetic language, the pronunciation of a word can vary drastically from its pronunciation. This problem is solved by looking up the pronunciation for a word in a CSV file. The output is an array of numbers that each correspond to one of the 44 English phonemes.
* **Phonemes-to-sounds**, where each phoneme is paired with an audio file. This is the point where the actual audio is stitched together. It would also be in this step that the correct voice for the audio is selected, assuming multiple voices are supported.

## Dependencies
This project relies on Python 3.x.

## Installation
Follow the steps below to try the speech synthesizer out.

1. Make sure that all dependencies are installed.
2. Clone or download this repository to your local machine.
3. Open a terminal and navigate to the cloned directory.
4. Run: `pip install -r requirements.txt`
5. Run the command `python3 synthme.py`
6. You will be prompted for a message. Enter what you want the engine to say!
7. The program will end. Open output.wav to hear the result.

