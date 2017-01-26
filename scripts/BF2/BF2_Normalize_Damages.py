# Adjust Damages.

# MaterialManager.createCell 1 2
# MaterialManager.damageMod 1'

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
                 'Damage multipliers',
                 'Power to = 1\r\nHuman_bodyarmour x2; Human_body x2; Human_head x1; Human_limbs x1; PR_BODYARMOR_POOR x2\r\nRound to = 2\r\nComment lines = 1')

expression = re.sub('\r\n', '; ', expression)
list = expression.split('; ')

Power = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[0], 0, 0)))
MULT_Human_bodyarmour = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[1], 0, 0)))
MULT_Human_body = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[2], 0, 0)))
MULT_Human_head = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[3], 0, 0)))
MULT_Human_limbs = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[4], 0, 0)))
MULT_PR_BODYARMOR_POOR = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[5], 0, 0)))
Round = int(abs(round(float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[6], 0, 0))))))
# Enable/Disable backup source lines in comments.
Comment=bool(float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[7], 0, 0))))

def Human_bodyarmour(m):
    try:
	#Get value from string
	value1 = float(m.group(5))
	# Normalizing value
	if abs(value1) > 1:
		value1 = round(pow(abs(value1), Power)*MULT_Human_bodyarmour, Round)*sign(value1)
	else:
		value1 = round(pow(abs(value1), 1/Power)*MULT_Human_bodyarmour, Round)*sign(value1)
	#Get normalized results
        if Comment and (Power!=1 or MULT_Human_bodyarmour!=0):
			return '%s%s %s %s\r\nrem MaterialManager.damageMod %s\r\nMaterialManager.damageMod %s' % ( m.group(1), m.group(2), m.group(3), m.group(4), m.group(5), value1)
        else:
			return '%s%s %s %s\r\nMaterialManager.damageMod %s' % ( m.group(1), m.group(2), m.group(3), m.group(4), value1)
    except:
        return m.group(0)
		
def Human_body(m):
    try:
	#Get value from string
	value1 = float(m.group(5))
	# Normalizing value
	if abs(value1) > 1:
		value1 = round(pow(abs(value1), Power)*MULT_Human_body, Round)*sign(value1)
	else:
		value1 = round(pow(abs(value1), 1/Power)*MULT_Human_body, Round)*sign(value1)
	#Get normalized results
        if Comment and (Power!=1 or MULT_Human_body!=0):
			return '%s%s %s %s\r\nrem MaterialManager.damageMod %s\r\nMaterialManager.damageMod %s' % ( m.group(1), m.group(2), m.group(3), m.group(4), m.group(5), value1)
        else:
			return '%s%s %s %s\r\nMaterialManager.damageMod %s' % ( m.group(1), m.group(2), m.group(3), m.group(4), value1)
    except:
        return m.group(0)
		
def Human_head(m):
    try:
	#Get value from string
	value1 = float(m.group(5))
	# Normalizing value
	if abs(value1) > 1:
		value1 = round(pow(abs(value1), Power)*MULT_Human_head, Round)*sign(value1)
	else:
		value1 = round(pow(abs(value1), 1/Power)*MULT_Human_head, Round)*sign(value1)
	#Get normalized results
        if Comment and (Power!=1 or MULT_Human_head!=0):
			return '%s%s %s %s\r\nrem MaterialManager.damageMod %s\r\nMaterialManager.damageMod %s' % ( m.group(1), m.group(2), m.group(3), m.group(4), m.group(5), value1)
        else:
			return '%s%s %s %s\r\nMaterialManager.damageMod %s' % ( m.group(1), m.group(2), m.group(3), m.group(4), value1)
    except:
        return m.group(0)
		
def Human_limbs(m):
    try:
	#Get value from string
	value1 = float(m.group(5))
	# Normalizing value
	if abs(value1) > 1:
		value1 = round(pow(abs(value1), Power)*MULT_Human_limbs, Round)*sign(value1)
	else:
		value1 = round(pow(abs(value1), 1/Power)*MULT_Human_limbs, Round)*sign(value1)
	#Get normalized results
        if Comment and (Power!=1 or MULT_Human_limbs!=0):
			return '%s%s %s %s\r\nrem MaterialManager.damageMod %s\r\nMaterialManager.damageMod %s' % ( m.group(1), m.group(2), m.group(3), m.group(4), m.group(5), value1)
        else:
			return '%s%s %s %s\r\nMaterialManager.damageMod %s' % ( m.group(1), m.group(2), m.group(3), m.group(4), value1)
    except:
        return m.group(0)
		
def PR_BODYARMOR_POOR(m):
    try:
	#Get value from string
	value1 = float(m.group(5))
	# Normalizing value
	if abs(value1) > 1:
		value1 = round(pow(abs(value1), Power)*MULT_PR_BODYARMOR_POOR, Round)*sign(value1)
	else:
		value1 = round(pow(abs(value1), 1/Power)*MULT_PR_BODYARMOR_POOR, Round)*sign(value1)
	#Get normalized results
        if Comment and (Power!=1 or MULT_PR_BODYARMOR_POOR!=0):
			return '%s%s %s %s\r\nrem MaterialManager.damageMod %s\r\nMaterialManager.damageMod %s' % ( m.group(1), m.group(2), m.group(3), m.group(4), m.group(5), value1)
        else:
			return '%s%s %s %s\r\nMaterialManager.damageMod %s' % ( m.group(1), m.group(2), m.group(3), m.group(4), value1)
    except:
        return m.group(0)

# First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
editor.beginUndoAction()

# (.*)(MaterialManager[.]createCell)[ \t](38|39|40|41|762|900|3012|3013|3050|3556|3762|3763|3900)[ \t](23)\r\nMaterialManager.damageMod[ \t]([0-9]*\.?[0-9]*)(.+)?
# \1\2 \3 \4\r\nMaterialManager.damageMod \5
# \1\2 \3 \4\r\nrem MaterialManager.damageMod \5\r\nMaterialManager.damageMod \5[*]2

str_Human_bodyarmour = '(.*)(MaterialManager[.]createCell)[ \t](38|39|40|41|762|900|3012|3013|3050|3556|3762|3763|3900)[ \t](23)\r\nMaterialManager.damageMod[ \t]([0-9]*\.?[0-9]*)(.+)?'
str_Human_body = '(.*)(MaterialManager[.]createCell)[ \t](38|39|40|41|762|900|3012|3013|3050|3556|3762|3763|3900)[ \t](24)\r\nMaterialManager.damageMod[ \t]([0-9]*\.?[0-9]*)(.+)?'
str_Human_head = '(.*)(MaterialManager[.]createCell)[ \t](38|39|40|41|762|900|3012|3013|3050|3556|3762|3763|3900)[ \t](25)\r\nMaterialManager.damageMod[ \t]([0-9]*\.?[0-9]*)(.+)?'
str_Human_limbs = '(.*)(MaterialManager[.]createCell)[ \t](38|39|40|41|762|900|3012|3013|3050|3556|3762|3763|3900)[ \t](77)\r\nMaterialManager.damageMod[ \t]([0-9]*\.?[0-9]*)(.+)?'
str_PR_BODYARMOR_POOR = '(.*)(MaterialManager[.]createCell)[ \t](38|39|40|41|762|900|3012|3013|3050|3556|3762|3763|3900)[ \t](3703)\r\nMaterialManager.damageMod[ \t]([0-9]*\.?[0-9]*)(.+)?'

if MULT_Human_bodyarmour!=0:
	if Comment and (Power!=1 or MULT_Human_bodyarmour!=0):
		editor.rereplace(str_Human_bodyarmour, Human_bodyarmour, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
	else:
		editor.rereplace(str_Human_bodyarmour, Human_bodyarmour, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
if MULT_Human_body!=0:
	if Comment and (Power!=1 or MULT_Human_body!=0):
		editor.rereplace(str_Human_body, Human_body, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
	else:
		editor.rereplace(str_Human_body, Human_body, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
if MULT_Human_head!=0:
	if Comment and (Power!=1 or MULT_Human_head!=0):
		editor.rereplace(str_Human_head, Human_head, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
	else:
		editor.rereplace(str_Human_head, Human_head, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
if MULT_Human_limbs!=0:
	if Comment and (Power!=1 or MULT_Human_limbs!=0):
		editor.rereplace(str_Human_limbs, Human_limbs, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
	else:
		editor.rereplace(str_Human_limbs, Human_limbs, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
if MULT_PR_BODYARMOR_POOR!=0:
	if Comment and (Power!=1 or MULT_PR_BODYARMOR_POOR!=0):
		editor.rereplace(str_PR_BODYARMOR_POOR, PR_BODYARMOR_POOR, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
	else:
		editor.rereplace(str_PR_BODYARMOR_POOR, PR_BODYARMOR_POOR, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))

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

if MULT_Human_bodyarmour!=0 and MULT_Human_bodyarmour!=0:
    console.write("Human_bodyarmour * %s\n" % MULT_Human_bodyarmour)
if MULT_Human_body!=0 and MULT_Human_body!=0:
    console.write("Human_body * %s\n" % MULT_Human_body)
if MULT_Human_head!=0 and MULT_Human_head!=0:
    console.write("Human_head * %s\n" % MULT_Human_head)
if MULT_Human_limbs!=0 and MULT_Human_limbs!=0:
    console.write("Human_limbs * %s\n" % MULT_Human_limbs)
if MULT_PR_BODYARMOR_POOR!=0 and MULT_PR_BODYARMOR_POOR!=0:
    console.write("PR_BODYARMOR_POOR * %s\n" % MULT_PR_BODYARMOR_POOR)
# console.write("END\n")
