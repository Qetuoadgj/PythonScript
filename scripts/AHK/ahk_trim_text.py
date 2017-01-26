# -*- coding: cp1251 -*-

console.show()
console.clear()

import re

lineCount = 0

start = '; '
space = ' ';
symbol_sign = '-'
symbol_num = 40

def foundSomething(m):
  global lineCount
  global symbol_num
  lineCount += 1
  selectionStart, selectionEnd = editor.getUserLineSelection()

  lineString = m.group(1)
  lineNumber = selectionStart + lineCount

  lineString = re.sub(r';', ';~', lineString)
  lineString = re.sub(r';[ ~]+', '; ', lineString)

  lineString = re.sub(r'[ ]+,', ',', lineString)
  lineString = re.sub(r',', ', ', lineString)
  lineString = re.sub(r',[ ]+', ', ', lineString)
  lineString = re.sub(r',[ ]+', ',', lineString)
  lineString = re.sub(r'(Gui,(.*?):)[ ]+', r'\1', lineString)

  # lineString = re.sub(r'; -[-]+', '; --------------------', lineString)
  if re.match( r'.*; -[-]+', lineString):
    symbol_num_g = symbol_num
    symbol_group_f = ''
    symbol_num_f = symbol_num_g - len(start) + 1
    for num in range(1, symbol_num_f):
      symbol_group_f = symbol_group_f + symbol_sign
    lineString = re.sub(r'; -['+symbol_sign+']+', start+symbol_group_f, lineString)

  if re.match( r'; -['+symbol_sign+']+ (.*?)', lineString):
    symbol_num_g = symbol_num
    symbol_group_l = ''
    symbol_group_r = ''
    title = re.sub(r'; -['+symbol_sign+']+ (.*?)[ ]+['+symbol_sign+']+', r'\1', lineString)
    symbol_num_g = symbol_num_g - len(start) - len(space)*2 - len(title) + 1
    symbol_num_l = int(symbol_num_g/2)
    symbol_num_r = symbol_num_g - symbol_num_l
    for num in range(1, symbol_num_l):
      symbol_group_l = symbol_group_l + symbol_sign
    for num in range(1, symbol_num_r):
      symbol_group_r = symbol_group_r + symbol_sign
    centered = (start + symbol_group_l + space + title + space + symbol_group_r)
    lineString = re.sub(r'; -['+symbol_sign+']+ .*', centered, lineString)

  lineString = re.sub(r'[ \t]+$', '', lineString)

  if lineString != m.group(1):
    console.write( '%02d: %s\n' % (lineNumber, lineString) )

  return lineString

# First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
editor.beginUndoAction()

# run a command from the menu.
# notepad.runMenuCommand('Language', 'WoW Macro')
# notepad.runMenuCommand('Синтаксисы'.decode('cp1251').encode('utf-8'), 'WoW Macro')

# notepad.runMenuCommand('Encoding', 'Convert to ANSI')
# notepad.save()

# '''
# вызов функции обработки строк
# editor.rereplace(r'\r\n([ \t]+)?\r\n', r'\r\n', 0, editor.positionFromLine(editor.getUserLineSelection()[0]), editor.positionFromLine(editor.getUserLineSelection()[1]), 0)
# editor.rereplace(r'^\r\n', '', 0, editor.positionFromLine(editor.getUserLineSelection()[0]), editor.positionFromLine(editor.getUserLineSelection()[1]), 0)
editor.rereplace(r'^(.*)$', foundSomething, 0, editor.positionFromLine(editor.getUserLineSelection()[0]), editor.positionFromLine(editor.getUserLineSelection()[1]), 0)
# '''

# notepad.runMenuCommand('Encoding', 'Convert to UTF-8')

# End the undo action, so Ctrl-Z will undo the above actions
editor.endUndoAction()
# Turn the undo recorder back on.
editor.setUndoCollection(1)
