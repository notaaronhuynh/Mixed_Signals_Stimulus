# Mixed_Signals_Stimulus
Code that uses Google's Text to Speech API to convert a list of string tokens into MP3 and MP4 audio files for cognitive training experiment with Alzheimer's and Dementia Patients. 

Use Mixed_Signals_Stimulus.ipynb file to create mixed signal stimulus.

To create audio files, install Google API Text to Speech package. To download package, enter the following code in terminal or Python console:

	$ pip install gTTS

From the gtts package, import gTTS:

	from gtts import gTTS

Create a list of string tokens to convert from text to speech.

	numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'];


Create a For Loop in range of the length of list created.

	for i in range(len(numbers)):

Within the For Loop, instantiate a "stimulus" variable that uses the gTTS(value, language). Argument 1 can index the list of string tokens, and Argument 2 declares the language of speech for the text to speech conversion.

	stimulus = gTTS(numbers[i], lang = 'en')

Save this stimulus speech object as an MP3 or MP4 file using the save(filename) function from the gTTS package. 
	
	stimulus.save("mixed_signals_numbers_%s.mp3" % numbers[i])

	OR

	stimulus.save("mixed_signals_numbers_%s.mp4" % numbers[i])

Where %s modulates a string given by the indexed token from a list. 
