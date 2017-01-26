# -*- coding: utf8 -*-

console.show()
console.clear()

import re

Notepad = notepad
Editor = editor

SCRIPT_NAME = 'Remove Attributes'
SCRIPT_VERSION = '1.0.0'

CURRENT_FILE = notepad.getCurrentFilename()
FILE_ENCODING = Notepad.getEncoding()
OUTPUT_FILE = ''

COMMENTS = ''

HEADER = ''
HEADER = '%s Source File: %s (%s)\r\n%s\r\n' % (COMMENTS, CURRENT_FILE, FILE_ENCODING, HEADER)

def log(message):
  message = re.sub(r'(.+)', COMMENTS + r' \1', message, re.M)
  console.write(message)

eqString = r'(\s+)?=(\s+)?'

def trim(string):
  if string:
    # удаление кавычек
    string = re.sub(r'["]', '', string)
    # удаление начальных и замыкающих пробелов
    string = re.sub(r'^[ \t]+', '', string)
    string = re.sub(r'[ \t]+$', '', string)
    # удаление повтор¤ющихс¤ пробелов
    string = re.sub(r'[\t]+', ' ', string)
    string = re.sub(r'[\s]+', ' ', string)
    # возвращение результата
    return string

lineCount = 0
def foundSomething(m):
  global lineCount
  lineCount += 1
  selectionStart, selectionEnd = editor.getUserLineSelection()

  lineString = m.group(1)
  lineNumber = selectionStart + lineCount

  match = re.match( r'(.*?)<(.*?) class="(.*?)" id="(.*?)" (style="display: block;")>(.*)', lineString)
  if match:
    PREFIX, TAG, CLASS, ID, STYLE, SUFFIX = match.group(1, 2, 3, 4, 5, 6)
    if (TAG):
      lineString = '%s<%s class="%s" id="%s"%s>%s' % (PREFIX, TAG, CLASS, ID, '', SUFFIX)
  
  match = re.match( r'(.*?)<(.*?) class="(.*?)" title="(.*?)" src="(.*?)" content="(.*?)".*?>(.*)', lineString)
  if match:
    PREFIX, TAG, CLASS, TITLE, SRC, CONTENT, SUFFIX = match.group(1, 2, 3, 4, 5, 6, 7)
    if (TAG):
      lineString = '%s<%s class="%s" title="%s" src="%s" content="%s">%s' % (PREFIX, TAG, CLASS, '', SRC, CONTENT, SUFFIX)

  # if lineString != m.group(1):
    # console.write( '%02d: %s\n' % (lineNumber, lineString) )

  return lineString

def findMatches():
  editor.rereplace(r'^(.*)$', foundSomething, 0, editor.positionFromLine(editor.getUserLineSelection()[0]), editor.positionFromLine(editor.getUserLineSelection()[1]), 0)

log('Started script: %s - v%s\r\n' % (SCRIPT_NAME, SCRIPT_VERSION))
log('Parsing File: %s (%s)\r\n' % (CURRENT_FILE, FILE_ENCODING))

# First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
editor.beginUndoAction()
findMatches()
# End the undo action, so Ctrl-Z will undo the above actions
editor.endUndoAction()
# Turn the undo recorder back on.
editor.setUndoCollection(1)

# text = 'Result was written in: %s\r\nGroups count: %d\r\nWithout groups: %d' % (OUTPUT_FILE, GROUPS_COUNT, NO_GROUPS_COUNT)
# log(text)
# Notepad.messageBox(text.decode('utf-8').encode('cp1251'), SCRIPT_NAME + ' v' + SCRIPT_VERSION)
