# -*- coding: cp1251 -*-

# https://github.com/Qetuoadgj/PythonScript/tree/master/scripts/HTML%20Scripts
# https://github.com/Qetuoadgj/PythonScript/raw/master/scripts/HTML%20Scripts/Generate%20URL%20List.py

import re
# import types
# import time

def trim(string):
  if string:
    # �������� �������
    # string = re.sub(r'["]', '', string)
    # �������� ��������� � ���������� ��������
    string = re.sub(r'^[\s\t]+', '', string)
    string = re.sub(r'[\s\t]+$', '', string)
    # �������� ������������� ��������
    string = re.sub(r'[\t]+', ' ', string)
    string = re.sub(r'[\s]+', ' ', string)
    # ����������� ����������
    return string

# ����������� ����������
SYNTAX    = '#EXTINF: -1 group-title="LANET",___%04d___'
PATTERN   = 'http://play.lanet.tv/live/%04d.m3u8'
COUNT_MIN = 1000
COUNT_MAX = COUNT_MIN + 30
SPLIT_AT  = 5000
SKIP_UNKNOWN = 1

# #EXTINF:.*,[ \t]?+(.*)\r\n.*?(\d+).m3u8\r\n\r\n
# \2:'\1',\r\n

# ([^,]+)(,[ ]*\1)+
# \1

lanet = {
	9002:'1+1',
	9053:'112',
	9010:'���',
	9014:'5 �����',
	9016:'2+2',
	9017:'��������',
	9018:'����',
	9035:'��������� �������� 24',
	9047:'������',
	9050:'ZIK',
	9060:'������� TV',
	1001:'����������-TB',
	9086:'3S',
	1002:'������� HD',

  # Lanet 2017
  1008:'Skrypin UA',
  2001:'Lanet Trailers HD',
  2003:'Lanet Streams HD',
  2006:'Lanet Fight HD',
  9086:'3S',
  9921:'UA: ������',
  9923:'����',
  9922:'UA | TV',

  #VLAD - 2017.01.26
  1001:'Hromadske',
  1004:'HELTV',
  1005:'MostVideo.TV',
  1007:'���� music HD',
  1008:'Skrypin.ua',
  1009:'����� HD',
  1010:'CK1',
  1011:'��� �����',
  2001:'��������',
  2003:'Z GAMES',
  9001:'UA ������ [ua]',
  9003:'���',
  9011:'Tonis',
  9014:'5 ����� UA',
  9015:'Gamma',
  9018:'����',
  9025:'EU Music',
  9026:'Q TV',
  9028:'Music BOX',
  9031:'Z',
  9032:'A One',
  9033:'��',
  9034:'NewsOne',
  9035:'24 ����� UA',
  9037:'������ ������� �����',
  9039:'��.INFO',
  9041:'���� ��',
  9043:'���� ��',
  9045:'��� ��',
  9048:'UA',
  9049:'���',
  9051:'����������',
  9052:'������� TV',
  9053:'112 �������',
  9055:'PRO ��',
  9057:'��R',
  9059:'Boutique TV',
  9060:'�������',
  9061:'����� 402',
  9063:'�����',
  9066:'�������� UA',
  9076:'����',
  9085:'Milady Television',
  9086:'3S TV',
  9089:'CNL',
  9094:'������ ���',
  9097:'LALE',
  9098:'Shopping',
  9099:'������ ��������',
  9129:'������ ��',
  9130:'����������',
  9143:'��������',
  9152:'News Network',
}

for c_num, c_name in lanet.items():
  lanet[c_num] = c_name.decode('cp1251').encode('utf-8')

channels = lanet

expression = notepad.prompt(
  '',
  '���� ������:',
  ('syntax = %s' + '\r\n' + 'pattern = %s' + '\r\n' + 'count_min = %s' + '\r\n' + 'count_max = %s' + '\r\n' + 'split_at = %s') % (SYNTAX, PATTERN, COUNT_MIN, COUNT_MAX, SPLIT_AT)
)

if expression != None:

  # �������������� ��������� ANSI � UTF-8
  expression = expression.decode('cp1251').encode('utf-8')

  console.show()
  console.clear()

  expression = re.sub('\r\n', '; ', expression)
  list = expression.split('; ')

  eqString = r'([\s\t]+)?=([\s\t]+)?'

  SYNTAX = re.sub(r'syntax' + eqString, '', list[0])
  SYNTAX = trim(SYNTAX)

  SYNTAX_OLD = SYNTAX

  PATTERN = re.sub(r'pattern' + eqString, '', list[1])
  PATTERN = trim(PATTERN)

  COUNT_MIN = re.sub(r'count_min' + eqString, '', list[2])
  COUNT_MIN = trim(COUNT_MIN)
  COUNT_MIN = int(COUNT_MIN)

  COUNT_MAX = re.sub(r'count_max' + eqString, '', list[3])
  COUNT_MAX = trim(COUNT_MAX)
  COUNT_MAX = int(COUNT_MAX)

  SPLIT_AT = re.sub(r'split_at' + eqString, '', list[4])
  SPLIT_AT = trim(SPLIT_AT)
  SPLIT_AT = int(SPLIT_AT)

  # First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
  editor.beginUndoAction()

  if (SYNTAX and SYNTAX != ""):
    # run a command from the menu.
    notepad.runMenuCommand('Language', 'M3U')
    notepad.runMenuCommand('����������'.decode('cp1251').encode('utf-8'), 'M3U')
    ''' For built-in menus use notepad.menuCommand(),
    for non built-in menus (e.g. TextFX and macros you�ve defined),
    use notepad.runMenuCommand(menuName, menuOption).
    For other plugin commands (in the plugin menu),
    use Notepad.runPluginCommand(pluginName, menuOption) '''

  count = 0
  num = 0
  list = 1

  # delay = 1
  # time.sleep(delay) # Delay for 'delay' seconds

  if ( (COUNT_MIN + SPLIT_AT) <= COUNT_MAX ):
    print('## %s - %s' % (COUNT_MIN, (COUNT_MIN + SPLIT_AT) - 1))
  else:
    print('## %s - %s' % (COUNT_MIN, COUNT_MAX - 1))

  if (SYNTAX and SYNTAX != ""):
    print('#EXTM3U')
    console.write('%03d.\r\n#EXTM3U\r\n' % (list))

  for x in range(COUNT_MIN, COUNT_MAX):

    count = count + 1
    num = num + 1
    c_count = COUNT_MIN + count - 1

    check = float(count)/float(SPLIT_AT) - int(count)/int(SPLIT_AT)

    SYNTAX = SYNTAX_OLD
    RESULT = (SYNTAX + '\r\n' + PATTERN) % (int(num), int(x))

    isLanet = re.match(r'.*lanet.tv\/.*\/.*.m3u8.*', PATTERN, re.I)
    if isLanet:
      for c_num, c_name in channels.items():
        if int(c_num) == int(c_count):
          SYNTAX = '#EXTINF: -1 group-title="LANET",'+c_name
          RESULT = (SYNTAX + '\r\n' + PATTERN) % (int(x))
          break
        else:
          if (SKIP_UNKNOWN == 1):
            RESULT = False

    if (RESULT):
      if (SYNTAX and SYNTAX != ""):
        print(RESULT)
        console.write(RESULT + '\r\n')
      else:
        RESULT = (PATTERN) % (int(x))
        print(RESULT)
        console.write(RESULT + '\r\n')

      if ( (float(check) == float(0)) and (x < (COUNT_MAX-1)) ):
        # move caret to first position in document.
        editor.documentStart()
        # ����� ��������
        num = 0
        list = list + 1
        # create a new document.
        notepad.new()
        if (SYNTAX and SYNTAX != ""):
          # run a command from the menu.
          notepad.runMenuCommand('Language', 'M3U')
          notepad.runMenuCommand('����������'.decode('cp1251').encode('utf-8'), 'M3U')

        if ( (x + SPLIT_AT) <= COUNT_MAX ):
          print('## %s - %s' % ((x + 1), (x + SPLIT_AT + 1)))
        else:
          print('## %s - %s' % ((x + 1), COUNT_MAX))

        if (SYNTAX and SYNTAX != ""):
          print('#EXTM3U')
          console.write('\r\n\r\n%03d.\r\n#EXTM3U\r\n' % (list))

      # move caret to last position in document.
      editor.documentEnd()

  # move caret to first position in document.
  editor.documentStart()

  # End the undo action, so Ctrl-Z will undo the above actions
  editor.endUndoAction()
  # Turn the undo recorder back on.
  editor.setUndoCollection(1)
