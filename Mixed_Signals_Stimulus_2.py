""" Duje Tadin's Lab: Mixed Signal Stimulus
University of Rochester
Rochester, NY
Department of Brain & Cognitive Sciences
Center for Visual Sciences

Initial Commit by: Aaron Huynh
Last Updated: 01 March 2022
"""

# install Google API Text-to-Speech package
# $ pip install gTTS

# imports Google API Text-to-Speech package
from gtts import gTTS


def text_to_mp3(items):
    for x in range(len(items)):
        stim = gTTS(items[x], lang='en')
        stim.save('mixed_signals_%s.mp3' % items[x])


def text_to_mp4(items):
    for x in range(len(items)):
        stim = gTTS(items[x], lang='en')
        stim.save('mixed_signals_%s.mp4' % items[x])


def main():
    numbers = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
    colors = ['Blue', 'Red', 'Orange', 'Yellow', 'Green', 'Purple', 'Pink', 'White', 'Black', ' Grey', 'Brown']
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']

    text_to_mp3(numbers)
    text_to_mp4(numbers)

    text_to_mp3(colors)
    text_to_mp4(colors)

    text_to_mp3(alphabet)
    text_to_mp4(alphabet)


if __name__ == "__main__":
    main()
