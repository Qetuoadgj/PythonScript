# -*- coding: utf8 -*-

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
    # удаление повторяющихся пробелов
    string = re.sub(r'[\t]+', ' ', string)
    string = re.sub(r'[\s]+', ' ', string)
    # возвращение результата
    return string

format = '%01d'
start_num = 1
end_num = 30
expression = notepad.prompt(
  ''.decode('utf-8').encode('cp1251'),
  'Ввод данных:'.decode('utf-8').encode('cp1251'),
  ('format = %s' + '\r\n' + 'start_num = %d' + '\r\n' + 'end_num = %d' + '\r\n') % (format, start_num, end_num)
)

if expression != None:
  expression = re.sub('\r\n', '; ', expression)
  list = expression.split('; ')

  eqString = r'([\s\t]+)?=([\s\t]+)?'

  format = re.sub(r'format' + eqString, '', list[0])
  format = trim(format)

  start_num = re.sub(r'start_num' + eqString, '', list[1])
  start_num = trim(start_num)
  start_num = int(start_num)
  end_num = re.sub(r'end_num' + eqString, '', list[2])
  end_num = trim(end_num)
  end_num = int(end_num)

  # First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
  editor.beginUndoAction()

  text = editor.getSelText()
  # matchText = r'^(.*?)(\d+)[.](.*)$'
  matchText = r'^(.*\/)(\d+)\.(.*)$'
  url, ext = re.match( matchText, text, re.M).group(1,3)
  ext = trim(ext)

  editor.appendText('\r\n')
  for count in range(start_num, end_num+1):
    number = format % count
    string = '<img src="%s%s.%s"></img>' % (url, number, ext)
    editor.appendText(string + '\r\n')
    console.write(string + '\r\n')

  # End the undo action, so Ctrl-Z will undo the above actions
  editor.endUndoAction()
  # Turn the undo recorder back on.
  editor.setUndoCollection(1)
