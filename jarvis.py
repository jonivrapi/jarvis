from pynput import keyboard
import os
import click

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
    
    shortcut = keyboard.HotKey.parse('<cmd>+`')
    
    hotkey = keyboard.HotKey(shortcut, on_activate)
    
    with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)
    ) as l:
        l.join()


@cli.command()
def say_hi():
    print('Hi!')
    

def on_activate():
    os.system("open -a /System/Applications/Utilities/Terminal.app")
    os.system("osascript -e 'tell application \"Terminal\" to set visible of every window to true'")