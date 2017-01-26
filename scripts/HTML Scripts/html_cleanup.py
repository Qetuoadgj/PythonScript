# -*- coding: utf8 -*-

console.show()
console.clear()

import re

Notepad = notepad
Editor = editor

SCRIPT_NAME = 'Cleanup HTML'
SCRIPT_VERSION = '1.0.1'

CURRENT_FILE = notepad.getCurrentFilename()
FILE_ENCODING = Notepad.getEncoding()
OUTPUT_FILE = ''

COMMENTS = ''

HEADER = ''
HEADER = '%s Source File: %s (%s)\r\n%s\r\n' % (COMMENTS, CURRENT_FILE, FILE_ENCODING, HEADER)

# определение переменных
DELETE_TITLES = 1
DELETE_COMMENTED = 0

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
    # удаление повторяющихся пробелов
    string = re.sub(r'[\t]+', ' ', string)
    string = re.sub(r'[\s]+', ' ', string)
    # возвращение результата
    return string

expression = notepad.prompt(
  'delete_titles - удаление заголовков (0|1)\r\ndelete_commented - удаление закоментированных строк (1|0)'.decode('utf-8').encode('cp1251'),
  'Ввод данных:'.decode('utf-8').encode('cp1251'),
  ('delete_titles = %s' + '\r\n' + 'delete_commented = %s' + '\r\n') % (DELETE_TITLES, DELETE_COMMENTED)
)

if expression != None:
  expression = re.sub('\r\n', '; ', expression)
  list = expression.split('; ')

  DELETE_TITLES = re.sub(r'delete_titles' + eqString, '', list[0])
  DELETE_TITLES = trim(DELETE_TITLES)

  DELETE_COMMENTED = re.sub(r'delete_commented' + eqString, '', list[1])
  DELETE_COMMENTED = trim(DELETE_COMMENTED)

lineCount = 0
def foundSomething(m):
  global DELETE_TITLES
  global DELETE_COMMENTED

  global lineCount
  lineCount += 1
  selectionStart, selectionEnd = editor.getUserLineSelection()

  lineString = m.group(1)
  lineNumber = selectionStart + lineCount

  if (re.match( r'(.*?<!--.*)', lineString) and DELETE_COMMENTED == '1'):
    return ''

  elif re.match( r'(.*style="display: block;".*)', lineString):
    PREFIX, TAG, CLASS, ID, STYLE, SUFFIX = re.match( r'(.*?)<(.*?) class="(.*?)" id="(.*?)" (style="display: block;")>(.*)', lineString).group(1, 2, 3, 4, 5, 6)
    lineString = '%s<%s class="%s" id="%s"%s>%s' % (PREFIX, TAG, CLASS, ID, '', SUFFIX)

  elif re.match( r'(.* url=".*?".*)', lineString):
    PREFIX, TAG, CLASS, TITLE, SRC, CONTENT, URL, SUFFIX = re.match( r'(.*?)<(.*?) class="(.*?)" title="(.*?)" src="(.*?)" content="(.*?)" url="(.*?)".*?>(.*)', lineString).group(1, 2, 3, 4, 5, 6, 7, 8)
    if (DELETE_TITLES == '1'):
      TITLE = ''
    lineString = '%s<%s class="%s" title="%s" src="%s" content="%s" url="%s">%s' % (PREFIX, TAG, CLASS, TITLE, SRC, CONTENT, URL, SUFFIX)

  elif re.match( r'(.* content=".*?".*)', lineString):
    PREFIX, TAG, CLASS, TITLE, SRC, CONTENT, SUFFIX = re.match( r'(.*?)<(.*?) class="(.*?)" title="(.*?)" src="(.*?)" content="(.*?)".*?>(.*)', lineString).group(1, 2, 3, 4, 5, 6, 7)
    if (DELETE_TITLES == '1'):
      TITLE = ''
    lineString = '%s<%s class="%s" title="%s" src="%s" content="%s">%s' % (PREFIX, TAG, CLASS, TITLE, SRC, CONTENT, SUFFIX)

  # if lineString != m.group(1):
    # console.write( '%02d: %s\n' % (lineNumber, lineString) )

  return lineString + '\r\n'

def findMatches():
  # editor.rereplace(r'^(.*)$', foundSomething, 0, editor.positionFromLine(editor.getUserLineSelection()[0]), editor.positionFromLine(editor.getUserLineSelection()[1]), 0)
  editor.rereplace(r'^(.*)\r\n', foundSomething, 0, editor.positionFromLine(editor.getUserLineSelection()[0]), editor.positionFromLine(editor.getUserLineSelection()[1]), 0)

log('Started script: %s - v%s\r\n' % (SCRIPT_NAME, SCRIPT_VERSION))
log('Parsing File: %s (%s)\r\n' % (CURRENT_FILE, FILE_ENCODING))
log('DELETE_TITLES = %s\r\nDELETE_COMMENTED = %s\r\n' % (DELETE_TITLES, DELETE_COMMENTED))

# run a command from the menu.
notepad.menuCommand(MENUCOMMAND.LANG_HTML)

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
