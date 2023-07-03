from gtts import gTTS
from playsound import playsound


def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    playsound(filename)


file = open("input.txt", "w")
while True:
    text = input()
    if text == "EOF":
        break
    file.write(text + "\n")
    filename = "output.mp3"
    text_to_speech(text, filename)
