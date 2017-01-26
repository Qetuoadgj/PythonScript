# -*- coding: cp1251 -*-

import re

expression = notepad.prompt(
  '',
  '',
  # '1 2 3 4 5' + '\r\n' + 'A B C D E' + '\r\n' + u'А Б В Г Д'.encode('cp1251')+ '\r\n' + u'А Б В Г Д'.encode('utf-8')
  '1 2 3 4 5' + '\r\n' + 'A B C D E' + '\r\n' + 'А Б В Г Д'
)

if expression != None:

  console.show()
  console.clear()
  
  # alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
  # alphabet = u'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.encode('utf-8')
  alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.decode('cp1251').encode('utf-8')
  
  expression = expression.decode('cp1251').encode('utf-8')
  
  STRING = alphabet + '\r\n' + expression + '\r\n' + expression
  
   # First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
  editor.beginUndoAction()
  
  console.write( '%s\n' % STRING )
  print( '%s\n' % STRING )
  
  # End the undo action, so Ctrl-Z will undo the above actions
  editor.endUndoAction()
  # Turn the undo recorder back on.
  editor.setUndoCollection(1)
  