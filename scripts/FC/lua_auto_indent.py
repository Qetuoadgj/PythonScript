# -*- coding: utf-8 -*-

# console.show()
console.clear()

import re

# First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
editor.beginUndoAction()

pos = editor.getCurrentPos()
editor.documentStart()
editor.documentEnd()
editor.selectAll()

# перенос комментариев
editor.rereplace(r'^[\t ]+--[\t ]+', r'-- ')
# перенос фигурных скобок к знаку равенства
editor.rereplace(r'[ ]?=\s+\{', r' = {')
# дописывание незначущего ноля -.001 --> -0.001
# editor.rereplace(r'([ -])\.(\d+)', r'$1(0.)$2')




for x in range(0, 2):
	# run a command from the menu.
	notepad.runMenuCommand('Операции со Строками', 'Удалить Пустые Строки (Содер. символы Пробела)')
	notepad.runMenuCommand('Операции с Пробелами', 'Убрать Замыкающие Пробелы')
	
	notepad.runMenuCommand('Синтаксисы', 'FarCry LUA')
	'''
	# Добавить пробелы перед и после знаков равенства (x=-000.5 --> x = -000.5)
	editor.rereplace(r'(\w)(?:[\t ]?)+(==|~=|!=|=)(?:[\t ]?)+(([-+.]+)?.+)', r'($1 $2 $3)')
	# Добавить пробелы после запятых (x,y,z --> x, y, z)
	editor.rereplace(r'(.*?)(?:[\t ]?)+,(?:[\t ]?)+', r'($1, )')
	# Добавить пробелы перед и после фигурных скобок ( {x} --> { x })
	editor.rereplace(r'(?:[\t ]?)+(\})', r'( $1)')
	editor.rereplace(r'(\{)(?:[\t ]?)+', r'($1 )')
	'''
	# Убрать пробелы перед и после операторов (x = -000.5 --> x=-000.5)
	editor.rereplace(r'(\w)(?:[\t ]?)+(==|~=|!=|=|>|<|\*|\/|\^)(?:[\t ]?)+(([-+.]+)?.+?)', r'($1$2$3)')
	editor.rereplace(r'(\d+(?:\.\d+)?)(?:[\t ]?)+(\*|\/|<|>|=)(?:[\t ]?)+', r'($1$2)')
	# Убрать пробелы после запятых (x, y, z --> x,y,z)
	editor.rereplace(r'(.*?)(?:[\t ]?)+,(?:[\t ]?)+', r'($1,)')
	# Убрать пробелы перед и после фигурных скобок ( { x } --> {x})
	# editor.rereplace(r'(?:[\t ]?)+(\}|\]|\))', r'($1)')
	# editor.rereplace(r'(\{|\[|\()(?:[\t ]?)+', r'($1)')
	editor.rereplace(r'(\{)(?:[\t ]?)+(.*?)(?:[\t ]?)+(\})', r'($1$2$3)')
	editor.rereplace(r'(\[)(?:[\t ]?)+(.*?)(?:[\t ]?)+(\])', r'($1$2$3)')
	editor.rereplace(r'(\()(?:[\t ]?)+(.*?)(?:[\t ]?)+(\))', r'($1$2$3)')
	#
	editor.rereplace(r'(-{2,}\*?)', r'(--*)')
	editor.rereplace(r'--\*(\{|\[)', r'(--$1)')
	editor.rereplace(r'--\*(\}|\])', r'(--$1)')
	editor.rereplace(r'(?:[\t ]?)+(--\*)(?:[\t ]?)+', r'( $1 )')
	
	for x in range(0, 10):
		editor.rereplace(r'^([ \t]+)?\b(end)\b(.*)\b(end)\b', r'$2\r\n$3\r\n$4')
	notepad.runPluginCommand('Indent By Fold', 'Reindent File')
	editor.rereplace(r'\t\b(else|elseif)\b', r'$1')
	editor.rereplace(r'\t(--\[|--\]|--~)', r'$1')

notepad.runMenuCommand('Операции с Пробелами', 'Убрать Замыкающие Пробелы')

'''
# editor.rereplace(r'(\},)(?!.*\s+[{}])', r'$1\r\n')
editor.rereplace(r'(\},)(?!.*\s+(--[\t ]?+)?[{}]+)', r'$1\r\n')

editor.rereplace(r'(^[\t ]?+\w+[ =]+\{)', r'\r\n$1')
	
editor.rereplace(r'(^\bend;?\b|^\}[;,]?)', r'$1\r\n')
editor.rereplace(r'^(\bend\b;?)$(?:\r\n){2}^(--(\]|~)?)$', r'$1\r\n$2\r\n')

editor.rereplace(r'(^.*[;,])[\r\n]+([\t ]+?--\])', r'$1\r\n$2\r\n')
editor.rereplace(r'[\r\n]{6,}', r'\r\n\r\n')

editor.rereplace(r'(--\]$)[\r\n]+([\t ]+?\})', r'$1\r\n$2')
editor.rereplace(r'(^.*\{.*\}[;,]?)[\r\n]{3,}', r'$1\r\n')
editor.rereplace(r'(\}.*)[\r\n]+([\t ]+\{(?!.*\}))', r'$1\r\n\r\n$2')
'''
# editor.rereplace(r'(--\[.*([\r\n].*?)+--\])', lambda m: re.sub(r'(^|\n)', r'\1\t', m.group(1)), re.G)

notepad.setLangType(LANGTYPE.LUA)
editor.gotoPos(pos)

# End the undo action, so Ctrl-Z will undo the above actions
editor.endUndoAction()
# Turn the undo recorder back on.
editor.setUndoCollection(1)


