""" Duje Tadin's Lab: Mixed Signal Stimulus
University of Rochester
Rochester, NY
Department of Brain & Cognitive Sciences
Center for Visual Sciences

Initial Commit by: Aaron Huynh
Last Updated: 28 February 2022
"""

# install Google API Text-to-Speech package
# $ pip install gTTS

#imports Google API Text-to-Speech package
from gtts import gTTS

# list of stimulus for mixed signal experimental condition
numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'];

# For Loop iterates over the length of the list of items
for i in range(len(numbers)):
    # stimulus object is now a speech/audio object
    stimulus = gTTS(numbers[i], lang='en')
    # save stimulus as MP3 or MP4 file
    # %s modulates a string that is replaced by an index of the list during each loop iteration
    stimulus.save("mixed_signals_numbers_%s.mp3" % numbers[i])
    stimulus.save("mixed_signals_numbers_%s.mp4" % numbers[i])

# list of stimulus for mixed signal experimental condition
colors = ['Blue', 'Red', 'Orange', 'Yellow', 'Green', 'Purple', 'Pink', 'White', 'Black', ' Grey', 'Brown'];

# For Loop iterates over the length of the list of items
for i in range(len(colors)):
    # stimulus object is now a speech/audio object
    stimulus = gTTS(colors[i], lang='en')
    # save stimulus as MP3 or MP4 file
    # %s modulates a string that is replaced by an index of the list during each loop iteration
    stimulus.save("mixed_signals_colors_%s.mp3" % colors[i])
    stimulus.save("mixed_signals_colors_%s.mp4" % colors[i])

# list of stimulus for mixed signal experimental condition
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z'];

# For Loop iterates over the length of the list of items
for i in range(len(alphabet)):
    # stimulus object is now a speech/audio object
    stimulus = gTTS(alphabet[i], lang='en')
    # save stimulus as MP3 or MP4 file
    # %s modulates a string that is replaced by an index of the list during each loop iteration
    stimulus.save("mixed_signals_alphabet_%s.mp3" % alphabet[i])
    stimulus.save("mixed_signals_alphabet_%s.mp4" % alphabet[i])