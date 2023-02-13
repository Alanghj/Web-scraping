import pyttsx3



def bot_speaker():
    while True:
        quest_valid = input(
            'Do you want to hear the audio of the text? (y/n) ')

        if quest_valid == 'y' or quest_valid == 'Y':
            with open('article/subject.txt', 'r', encoding="utf-8") as f:
                read_file = f.readlines()

                engine = pyttsx3.init()
                engine.setProperty("rate", 180)

                voices = engine.getProperty("voices")
                engine.setProperty("voice", voices[2].id)

                engine.say(read_file)
                engine.runAndWait()
        else:
            break
    
