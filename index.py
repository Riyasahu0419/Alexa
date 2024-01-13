import speech_recognition as sr
import pyttsx3
import pywhatkit
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    # except:
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Error with the request to Google Speech Recognition service; {e}")

        # pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    else:
        talk('Please say the command again.')
while True:
    run_alexa()



# //Install SpeechRecognition Module on Jupyter Notebook
# (It help for speech recognition from the microphone)
    
# //Install pyttsx3 Module on Jupyter Notebook
# (It Convert Text to Speech)
    
# //Install pywhatkit Module on Jupyter Notebook
# (It use for automation)
    
# //Install pyaudio Module on Jupyter Notebook
# (With PyAudio, you can easily use Python to play and record audio on a variety of platforms,
# such as Microsoft Windows, and Apple macOS)
# 