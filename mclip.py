#! python3
# mclip.py - A multi-clipboard program.
TEXT = {'ok': """It's Treason then""",
'yes': """Do it""",
'hi': """Hello There""",
'no':"""No, No, Noooooooooo""" }
import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: py mclip.py [keyphrase] - copy phrase text')
    sys.exit()
keyphrase = sys.argv[1] # first command line arg is the keyphrase
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(TEXT[keyphrase]+" Copied")
else:
    print('There is no text for ' + keyphrase)
sys.exit()