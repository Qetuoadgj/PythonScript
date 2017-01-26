# -*- coding: cp1251 -*-

import re

console.show()
console.clear()

def trim(string):
  if string:
    # удаление кавычек
    string = re.sub(r'["]', '', string)
    # удаление начальных и замыкающих пробелов
    string = re.sub(r'^[\s\t]+', '', string)
    string = re.sub(r'[\s\t]+$', '', string)
    # удаление повтор¤ющихс¤ пробелов
    string = re.sub(r'[\t]+', ' ', string)
    string = re.sub(r'[\s]+', ' ', string)
    # возвращение результата
    return string

format = '%02d'
expression = notepad.prompt(
  '',
  'Ввод данных:',
  ('format = %s' + '\r\n') % (format)
)

if expression != None:

  # преобразование кодировки ANSI в UTF-8
  expression = expression.decode('cp1251').encode('utf-8')

  expression = re.sub('\r\n', '; ', expression)
  list = expression.split('; ')

  eqString = r'([\s\t]+)?=([\s\t]+)?'

  format = re.sub(r'format' + eqString, '', list[0])
  format = trim(format)

  # First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
  editor.beginUndoAction()

  text = editor.getSelText()
  url = re.match( r'^(.*?)(\d+)[.]jpg$', text, re.M).group(1)

  editor.appendText('\r\n')
  for count in range(1, 30+1):
    number = format % count
    string = '<img src="%s%s.jpg"></img>' % (url, number)
    editor.appendText(string + '\r\n')
    console.write(string + '\r\n')

  # End the undo action, so Ctrl-Z will undo the above actions
  editor.endUndoAction()
  # Turn the undo recorder back on.
  editor.setUndoCollection(1)
