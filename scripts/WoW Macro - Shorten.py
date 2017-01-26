# -*- coding: cp1251 -*-

import re

def trim(string):
  if string:
    # �������� �������
    string = re.sub(r'["]', '', string)
    # �������� ��������� � ���������� ��������
    string = re.sub(r'^[\s\t]+', '', string)
    string = re.sub(r'[\s\t]+$', '', string)
    # �������� ������������� ��������
    string = re.sub(r'[\t]+', ' ', string)
    string = re.sub(r'[\s]+', ' ', string)
    # ����������� ����������
    return string

console.show()
console.clear()

# eqString = r'([\s\t]+)?=([\s\t]+)?'
SIGNS = r'([;]|[:]|[,]|[=]|[@])'

lineCount = 0
def foundSomething(m):
  global lineCount
  lineCount += 1
  selectionStart, selectionEnd = editor.getUserLineSelection()

  lineString = m.group(1)
  lineNumber = selectionStart + lineCount

  spacings = re.match( r'^(([ \t]+)?).*', lineString).group(1)

  url = trim(m.group(1))

  if re.match( r'(^\/.*)', lineString):
    # �������� ��������� � ���������� ��������
    lineString = re.sub(r'^[\s\t]+', '', lineString)
    lineString = re.sub(r'[\s\t]+$', '', lineString)
    # �������� ������������� ��������
    lineString = re.sub(r'[\s\t]+', ' ', lineString)
    # �������� ������������� ������
    lineString = re.sub(r'(\])+', r']', lineString)
    lineString = re.sub(r'(\[)+', r'[', lineString)
    # �������� ������ �������� �� � ����� ������
    lineString = re.sub(r' (\])', r'\1', lineString)
    lineString = re.sub(r'(\]|\[) ', r'\1', lineString)
    # �������� ������ �������� �� � ����� ����������
    lineString = re.sub(r' ' + SIGNS, r'\1', lineString)
    lineString = re.sub(SIGNS + r' ', r'\1', lineString)
    # ������ ������� ���������� ������������
    lineString = re.sub('target=', '@', lineString)
    lineString = re.sub('@assist', '@targettarget', lineString)
    lineString = re.sub(r'^\/cast ', r'/use ', lineString)
    # �������� ���������� ��������
    lineString = re.sub(SIGNS + r'$', '', lineString)

  if lineString != m.group(1):
    console.write( '%02d: %s\n' % (lineNumber, lineString) )

  return lineString

# First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
editor.beginUndoAction()

# run a command from the menu.
notepad.runMenuCommand('Language', 'WoW Macro')
notepad.runMenuCommand('����������'.decode('cp1251').encode('utf-8'), 'WoW Macro')

# notepad.runMenuCommand('Encoding', 'Convert to ANSI')
# notepad.save()

# '''
# ����� ������� ��������� �����
editor.rereplace(r'\r\n([ \t]+)?\r\n', r'\r\n', 0, editor.positionFromLine(editor.getUserLineSelection()[0]), editor.positionFromLine(editor.getUserLineSelection()[1]), 0)
editor.rereplace(r'^\r\n', '', 0, editor.positionFromLine(editor.getUserLineSelection()[0]), editor.positionFromLine(editor.getUserLineSelection()[1]), 0)
editor.rereplace(r'^(.*)$', foundSomething, 0, editor.positionFromLine(editor.getUserLineSelection()[0]), editor.positionFromLine(editor.getUserLineSelection()[1]), 0)
# '''

# notepad.runMenuCommand('Encoding', 'Convert to UTF-8')

# End the undo action, so Ctrl-Z will undo the above actions
editor.endUndoAction()
# Turn the undo recorder back on.
editor.setUndoCollection(1)
