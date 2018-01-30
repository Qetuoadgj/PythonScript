# -*- coding: utf-8 -*-

console.show()
console.clear()

import re

# First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
editor.beginUndoAction()

# pos = editor.getCurrentPos()
# editor.documentStart()
# editor.documentEnd()
# editor.selectAll()

editor.rereplace(r'[ ,([{]+.*|[#_.]', '')
notepad.runMenuCommand('Операции с Пробелами', 'Убрать Замыкающие Пробелы')
notepad.runMenuCommand('Операции со Строками', 'Удалить Пустые Строки (Содер. символы Пробела)')

compareTable = []
uniques = []
def parseMatches(m):
	match = m.group(1)
	compare = match.lower()
	if (not compare == '' and not compare in compareTable):
		compareTable.append(compare)
		uniques.append(match)

editor.research('(^(.*)$)', parseMatches)

output = ''
for index, item in enumerate(uniques):
	result = '%s' % (item)
	output += "\t'" + result + "'"
	if index < len(uniques)-1:
		output += ',\r\n'

console.write(output)
editor.clearAll()
editor.appendText('t = [\r\n')
editor.appendText(output)
editor.appendText('\r\n]')

# notepad.setLangType(LANGTYPE.LUA)
# editor.gotoPos(pos)

# End the undo action, so Ctrl-Z will undo the above actions
editor.endUndoAction()
# Turn the undo recorder back on.
editor.setUndoCollection(1)
