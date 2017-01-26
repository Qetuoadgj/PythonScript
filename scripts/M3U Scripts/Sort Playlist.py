# -*- coding: utf8 -*-

console.show()
console.clear()

import re

Notepad = notepad
Editor = editor

SCRIPT_NAME = 'Sort Playlist'
SCRIPT_VERSION = '1.0.0'

CURRENT_FILE = notepad.getCurrentFilename()
FILE_ENCODING = Notepad.getEncoding()
OUTPUT_FILE = ''

COMMENTS = '##'

HEADER = '#EXTM3U'
HEADER = '%s Source File: %s (%s)\r\n%s\r\n' % (COMMENTS, CURRENT_FILE, FILE_ENCODING, HEADER)

GROUPS_COUNT = 0
NO_GROUPS_COUNT = 0

def log(message):
  message = re.sub(r'(.+)', COMMENTS + r' \1', message, re.M)
  console.write(message)

def convertToString(string):
  # Escaped := ["\", ".", "*", "?", "+", "[", "]", "{", "}", "|", "(", ")", "^", "$"]
  # string = re.sub(r'\\', '\\',  string)
  string = re.sub(r'\.', '\.',  string)
  string = re.sub(r'\*', '\*',  string)
  string = re.sub(r'\?', '\?',  string)
  string = re.sub(r'\+', '\+',  string)
  string = re.sub(r'\[', '\[',  string)
  string = re.sub(r'\]', '\]',  string)
  string = re.sub(r'\{', '\{',  string)
  string = re.sub(r'\}', '\}',  string)
  string = re.sub(r'\|', '\|',  string)
  string = re.sub(r'\(', '\(',  string)
  string = re.sub(r'\)', '\)',  string)
  string = re.sub(r'\^', '\^',  string)
  string = re.sub(r'\$', '\$',  string)
  return string

def removeEmptyLines(lineString, removeCommented):
  if (removeCommented == 1):
    # skip comments
    lineString = re.sub(r'.*' + COMMENTS + '.*\s+', r'', lineString)
  else:
    lineString = re.sub(r'(#EXTINF:.*\s+)((.*## .*\s+)+)(.*://.*)', r'\1\4\r\n\2', lineString)
  lineString = re.sub(r'[\r\n]+', '\r\n', lineString)
  return lineString

def writeOutput():
  outputString = ''
  if GROUPS_COUNT > 1:
    # notepad.new()

    if ANSWER == 6:
      Editor.clearAll()
    elif ANSWER == 7:
      notepad.new()

    # editor.appendText(HEADER + '\r\n')
    outputString = outputString + HEADER + '\r\n'

    notepad.runMenuCommand('Language', 'M3U')
    notepad.runMenuCommand('Синтаксисы', 'M3U')

    global OUTPUT_FILE
    outputFile = notepad.getCurrentFilename()
    OUTPUT_FILE = outputFile

    for index, item in enumerate(lines):
      number = 1 + index
      result = COMMENTS + ' %d:\r\n%s' % (number, item)

      notepad.activateFile(outputFile)

      # editor.appendText(result + '\r\n')
      outputString = outputString + result + '\r\n'

    start = number
    for index, item in enumerate(noGroups):
      number = 1 + index + start
      result = COMMENTS + ' %d:\r\n%s' % (number, item)

      notepad.activateFile(outputFile)

      # editor.appendText(result + '\r\n')
      outputString = outputString + result + '\r\n'

  editor.appendText(outputString)

lines = []
def addToList(lineString):
  header, url = lineString.group(1, 2)
  # header = removeEmptyLines(header, 0)
  # url = removeEmptyLines(url, 0)

  if (header and url):
    lineString = '%s\r\n%s' % (header, url)

    lines.append(removeEmptyLines(lineString, 0))

def sortByGroups():
  if GROUPS_COUNT > 0:
    for index, item in enumerate(groups):
      editor.research('(.*#EXTINF:.*' + 'group-title="%s"' % convertToString(item) +'.*)\s+' + '((.*://.*(\s+)?)+)', addToList, 0, editor.positionFromLine(editor.getUserLineSelection()[0]), editor.positionFromLine(editor.getUserLineSelection()[1]), 0)

iterations = 0
iterations_max = 1
iterations_step = -1

eqString = r'(\s+)?=(\s+)?'

groups = []
noGroups = []
def parseMatches(lineString):

  if iterations < iterations_max:

    global iterations
    iterations = iterations + iterations_step

    header, url = lineString.group(1, 2)
    # header = removeEmptyLines(header, 0)
    # url = removeEmptyLines(url, 0)

    if (header and url):
      lineString = '%s\r\n%s' % (header, url)

      group = re.match( r'.*group-title' + eqString + r'"(.+?)".*', header)
      if group:
        group = group.group(3)

        if group not in groups:
          groups.append(group)

          global GROUPS_COUNT
          GROUPS_COUNT = GROUPS_COUNT + 1
      else:
        lineString = re.sub('group-title=""', '', lineString)
        noGroups.append(removeEmptyLines(lineString, 0))

        global NO_GROUPS_COUNT
        NO_GROUPS_COUNT = NO_GROUPS_COUNT + 1


def findMatches():
  editor.research('(.*#EXTINF:.*)\s+((.*://.*(\s+)?)+)', parseMatches, 0, editor.positionFromLine(editor.getUserLineSelection()[0]), editor.positionFromLine(editor.getUserLineSelection()[1]), 0)

log('Started script: %s - v%s\r\n' % (SCRIPT_NAME, SCRIPT_VERSION))
log('Parsing File: %s (%s)\r\n' % (CURRENT_FILE, FILE_ENCODING))

ANSWER = Notepad.messageBox('Да - Перезаписать текущий файл\r\nНет - Создать новый файл\r\nОтмена - Выход'.decode('utf-8').encode('cp1251'), SCRIPT_NAME + ' v' + SCRIPT_VERSION, MESSAGEBOXFLAGS.ICONQUESTION | MESSAGEBOXFLAGS.YESNOCANCEL)

if ANSWER != 2:
  findMatches()
  sortByGroups()
  writeOutput()

  if GROUPS_COUNT == 1:
    text = 'There is only one group.'
  elif GROUPS_COUNT > 0:
    text = 'Result was written in: %s\r\nGroups count: %d\r\nWithout groups: %d' % (OUTPUT_FILE, GROUPS_COUNT, NO_GROUPS_COUNT)
  else:
    text = 'No groups found.'

  log(text)
  Notepad.messageBox(text.decode('utf-8').encode('cp1251'), SCRIPT_NAME + ' v' + SCRIPT_VERSION)
