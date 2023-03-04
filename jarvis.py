from pynput import keyboard
import os
import click
import speech_recognition as sr
import pyttsx3

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

@cli.command()
# @click.option('-l', '--length', type=int, help='Length of password to be generated')
# @click.option('-o', '--option', type=click.Choice(['1', '2', '3', '4']), default = '4',
#     help='''Options\n
#     1 - alphabetic lowercase\n
#     2 - alphabetic both cases\n
#     3 - alphanumeric\n
#     4 - alphanumeric + special characters'''
# )
def set_hotkey():
    def for_canonical(f):
        return lambda k: f(l.canonical(k))
    
    shortcut = keyboard.HotKey.parse('<cmd>+1')
    
    hotkey = keyboard.HotKey(shortcut, on_activate)
    
    with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)
    ) as l:
        l.join()


@cli.command()
def say_hi():
    print('Hi!')

@cli.command()
def speak():
    r = sr.Recognizer()
 
    # Function to convert text to
    # speech
    def SpeakText(command):
        voiceID = "com.apple.voice.compact.en-GB.Daniel"
        engine = pyttsx3.init('nsss')
        
        engine.setProperty('voice', voiceID)
        engine.say(command)

        engine.runAndWait()
        
        
    # Loop infinitely for user to
    # speak
    
    while(1):   
        
        # Exception handling to handle
        # exceptions at the runtime
        try:
            
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                #listens for the user's input
                audio2 = r.listen(source2)
                
                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                if 'jarvis' in MyText:
                    print("How can I help you sir?")
                    SpeakText("How can I help you sir?")

                if 'terminal' in MyText:
                    set_hotkey()
                    SpeakText("I have set your terminal hotkey?")

                if 'open chrome' in MyText:
                    os.system("open -a /Applications/Google\ Chrome.app")
    
                # print("Did you say ",MyText)
                # SpeakText(MyText)
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occurred")
    

def on_activate():
    os.system("open -a /System/Applications/Utilities/Terminal.app")
    os.system("osascript -e 'tell application \"Terminal\" to set visible of every window to true'")