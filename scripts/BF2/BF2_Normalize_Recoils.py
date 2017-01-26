# Reduce recoils.

# ObjectTemplate.recoil.recoilForceUp           CRD_UNIFORM / 1' / 2' / 3
# ObjectTemplate.recoil.recoilForceLeftRight    CRD_UNIFORM / 1' / 2' / 3'

console.show()
console.clear()

# get sign of a number by Greg Pinero
# http://www.answermysearches.com/python-how-to-get-the-sign-of-a-number/35/

# Here's a better way provided by Florent Guillaume:
def sign(number):return cmp(number,0)

# Here is my original method:
# def sign(number):
    # """Will return 1 for positive,
    # -1 for negative, and 0 for 0"""
    # try:return number/abs(number)
    # except ZeroDivisionError:return 0

import re

# Count the number of characters, words and lines in the current editor window of Notepad++.
# http://www.sivachandran.in/2012/04/scripting-notepad-with-python.html
from Npp import *
def Count(string):
	numChars = 0
	numWords = 0
	numLines = 0

	editorContent = editor.getText()
	for line in editorContent.splitlines():
	  numLines += 1
	  for word in re.findall(string, line):
		numWords += 1
		numChars += len(word)
	return (numChars, numWords, numLines)

# notepad.messageBox("Number of characters: %d \nNumber of words: %d \nNumber of lines: %d" % Count("[a-zA-Z0-9]+"))
# notepad.messageBox("Number of characters: %d \nNumber of words: %d \nNumber of lines: %d" % (Count("[a-zA-Z0-9]+")[0],Count("[a-zA-Z0-9]+")[1],Count("[a-zA-Z0-9]+")[2]))

# Get values from prompt window
expression = notepad.prompt(
                 'Set multipliers or use "0" values to skip positions.',
                 'Recoil multipliers',
                 'Power to = 0.5\r\nForceUp x1; ForceLeftRight x1\r\nRound to = 2\r\nComment lines = 1')

expression = re.sub('\r\n', '; ', expression)
list = expression.split('; ')

Power = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[0], 0, 0)))
MULT_ForceUp = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[1], 0, 0)))
MULT_ForceLeftRight = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[2], 0, 0)))
Round = int(abs(round(float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[3], 0, 0))))))
# Enable/Disable backup source lines in comments.
Comment=bool(float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[4], 0, 0))))

def recoilForceUp(m):
    try:
	#Get 3 values from string
	value1 = float(m.group(3))
	value2 = float(m.group(4))
	value3 = float(m.group(5))
	# Normalizing 2 of 3 values
	if abs(value1) > 1:
		value1 = round(pow(abs(value1), Power)*MULT_ForceUp, Round)*sign(value1)
	else:
		value1 = round(pow(abs(value1), 1/Power)*MULT_ForceUp, Round)*sign(value1)
	if abs(value2) > 1:
		value2 = round(pow(abs(value2), Power)*MULT_ForceUp, Round)*sign(value2)
	else:
		value2 = round(pow(abs(value2), 1/Power)*MULT_ForceUp, Round)*sign(value2)
	#Get normalized results
        # if Comment and MULT_ForceUp!=1:
        if Comment and (Power!=1 or MULT_ForceUp!=0):
			return '%s %s CRD_UNIFORM/%s/%s/%s\n%s%s CRD_UNIFORM/%s/%s/%s' % ( m.group(1)+'rem', m.group(2), float(m.group(3)), float(m.group(4)), float(m.group(5)), m.group(1), m.group(2), value1, value2, value3 )
        else:
			return '%s%s CRD_UNIFORM/%s/%s/%s' % ( m.group(1), m.group(2), value1, value2, value3 )
    except:
        return m.group(0)

def recoilForceLeftRight(m):
    try:
	#Get 3 values from string
	value1 = float(m.group(3))
	value2 = float(m.group(4))
	value3 = float(m.group(5))
	# Normalizing 3 of 3 values
	if abs(value1) > 1:
		value1 = round(pow(abs(value1), Power)*MULT_ForceLeftRight, Round)*sign(value1)
	else:
		value1 = round(pow(abs(value1), 1/Power)*MULT_ForceLeftRight, Round)*sign(value1)
	if abs(value2) > 1:
		value2 = round(pow(abs(value2), Power)*MULT_ForceLeftRight, Round)*sign(value2)
	else:
		value2 = round(pow(abs(value2), 1/Power)*MULT_ForceLeftRight, Round)*sign(value2)
	if abs(value3) > 1:
		value3 = round(pow(abs(value3), Power)*MULT_ForceLeftRight, Round)*sign(value3)
	else:
		value3 = round(pow(abs(value3), 1/Power)*MULT_ForceLeftRight, Round)*sign(value3)
	#Get normalized results
	# if Comment and MULT_ForceLeftRight!=1:
	if Comment and (Power!=1 or MULT_ForceLeftRight!=0):
            return '%s %s CRD_UNIFORM/%s/%s/%s\n%s%s CRD_UNIFORM/%s/%s/%s' % ( m.group(1)+'rem', m.group(2), float(m.group(3)), float(m.group(4)), float(m.group(5)), m.group(1), m.group(2), value1, value2, value3 )
        else:
            return '%s%s CRD_UNIFORM/%s/%s/%s' % ( m.group(1), m.group(2), value1, value2, value3 )
    except:
        return m.group(0)

# First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
editor.beginUndoAction()

str_ForceLeftRight = '(.*)(ObjectTemplate.*[.]recoilForceLeftRight)[ \t]CRD_UNIFORM[ \t/](.*)[ \t/](.*)[ \t/]([0-9]*\.?[0-9]+)(.+)?'
str_ForceUp = '(.*)(ObjectTemplate.*[.]recoilForceUp)[ \t]CRD_UNIFORM[ \t/](.*)[ \t/](.*)[ \t/]([0-9]*\.?[0-9]+)(.+)?'

if MULT_ForceUp!=0:
	if Comment and (Power!=1 or MULT_ForceUp!=0):
		editor.rereplace(str_ForceUp, recoilForceUp, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
	else:
		editor.rereplace(str_ForceUp, recoilForceUp, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
if MULT_ForceLeftRight!=0:
	if Comment and (Power!=1 or MULT_ForceLeftRight!=0):
		editor.rereplace(str_ForceLeftRight, recoilForceLeftRight, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
	else:
		editor.rereplace(str_ForceLeftRight, recoilForceLeftRight, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))

# End the undo action, so Ctrl-Z will undo the above two actions
editor.endUndoAction()
# Turn the undo recorder back on.
editor.setUndoCollection(1)

# Write to the console window
# console.write("START\n")
if Comment:
	console.write("Comments - %s\n" % 'Enabled')
else:
	console.write("Comments - %s\n" % 'Disabled')

if Power!=1:
	console.write('All values powered by %s\n' % Power)

if MULT_ForceUp!=0 and MULT_ForceUp!=0:
    console.write("ForceUp * %s\n" % MULT_ForceUp)
if MULT_ForceLeftRight!=0 and MULT_ForceLeftRight!=0:
    console.write("ForceLeftRight * %s\n" % MULT_ForceLeftRight)
# console.write("END\n")
