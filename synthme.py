from Utilities import tts

if __name__ == "__main__":
	# message = input("Message: ")
	# message = "को"
	message = "मैं सार्थक हूँ"

	# for i in message:
	# 	print(i)



	tts.text_to_speech(message, debug=True, use_pronunciation_dict=True)
