# Reduce deviations.

# ObjectTemplate.deviation.minDev       1'
# ObjectTemplate.deviation.setFireDev   1'  2'  3
# ObjectTemplate.deviation.setTurnDev   1'  2   3   4
# ObjectTemplate.deviation.setSpeedDev  1'  2   3   4
# ObjectTemplate.deviation.setMiscDev   1'  2'  3

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
                 'Devation multipliers',
                 'Power to = 0.5\r\nMinDev x0; FireDev x0.5; TurnDev x1; SpeedDev x1; MiscDev x1\r\nRound to = 2\r\nComment lines = 1')

expression = re.sub('\r\n', '; ', expression)
list = expression.split('; ')

Power = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[0], 0, 0)))
MULT_MinDev = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[1], 0, 0)))
MULT_FireDev = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[2], 0, 0)))
MULT_TurnDev = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[3], 0, 0)))
MULT_SpeedDev = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[4], 0, 0)))
MULT_MiscDev = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[5], 0, 0)))
Round = int(abs(round(float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[6], 0, 0))))))
# Enable/Disable backup source lines in comments.
Comment=bool(float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[7], 0, 0))))

def minDev(m):
    try:
	#Get value from string
	value1 = float(m.group(3))
	# Normalizing value
	if abs(value1) > 1:
		value1 = round(pow(abs(value1), Power)*MULT_MinDev, Round)*sign(value1)
	else:
		value1 = round(pow(abs(value1), 1/Power)*MULT_MinDev, Round)*sign(value1)
	#Get normalized results
        if Comment and (Power!=1 or minDev!=0):
            return '%s %s.minDev %s\n%s%s.minDev %s' % ( m.group(1)+'rem', m.group(2), float(m.group(3)), m.group(1), m.group(2), value1 )
        else:
            return '%s%s.minDev %s' % ( m.group(1), m.group(2), value1 )
    except:
        return m.group(0)

def setFireDev(m):
    try:
	#Get 3 values from string
	value1 = float(m.group(3))
	value2 = float(m.group(4))
	value3 = float(m.group(5))
	# Normalizing 2 of 3 values
	if abs(value1) > 1:
		value1 = round(pow(abs(value1), Power)*MULT_FireDev, Round)*sign(value1)
	else:
		value1 = round(pow(abs(value1), 1/Power)*MULT_FireDev, Round)*sign(value1)
	if abs(value2) > 1:
		value2 = round(pow(abs(value2), Power)*MULT_FireDev, Round)*sign(value2)
	else:
		value2 = round(pow(abs(value2), 1/Power)*MULT_FireDev, Round)*sign(value2)
	#Get normalized results
        if Comment and (Power!=1 or MULT_FireDev!=0):
            return '%s %s.setFireDev %s %s %s\n%s%s.setFireDev %s %s %s' % ( m.group(1)+'rem', m.group(2), float(m.group(3)), float(m.group(4)), float(m.group(5)), m.group(1), m.group(2), value1, value2, value3 )
        else:
            return '%s%s.setFireDev %s %s %s' % ( m.group(1), m.group(2), value1, value2, value3 )
    except:
        return m.group(0)

def setTurnDev(m):
    try:
	#Get 4 values from string
	value1 = float(m.group(3))
	value2 = float(m.group(4))
	value3 = float(m.group(5))
	value4 = float(m.group(6))
	# Normalizing 1 of 4 values
	if abs(value1) > 1:
		value1 = round(pow(abs(value1), Power)*MULT_TurnDev, Round)*sign(value1)
	else:
		value1 = round(pow(abs(value1), 1/Power)*MULT_TurnDev, Round)*sign(value1)
	#Get normalized results
        if Comment and (Power!=1 or MULT_TurnDev!=0):
            return '%s %s.setTurnDev %s %s %s %s\n%s%s.setTurnDev %s %s %s %s' % ( m.group(1)+'rem', m.group(2), float(m.group(3)), float(m.group(4)), float(m.group(5)), float(m.group(6)), m.group(1), m.group(2), value1, value2, value3, value4 )
        else:
            return '%s%s.setTurnDev %s %s %s %s' % ( m.group(1), m.group(2), value1, value2, value3, value4 )
    except:
        return m.group(0)

def setSpeedDev(m):
    try:
	#Get 4 values from string
	value1 = float(m.group(3))
	value2 = float(m.group(4))
	value3 = float(m.group(5))
	value4 = float(m.group(6))
	# Normalizing 1 of 4 values
	if abs(value1) > 1:
		value1 = round(pow(abs(value1), Power)*MULT_SpeedDev, Round)*sign(value1)
	else:
		value1 = round(pow(abs(value1), 1/Power)*MULT_SpeedDev, Round)*sign(value1)
	#Get normalized results
        if Comment and (Power!=1 or MULT_SpeedDev!=0):
            return '%s %s.setSpeedDev %s %s %s %s\n%s%s.setSpeedDev %s %s %s %s' % ( m.group(1)+'rem', m.group(2), float(m.group(3)), float(m.group(4)), float(m.group(5)), float(m.group(6)), m.group(1), m.group(2), value1, value2, value3, value4 )
        else:
            return '%s%s.setSpeedDev %s %s %s %s' % ( m.group(1), m.group(2), value1, value2, value3, value4 )
    except:
        return m.group(0)

def setMiscDev(m):
    try:
	#Get 3 values from string
	value1 = float(m.group(3))
	value2 = float(m.group(4))
	value3 = float(m.group(5))
	# Normalizing 2 of 3 values
	if abs(value1) > 1:
		value1 = round(pow(abs(value1), Power)*MULT_MiscDev, Round)*sign(value1)
	else:
		value1 = round(pow(abs(value1), 1/Power)*MULT_MiscDev, Round)*sign(value1)
	if abs(value2) > 1:
		value2 = round(pow(abs(value2), Power)*MULT_MiscDev, Round)*sign(value2)
	else:
		value2 = round(pow(abs(value2), 1/Power)*MULT_MiscDev, Round)*sign(value2)
	#Get normalized results
        if Comment and (Power!=1 or MULT_MiscDev!=0):
            return '%s %s.setMiscDev %s %s %s\n%s%s.setMiscDev %s %s %s' % ( m.group(1)+'rem', m.group(2), float(m.group(3)), float(m.group(4)), float(m.group(5)), m.group(1), m.group(2), value1, value2, value3 )
        else:
            return '%s%s.setMiscDev %s %s %s' % ( m.group(1), m.group(2), value1, value2, value3 )
    except:
        return m.group(0)

# First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
editor.beginUndoAction()

str_minDev = '(.*)(ObjectTemplate.*)[.]minDev[ \t]([0-9]*\.?[0-9]*)(.+)?'
str_setFireDev = '(.*)(ObjectTemplate.*)[.]setFireDev[ \t](.*)[ \t](.*)[ \t]([0-9]*\.?[0-9]+)(.+)?'
str_setTurnDev = '(.*)(ObjectTemplate.*)[.]setTurnDev[ \t](.*)[ \t](.*)[ \t](.*)[ \t]([0-9]*\.?[0-9]+)(.+)?'
str_setSpeedDev = '(.*)(ObjectTemplate.*)[.]setSpeedDev[ \t](.*)[ \t](.*)[ \t](.*)[ \t]([0-9]*\.?[0-9]+)(.+)?'
str_setMiscDev = '(.*)(ObjectTemplate.*)[.]setMiscDev[ \t](.*)[ \t](.*)[ \t]([0-9]*\.?[0-9]+)(.+)?'

if MULT_MinDev!=0:
	if Comment and (Power!=1 or MULT_MinDev!=0):
		editor.rereplace(str_minDev, minDev, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
	else:
		editor.rereplace(str_minDev, minDev, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
if MULT_FireDev!=0:
	if Comment and (Power!=1 or MULT_FireDev!=0):
		editor.rereplace(str_setFireDev, setFireDev, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
	else:
		editor.rereplace(str_setFireDev, setFireDev, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
if MULT_TurnDev!=0:
	if Comment and (Power!=1 or MULT_TurnDev!=0):
		editor.rereplace(str_setTurnDev, setTurnDev, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
	else:
		editor.rereplace(str_setTurnDev, setTurnDev, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
if MULT_SpeedDev!=0:
	if Comment and (Power!=1 or MULT_SpeedDev!=0):
		editor.rereplace(str_setSpeedDev, setSpeedDev, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
	else:
		editor.rereplace(str_setSpeedDev, setSpeedDev, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
if MULT_MiscDev!=0:
	if Comment and (Power!=1 or MULT_MiscDev!=0):
		editor.rereplace(str_setMiscDev, setMiscDev, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
	else:
		editor.rereplace(str_setMiscDev, setMiscDev, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))

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

if MULT_MinDev!=0 and MULT_MinDev!=0:
    console.write("minDev * %s\n" % MULT_MinDev)
if MULT_FireDev!=0 and MULT_FireDev!=0:
    console.write("setFireDev * %s\n" % MULT_FireDev)
if MULT_TurnDev!=0 and MULT_TurnDev!=0:
    console.write("setTurnDev * %s\n" % MULT_TurnDev)
if MULT_SpeedDev!=0 and MULT_SpeedDev!=0:
    console.write("setSpeedDev * %s\n" % MULT_SpeedDev)
if MULT_MiscDev!=0 and MULT_MiscDev!=0:
    console.write("setMiscDev * %s\n" % MULT_MiscDev)
# console.write("END\n")
