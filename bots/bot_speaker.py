import pyttsx3


def bot_speaker():
    while True:
        quest_valid = input(
            'Do you want to hear the audio of the text? (y/n) ')

        if quest_valid == 'y' or quest_valid == 'Y':
            with open('article/subject.txt', 'r', encoding="utf-8") as f:
                read_file = f.readlines()
            try:
                # Start the project
                engine = pyttsx3.init()

                # Control the velocity
                engine.setProperty("rate", 180)

                # Change the voice
                voices = engine.getProperty("voices")
                engine.setProperty("voice", voices[2].id)

                # start the audio
                engine.say(read_file)
                engine.runAndWait()
            finally:
                break
        else:
            break
