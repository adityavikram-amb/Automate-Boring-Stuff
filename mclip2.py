#! python3
# mclip.py - A multi-clipboard program.
# Star Wars- Interupt on "stop" 



import pyperclip
TEXT = {'ok': """It's Treason then""",
'yes': """Do it""",
'hi': """Hello There""",
'no':"""No, No, Noooooooooo""" }
keyphrase="start"
while(keyphrase != "stop"):
    keyphrase = pyperclip.paste()
    if keyphrase in TEXT:
        pyperclip.copy(TEXT[keyphrase])

pyperclip.copy("Terminated")
#    print(TEXT[keyphrase]+" Copied")
