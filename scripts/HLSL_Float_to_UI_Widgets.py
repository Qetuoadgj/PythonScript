# console.show()
console.clear()

import re

# Get values from prompt window
expression = notepad.prompt(
                 'Enter the name',
                 'Name',
                 '')

expression = re.sub('\r\n', '; ', expression)

def UI_bool(m):
	bool_name = m.group(1)
	value = m.group(3)
	comment = "" + m.group(4)
	
	return 'bool\t%s <\r\n\tstring UIName="%s";\r\n\tstring UIWidget="CheckButton";\r\n> = {%s};%s\r\n' % (bool_name, bool_name, value, comment)

def UI_int(m):
	int_name = m.group(1)
	value = m.group(3)
	comment = "" + m.group(4)
	
	return 'int\t%s <\r\n\tstring UIName="%s";\r\n\tstring UIWidget="Spinner";\r\n\t// int UIMin=0.0;\r\n\t// int UIMax=1.0;\r\n> = {%s};%s\r\n' % (int_name, int_name, value, comment)


def UI_float(m):
	float_name = m.group(1)
	value = m.group(3)
	comment = "" + m.group(4)
	
	return 'float\t%s <\r\n\tstring UIName="%s";\r\n\tstring UIWidget="Spinner";\r\n\t// float UIMin=0.0;\r\n\t// float UIMax=1.0;\r\n\t// float UIStep=0.1;\r\n> = {%s};%s\r\n' % (float_name, float_name, value, comment)

def UI_float2(m):
	float_name = m.group(1)
	value1 = m.group(3)
	value1_name = m.group(1) + "Night"
	value2 = m.group(4)
	value2_name = m.group(1) + "Day"
	comment = "" + m.group(5)
	
	return 'float\t%s <\r\n\tstring UIName="%s";\r\n\tstring UIWidget="Spinner";\r\n\t// float UIMin=0.0;\r\n\t// float UIMax=1.0;\r\n\t// float UIStep=0.1;\r\n> = {%s};%s\r\nfloat\t%s <\r\n\tstring UIName="%s";\r\n\tstring UIWidget="Spinner";\r\n\t// float UIMin=0.0;\r\n\t// float UIMax=1.0;\r\n\t// float UIStep=0.1;\r\n> = {%s};%s\r\n' % (value2_name, value2_name, value2, comment, value1_name, value1_name, value1, comment)

def UI_float3(m):
	float_name = m.group(1)
	value1 = m.group(3)
	value2 = m.group(4)
	value3 = m.group(5)
	comment = "" + m.group(6)
	
	return 'float3\t%s <\r\n\tstring UIName="%s";\r\n\tstring UIWidget="Color";\r\n> = {%s, %s, %s};%s\r\n' % (float_name, float_name, value1, value2, value3, comment)

# First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
editor.beginUndoAction()
	
bool  = '.*bool[\s\t]*([a-zA-Z0-9]+)(Ext|Int)?[\s\t]*=[\s\t]*(.*);(.*)'
int  = '.*int[\s\t]*([a-zA-Z0-9]+)(Ext|Int)?[\s\t]*=[\s\t]*(.*);(.*)'
float  = '.*float[\s\t]*([a-zA-Z0-9]+)(Ext|Int)?[\s\t]*=[\s\t]*(.*);(.*)'
float2 = '.*float2[\s\t]*([a-zA-Z0-9]+)(Ext|Int)?[\s\t]*=[\s\t]*float2[\s\t]*\([\s\t]*([+-]?[0-9]*\.?[0-9]*),[\s\t]*([+-]?[0-9]*\.?[0-9]*)[\s\t]*\)[\s\t]*;(.*)'
float3 = '.*float3[\s\t]*([a-zA-Z0-9]+)(Ext|Int)?[\s\t]*=[\s\t]*float3[\s\t]*\([\s\t]*([+-]?[0-9]*\.?[0-9]*),[\s\t]*([+-]?[0-9]*\.?[0-9]*),[\s\t]*([+-]?[0-9]*\.?[0-9]*)[\s\t]*\)[\s\t]*;(.*)'
	
editor.rereplace(bool, UI_bool, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
editor.rereplace(int, UI_int, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
editor.rereplace(float, UI_float, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
editor.rereplace(float2, UI_float2, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
editor.rereplace(float3, UI_float3, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))

editor.rereplace(r'UIName="E([A-Z])', 'UIName="'+expression+r'\1', 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
editor.rereplace(r'UIName="[a-z0-9]+([A-Z])', 'UIName="'+expression+r'\1', 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
editor.rereplace(r'UIName="(.*[a-z0-9])V[0-9]([A-Z].*)', r'UIName="\1\2', 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
editor.rereplace(r'UIName="(.*[a-z0-9])Ext([A-Z0-9].*)', r'UIName="\1\2', 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
editor.rereplace(r'UIName="(.*[a-z0-9])Int([A-Z0-9].*)', r'UIName="\1Interior\2', 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))

editor.rereplace(r'UIName="(.*)Ext(Day|Night)', r'UIName="\1\2', 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
editor.rereplace(r'UIName="(.*)Int(Day|Night)', r'UIName="\1Interior\2', 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))


# End the undo action, so Ctrl-Z will undo the above two actions
editor.endUndoAction()
# Turn the undo recorder back on.
editor.setUndoCollection(1)
