# -*- coding: utf-8 -*-

import re
import urllib
'''
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
'''
console.show()
console.clear()

CountNumber = 0

def foundSomething(m):
  line = m.group(1)

  LINE = ''

  value = re.match( r'(.*:\/\/.*)', line, re.M|re.I)
  if value:
    value = value.group(1)

    # �������������� URL
    # value = urllib.unquote(value).decode('utf8')
    
    # �������� ���������� ��������
    # value = re.sub(r'^[ \t]+', '', value)
    # �������� ������������� ��������
    # value = re.sub(r'[\s\t]+', ' ', value)
    # ������ �������� '.mkv' �� '.720.mp4'
    value = re.sub(r'((.*)\.mkv$)', r'## \1\r\n\2.720.mp4', value)
    '''
    # �������� ��������� � ���������� ��������
    value = re.sub(r'^[\s\t]+', '', value)
    value = re.sub(r'[\s\t]+$', '', value)
    # �������� ������������� ��������
    value = re.sub(r'[\s\t]+', ' ', value)
    # �������� ������������� ������
    value = re.sub(r'(\])+', r']', value)
    value = re.sub(r'(\[)+', r'[', value)
    # �������� ������ �������� �� � ����� ������
    value = re.sub(r' (\])', r'\1', value)
    value = re.sub(r'(\]|\[) ', r'\1', value)
    # �������� ������ �������� �� � ����� ����������
    SIGNS = r'([;]|[:]|[,]|[=]|[@])'
    value = re.sub(r' ' + SIGNS, r'\1', value)
    value = re.sub(SIGNS + r' ', r'\1', value)
    # �������� ���������� ��������
    value = re.sub(SIGNS + r'$', r'', value)
    # ������ ������� ���������� ������������
    # value = re.sub(r'^\/target ', r'/t ', value)
    value = re.sub('target=', '@', value)
    value = re.sub('@assist', '@targettarget', value)
    value = re.sub(r'^\/cast ', r'/use ', value)
    '''
    LINE = (LINE + '%s' % value)
  else:
    LINE = line

  if LINE != line:
    global CountNumber
    CountNumber += 1
    console.write( '%s. %s\n' % (CountNumber, LINE) )

  return LINE

# First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
editor.beginUndoAction()

editor.rereplace(r'(.+)', foundSomething, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
# �������� ������ �����
# editor.rereplace(r'^\r\n', r'', 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
# editor.rereplace(r'\r\n([\s\t]+)?\r\n', r'\r\n', 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))

# End the undo action, so Ctrl-Z will undo the above actions
editor.endUndoAction()
# Turn the undo recorder back on.
editor.setUndoCollection(1)


# string='example.com?title=%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D0%B2%D0%B0%D1%8F+%D0%B7%D0%B0%D1%89%D0%B8%D1%82%D0%B0'
# URL_Decode(string)
