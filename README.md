
* **Text-to-words**, where raw input text is tokenized into an list of words. This also generally includes converting numerical digits into their word equivalents (ex: turn "5" into "five").
* **Words-to-phonemes**, where the array of words is converted into phonemes. Phonemes are the individual sounds in a language. As Hindi has a very vast phonetic genre, the  hindi alphabetic pronunciation can vary change the pronunciation of the whole word. System has already mapped the hindi phonetic sounds to their alphabets, so whenever the alphabet is detected, the system just maps to its audio file and return its number. The output is an list of numbers that each correspond to one of the 44 hindi phonemes.
* **Phonemes-to-sounds**, where each phoneme is paired with an audio file. This is the point where the actual audio is stitched together. It would also be in this step that the correct voice for the audio is selected, assuming multiple voices are supported.

## Future Work
Right now the system has only one voice, that is mine and my project buddy's [@SarthakSavasil][1]. We would love to add a few more voices to it.
Also the Phoneme database is limited to only 44 audio files (at the time I am writing this) covering all the major and frequently used Hindi Alphabets.
So we need to build a bigger Phonetic voice database.

Do contribute to it if you can. It will really help us and make this project grow.

## Dependencies
This project relies on 
* Python 3x.
* re (for tokenization)
* wave and os (for stiching together the audio files)

## Installation
Follow the steps below to try the speech synthesizer out.

1. Make sure that all dependencies are installed.
2. Open a terminal and navigate to the cloned directory.
3. Run: `pip install -r requirements.txt`
4. Run the command `**python3 SpeechSynthesis.py**`
5. You will be prompted to input a message. Enter what you want the system to say for you!
6. The program will generate the output as a .wav file and end. Open output.wav to hear the result.

[1]:https://github.com/SarthakSavasil
