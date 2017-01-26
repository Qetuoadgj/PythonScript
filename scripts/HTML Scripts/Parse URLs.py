# -*- coding: cp1251 -*-

import re

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

console.show()
console.clear()

# eqString = r'([\s\t]+)?=([\s\t]+)?'

lineCount = 0
def foundSomething(m):
  global lineCount
  lineCount += 1
  selectionStart, selectionEnd = editor.getUserLineSelection()

  lineString = m.group(1)
  lineNumber = selectionStart + lineCount

  spacings = re.match( r'^(([ \t]+)?).*', lineString).group(1)

  url = trim(m.group(1))

  if re.match( r'(.*youtube\.com.*)', lineString):
    id = re.match( r'.*[?]v=(.*)', lineString).group(1)
    if id:
      lineString = (spacings + '<img class="thumbnail" title="" src="https://i.ytimg.com/vi/%s/mqdefault.jpg" content="https://www.youtube.com/embed/%s" url="%s"></img>' % (id, id, url))          

  elif re.match( r'(.*eporner\.com.*)', lineString):
    # http://www.eporner.com/hd-porn/494421/Banged-For-The-First-Time/
    # http://static.eporner.com/thumbs/static4/4/49/494/494421/494421-preview.mp4
    # http://static.eporner.com/thumbs/static4/4/49/494/494421/1.jpg
    # http://www.eporner.com/embed/494421
    id, title = re.match( r'.*eporner\.com\/.+\/(\d+)\/(.+)\/', lineString).group(1, 2)
    if id:
      url = trim(url)
      title = re.sub(r'[-_]', ' ', title).title()
      title = trim(title)
      id_1, id_2, id_3 = re.match( r'(((\d)\d)\d)\d+', id).group(3, 2, 1)
    
      lineString = (spacings + '<video class="thumbnail" title="%s" src="http://static.eporner.com/thumbs/static4/%s/%s/%s/%s/%s-preview.mp4" content="http://www.eporner.com/embed/%s" url="%s"></video>' % (title, id_1, id_2, id_3, id, id, id, url))          
     
  elif re.match( r'(.*xvideos\.com.*)', lineString):
    # http://www.xvideos.com/video7122533/is_this_a_blowjob_or_a_mouthfuck_
    # http://flashservice.xvideos.com/embedframe/7122533
    # http://img100-533.xvideos.com/videos/thumbsll/ad/f7/a1/adf7a1c629cb896c9993c520c1b370b0/adf7a1c629cb896c9993c520c1b370b0.8.jpg
    id, title = re.match( r'.*xvideos.com/video(\d+)/(.*)', lineString).group(1, 2)
    if id:
      title = re.sub(r'[-_]', ' ', title).title()
      title = trim(title)
      url = trim(url)
    
      lineString = (spacings + '<img class="thumbnail" title="%s" src="" content="http://flashservice.xvideos.com/embedframe/%s" url="%s"></img>' % (title, id, url))               
      
  elif re.match( r'(.*vporn\.com.*)', lineString):
      # http://www.vporn.com/straight/natalie-heart-x-jaslene-jade-c-rner-p-cket/985206/
      # http://www.vporn.com/embed/985206
      # http://th-eu2.vporn.com/t/6/985206/m130.jpg
    title, id = re.match( r'.*vporn.com/.+/(.*)/(\d+)/', lineString).group(1, 2)
    if id:
      title = re.sub(r'[-_]', ' ', title).title()
      title = trim(title)
      url = trim(url)
    
      lineString = (spacings + '<img class="thumbnail" title="%s" src="http://th-eu2.vporn.com/t/6/%s/m130.jpg" content="http://www.vporn.com/embed/%s" url="%s"></img>' % (title, id, id, url))                  
      
  elif re.match( r'(.*:\/\/.*)', lineString):
    url = trim(url)
    lineString = ('<img class="thumbnail" title="" src="" content="%s" url="%s"></img>' % (url, url))

  if lineString != m.group(1):
    console.write( '%02d: %s\n' % (lineNumber, lineString) )

  return lineString

# First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
editor.beginUndoAction()

# run a command from the menu.
# notepad.runMenuCommand('Language', 'M3U')
# notepad.runMenuCommand('Синтаксисы'.decode('cp1251').encode('utf-8'), 'M3U')

# notepad.runMenuCommand('Encoding', 'Convert to ANSI')
# notepad.save()

# '''
# вызов функции обработки строк
editor.rereplace(r'^(.*)$', foundSomething, 0, editor.positionFromLine(editor.getUserLineSelection()[0]), editor.positionFromLine(editor.getUserLineSelection()[1]), 0)
# '''

# notepad.runMenuCommand('Encoding', 'Convert to UTF-8')

# End the undo action, so Ctrl-Z will undo the above actions
editor.endUndoAction()
# Turn the undo recorder back on.
editor.setUndoCollection(1)
