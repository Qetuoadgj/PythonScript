# -*- coding: utf8 -*-

import re

def trim(string):
  if string:
    # удаление кавычек
    string = re.sub(r'["]', '', string)
    # удаление начальных и замыкающих пробелов
    string = re.sub(r'^\s+', '', string)
    string = re.sub(r'\s+$', '', string)
    # удаление повторяющихся пробелов
    string = re.sub(r'[\t]+', ' ', string)
    string = re.sub(r'\s+', ' ', string)
    # возвращение результата
    return string

# определение переменных
GROUP_TITLE   = ""
TVG_LOGO      = ""
AUDIO_TRACK   = ""
TVG_NAME      = ""
ASPECT_RATIO  = ""
TITLE         = ""

expression = notepad.prompt(
  'title = ЗАГОЛОВОК  | -1 (автонумерация) | +1 (группировка) | -0 (удаление параметра) | Пустой (без изменений)'.decode('utf-8').encode('cp1251'),
  'Ввод данных:'.decode('utf-8').encode('cp1251'),
  ('group-title = %s' + '\r\n' + 'aspect-ratio = %s' + '\r\n' + 'tvg-logo = %s' + '\r\n' + 'title = %s') % (GROUP_TITLE, ASPECT_RATIO, TVG_LOGO, TITLE)
)

if expression != None:

  # преобразование кодировки ANSI в UTF-8
  expression = expression.decode('cp1251').encode('utf-8')

  console.show()
  console.clear()

  expression = re.sub('\r\n', '; ', expression)
  list = expression.split('; ')

  eqString = r'(\s+)?=(\s+)?'

  # получение переменных из диалогового окна
  # GROUP_TITLE   = re.sub(r'group-title' + eqString, '', list[0])
  # GROUP_TITLE   = trim(GROUP_TITLE)

  # TVG_LOGO      = re.sub(r'tvg-logo' + eqString, '', list[1])
  # TVG_LOGO      = trim(TVG_LOGO)

  # AUDIO_TRACK   = re.sub(r'audio-track' + eqString, '', list[2])
  # AUDIO_TRACK   = trim(AUDIO_TRACK)

  # TVG_NAME      = re.sub(r'tvg-name' + eqString, '', list[3])
  # TVG_NAME      = trim(TVG_NAME)

  # ASPECT_RATIO  = re.sub(r'aspect-ratio' + eqString, '', list[4])
  # ASPECT_RATIO  = trim(ASPECT_RATIO)

  # TITLE         = re.sub(r'title' + eqString, '', list[5])
  # TITLE         = trim(TITLE)

  # Comment     = re.sub('["A-Za-z\s_=-]', '', list[1], 0, 0)
  # Comment     = bool(int(Comment))

  GROUP_TITLE   = re.sub(r'group-title' + eqString, '', list[0])
  GROUP_TITLE   = trim(GROUP_TITLE)

  ASPECT_RATIO  = re.sub(r'aspect-ratio' + eqString, '', list[1])
  ASPECT_RATIO  = trim(ASPECT_RATIO)

  TVG_LOGO      = re.sub(r'tvg-logo' + eqString, '', list[2])
  TVG_LOGO      = trim(TVG_LOGO)

  TITLE         = re.sub(r'title' + eqString, '', list[3])
  TITLE         = trim(TITLE)

  lineCount = 0
  count = 0
  # groups = []

  def foundSomething(m):
    global lineCount
    lineCount += 1
    selectionStart, selectionEnd = editor.getUserLineSelection()

    lineString = m.group(1)
    lineNumber = selectionStart + lineCount

    LINE = lineString

    # определение переменных, которым будут присваиваться значения внутри функции
    _TITLE        = TITLE
    _GROUP_TITLE  = GROUP_TITLE

    if re.match( r'(#EXTINF:.*)', lineString):
      LINE = '#EXTINF: -1'

      if (_TITLE):
        if(_TITLE == "-1"):
          global count
          count = count + 1
          _TITLE = ('___%04d___' % count)
        elif(_TITLE == "+1"):
          value = re.match( r'.*,(\s+)?(.*?):.*', lineString)
          if value:
            value = value.group(2)
            value = trim(value)
            _GROUP_TITLE = ('%s' % value)
          else:
            _GROUP_TITLE = ""

          value = re.match( r'.*,(\s+)?.*?:(.*)', lineString)
          if value:
            value = value.group(2)
            value = trim(value)
            _TITLE = ('%s' % value)
          else:
            _TITLE = ""

      if (_GROUP_TITLE and _GROUP_TITLE != ""):
        if(_GROUP_TITLE == "-0"):
          LINE = LINE
        else:
          LINE = (LINE + ' group-title="%s"' % _GROUP_TITLE)
      else:
        value = re.match( r'.*group-title' + eqString + r'"(.+?)".*', lineString)
        if value:
          value = value.group(3)
          value = trim(value)
          '''
          group = value
          if value not in groups:
            groups.append(group)
          '''
          LINE = (LINE + ' group-title="%s"' % value)

      if (TVG_LOGO and TVG_LOGO != ""):
        if(TVG_LOGO == "-0"):
          LINE = LINE
        else:
          LINE = (LINE + ' tvg-logo="%s"' % TVG_LOGO)
      else:
        value = re.match( r'.*tvg-logo' + eqString + r'"(.+?)".*', lineString)
        if value:
          value = value.group(3)
          value = trim(value)
          LINE = (LINE + ' tvg-logo="%s"' % value)

      if (AUDIO_TRACK and AUDIO_TRACK != ""):
        if(AUDIO_TRACK == "-0"):
          LINE = LINE
        else:
          LINE = (LINE + ' audio-track="%s"' % AUDIO_TRACK)
      else:
        value = re.match( r'.*audio-track' + eqString + r'"(.+?)".*', lineString)
        if value:
          value = value.group(3)
          value = trim(value)
          LINE = (LINE + ' audio-track="%s"' % value)

      if (TVG_NAME and TVG_NAME != ""):
        if(TVG_NAME == "-0"):
          LINE = LINE
        else:
          LINE = (LINE + ' tvg-name="%s"' % TVG_NAME)
      else:
        value = re.match( r'.*tvg-name' + eqString + r'"(.+?)".*', lineString)
        if value:
          value = value.group(3)
          value = trim(value)
          LINE = (LINE + ' tvg-name="%s"' % value)

      if (ASPECT_RATIO and ASPECT_RATIO != ""):
        if(ASPECT_RATIO == "-0"):
          LINE = LINE
        else:
          LINE = (LINE + ' aspect-ratio="%s"' % ASPECT_RATIO)
      else:
        value = re.match( r'.*aspect-ratio' + eqString + r'"(.+?)".*', lineString)
        if value:
          value = value.group(3)
          value = trim(value)
          LINE = (LINE + ' aspect-ratio="%s"' % value)

      if (_TITLE and _TITLE != ""):
        LINE = (LINE + ',%s' % _TITLE)
      else:
        value = re.match( r'.*,(.*)', lineString)
        if value:
          value = value.group(1)
          value = trim(value)
          LINE = (LINE + ',%s' % value)

    elif re.match( r'(#EXTVLCOPT(\s+)?:.*)', lineString):
      LINE = '#EXTVLCOPT:'

      value = re.match( r'.*network-caching.*?(\d+).*', lineString)
      if value:
        value = value.group(1)
        value = trim(value)
        LINE = (LINE + 'network-caching=%s' % value)

      value = re.match( r'.*start-time.*?(\d+).*', lineString)
      if value:
        value = value.group(1)
        value = trim(value)
        LINE = (LINE + 'start-time=%s' % value)

      value = re.match( r'.*stop-time.*?(\d+).*', lineString)
      if value:
        value = value.group(1)
        value = trim(value)
        LINE = (LINE + 'stop-time=%s' % value)

    '''
    elif re.match( r'(.*http://fs.to/get/dl/.+?)\..+?(/.+)', lineString):
      LINE = ''.join(re.match( r'(.*http://fs.to/get/dl/.+?)\..+?(/.+)', lineString).groups())
    '''

    lineString = LINE
    if lineString != m.group(1):
      console.write( '%02d: %s\r\n' % (lineNumber, lineString) )

    return lineString

  # First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
  editor.beginUndoAction()

  # run a command from the menu.
  notepad.runMenuCommand('Language', 'M3U')
  notepad.runMenuCommand('Синтаксисы', 'M3U')
  # notepad.runMenuCommand('Синтаксисы'.decode('cp1251').encode('utf-8'), 'M3U')

  # notepad.runMenuCommand('Encoding', 'Convert to ANSI')
  # notepad.save()

  # '''
  # удаление начальных пробелов
  editor.rereplace(r'^[\t ]+', r'', 0, editor.positionFromLine(editor.getUserLineSelection()[0]), editor.positionFromLine(editor.getUserLineSelection()[1]), 0)
  # перемещение активных ссылок вверх списка
  editor.rereplace(r'^(#EXTINF:.*\s+)((## .*?(\s+)?)+)^((.*://.*)?)(\s+)?$', r'$1$6\r\n$2', 0, editor.positionFromLine(editor.getUserLineSelection()[0]), editor.positionFromLine(editor.getUserLineSelection()[1]), 0)
  # удаление пустых строк
  editor.rereplace(r'^\r\n', '', 0, editor.positionFromLine(editor.getUserLineSelection()[0]), editor.positionFromLine(editor.getUserLineSelection()[1]), 0)
  editor.rereplace(r'[\r\n]+', r'\r\n', 0, editor.positionFromLine(editor.getUserLineSelection()[0]), editor.positionFromLine(editor.getUserLineSelection()[1]), 0)
  # вызов функции обработки строк
  editor.rereplace(r'^(.*)$', foundSomething, 0, editor.positionFromLine(editor.getUserLineSelection()[0]), editor.positionFromLine(editor.getUserLineSelection()[1]), 0)
  # '''

  # notepad.runMenuCommand('Encoding', 'Convert to UTF-8')

  '''
  for index, item in enumerate(groups):
    console.write( '%s: %s\r\n' % (index, item) )
  '''

  # End the undo action, so Ctrl-Z will undo the above actions
  editor.endUndoAction()
  # Turn the undo recorder back on.
  editor.setUndoCollection(1)
