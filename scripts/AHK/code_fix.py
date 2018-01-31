# -*- coding: utf-8 -*-

console.show()
console.clear()

import re

DocumentStartingPosition = editor.getCurrentPos()

# editor.documentStart()
# editor.documentEnd()
# editor.selectAll()

CaseTable = [
	"#ClipboardTimeout","#CommentFlag","#ErrorStdOut","#EscapeChar","#HotkeyInterval","#HotkeyModifierTimeout","#Hotstring","#If","#IfTimeout","#IfWinActive","#IfWinExist","#IfWinNotActive","#IfWinNotExist","#Include","#IncludeAgain","#InputLevel","#InstallKeybdHook","#InstallMouseHook","#KeyHistory","#LTrim","#MaxHotkeysPerInterval","#MaxMem","#MaxThreads","#MaxThreadsBuffer","#MaxThreadsPerHotkey","#MenuMaskKey","#NoEnv","#NoTrayIcon","#Persistent","#SingleInstance","#UseHook","#Warn","#WinActivateForce",".__Call",".__Get",".__Handle",".__Set","._NewEnum",".AtEOF",".Clone",".Close",".Encoding",".GetAddress",".GetCapacity",".HasKey",".Insert",".IsBuiltIn",".IsByRef",".IsOptional",".IsVariadic",".MaxIndex",".MaxParams",".MinIndex",".MinParams",".Name",".Pos",".Position",".RawRead",".RawWrite",".Read",".ReadChar",".ReadDouble",".ReadFloat",".ReadInt",".ReadInt64",".ReadLine",".ReadShort",".ReadUChar",".ReadUInt",".ReadUShort",".Remove",".Seek",".SetCapacity",".Write",".WriteChar",".WriteDouble",".WriteFloat",".WriteInt",".WriteInt64",".WriteLine",".WriteShort",".WriteUChar",".WriteUInt",".WriteUShort","__Call","__Delete","__Get","__New","__Set","_NewEnum","A_AhkPath","A_AhkVersion","A_AppData","A_AppDataCommon","A_AutoTrim","A_BatchLines","A_CaretX","A_CaretY","A_ComputerName","A_ControlDelay","A_Cursor","A_DD","A_DDD","A_DDDD","A_DefaultMouseSpeed","A_Desktop","A_DesktopCommon","A_DetectHiddenText","A_DetectHiddenWindows","A_EndChar","A_EventInfo","A_ExitReason","A_FileEncoding","A_FormatFloat","A_FormatInteger","A_Gui","A_GuiControl","A_GuiControlEvent","A_GuiEvent","A_GuiHeight","A_GuiWidth","A_GuiX","A_GuiY","A_Hour","A_IconFile","A_IconHidden","A_IconNumber","A_IconTip","A_Index","A_IPAddress1","A_IPAddress2","A_IPAddress3","A_IPAddress4","A_Is64bitOS","A_IsAdmin","A_IsCompiled","A_IsCritical","A_IsPaused","A_IsSuspended","A_IsUnicode","A_KeyDelay","A_Language","A_LastError","A_LineFile","A_LineNumber","A_LoopField","A_LoopFileAttrib","A_LoopFileDir","A_LoopFileExt","A_LoopFileFullPath","A_LoopFileLongPath","A_LoopFileName","A_LoopFileShortName","A_LoopFileShortPath","A_LoopFileSize","A_LoopFileSizeKB","A_LoopFileSizeMB","A_LoopFileTimeAccessed","A_LoopFileTimeCreated","A_LoopFileTimeModified","A_LoopReadLine","A_LoopRegKey","A_LoopRegName","A_LoopRegSubkey","A_LoopRegTimeModified","A_LoopRegType","A_MDay","A_Min","A_MM","A_MMM","A_MMMM","A_Mon","A_MouseDelay","A_MSec","A_MyDocuments","A_Now","A_NowUTC","A_NumBatchLines","A_OSType","A_OSVersion","A_PriorHotkey","A_PriorKey","A_ProgramFiles","A_Programs","A_ProgramsCommon","A_PtrSize","A_RegView","A_ScreenDPI","A_ScreenHeight","A_ScreenWidth","A_ScriptDir","A_ScriptFullPath","A_ScriptHwnd","A_ScriptName","A_Sec","A_Space","A_StartMenu","A_StartMenuCommon","A_Startup","A_StartupCommon","A_StringCaseSense","A_Tab","A_Temp","A_ThisFunc","A_ThisHotkey","A_ThisLabel","A_ThisMenu","A_ThisMenuItem","A_ThisMenuItemPos","A_TickCount","A_TimeIdle","A_TimeIdlePhysical","A_TimeSincePriorHotkey","A_TimeSinceThisHotkey","A_TitleMatchMode","A_TitleMatchModeSpeed","A_UserName","A_WDay","A_WinDelay","A_WinDir","A_WorkingDir","A_YDay","A_Year","A_YWeek","A_YYYY","Abort","AboveNormal","Abs","ACos","ActiveX","Add","ahk_class","ahk_exe","ahk_group","ahk_id","ahk_pid","All","alnum","alpha","Alt","AltDown","AltSubmit","AltTab","AltTabAndMenu","AltTabMenu","AltTabMenuDismiss","AltUp","AlwaysOnTop","and","AppsKey","Array","Asc","ASin","ATan","AutoSize","AutoTrim","Background","BackgroundTrans","BackSpace","BelowNormal","between","BitAnd","BitNot","BitOr","BitShiftLeft","BitShiftRight","BitXOr","Blind","BlockInput","bold","Border","Bottom","break","Browser_Back","Browser_Favorites","Browser_Forward","Browser_Home","Browser_Refresh","Browser_Search","Browser_Stop","Button","Buttons","ByRef","Cancel","Capacity","CapsLock","Caption","catch","Ceil","Center","Check","Check3","Checkbox","Checked","CheckedGray","Choose","ChooseString","Chr","class","Click","Clipboard","ClipboardAll","ClipWait","Close","Color","ComboBox","ComObjActive","ComObjArray","ComObjConnect","ComObjCreate","ComObject","ComObjEnwrap","ComObjError","ComObjFlags","ComObjGet","ComObjMissing","ComObjQuery","ComObjType","ComObjUnwrap","ComObjValue","ComSpec","contains","continue","Control","ControlClick","ControlFocus","ControlGet","ControlGetFocus","ControlGetPos","ControlGetText","ControlList","ControlMove","ControlSend","ControlSendRaw","ControlSetText","CoordMode","Cos","Count","Critical","Ctrl","CtrlBreak","CtrlDown","CtrlUp","Custom","date","DateTime","Days","DDL","Default","Del","Delete","DeleteAll","Delimiter","Deref","Destroy","DetectHiddenText","DetectHiddenWindows","digit","Disable","Disabled","DllCall","Down","DPIScale","Drive","DriveGet","DriveSpaceFree","DropDownList","Edit","Eject","else","Enable","Enabled","End","Enter","EnvAdd","EnvDiv","EnvGet","EnvMult","EnvSet","EnvSub","EnvUpdate","Error","ErrorLevel","Esc","Escape","Exception","Exist","Exit","ExitApp","Exp","Expand","ExStyle","extends","F1","F10","F11","F12","F13","F14","F15","F16","F17","F18","F19","F2","F20","F21","F22","F23","F24","F3","F4","F5","F6","F7","F8","F9","false","FileAppend","FileCopy","FileCopyDir","FileCreateDir","FileCreateShortcut","FileDelete","FileEncoding","FileExist","FileGetAttrib","FileGetShortcut","FileGetSize","FileGetTime","FileGetVersion","FileInstall","FileMove","FileMoveDir","FileOpen","FileRead","FileReadLine","FileRecycle","FileRecycleEmpty","FileRemoveDir","FileSelectFile","FileSelectFolder","FileSetAttrib","FileSetTime","FileSystem","finally","First","Flash","Float","FloatFast","Floor","Focus","Font","for","FormatTime","FromCodePage","Func","GetKeyName","GetKeySC","GetKeyState","GetKeyVK","global","gosub","goto","Grid","Group","GroupActivate","GroupAdd","GroupBox","GroupClose","GroupDeactivate","Gui","GuiClose","GuiContextMenu","GuiControl","GuiControlGet","GuiDropFiles","GuiEscape","GuiSize","Hdr","Hidden","Hide","High","HKCC","HKCR","HKCU","HKEY_CLASSES_ROOT","HKEY_CURRENT_CONFIG","HKEY_CURRENT_USER","HKEY_LOCAL_MACHINE","HKEY_USERS","HKLM","HKU","Home","Hotkey","Hours","HScroll","Icon","IconSmall","ID","IDLast","if","IfEqual","IfExist","IfGreater","IfGreaterOrEqual","IfInString","IfLess","IfLessOrEqual","IfMsgBox","IfNotEqual","IfNotExist","IfNotInString","IfWinActive","IfWinExist","IfWinNotActive","IfWinNotExist","Ignore","IL_Add","IL_Create","IL_Destroy","ImageList","ImageSearch","in","IniDelete","IniRead","IniWrite","Input","InputBox","Ins","Insert","InStr","Integer","IntegerFast","Interrupt","IsByRef","IsFunc","IsLabel","IsObject","italic","Join","Joy1","Joy10","Joy11","Joy12","Joy13","Joy14","Joy15","Joy16","Joy17","Joy18","Joy19","Joy2","Joy20","Joy21","Joy22","Joy23","Joy24","Joy25","Joy26","Joy27","Joy28","Joy29","Joy3","Joy30","Joy31","Joy32","Joy4","Joy5","Joy6","Joy7","Joy8","Joy9","JoyAxes","JoyButtons","JoyInfo","JoyName","JoyPOV","JoyR","JoyU","JoyV","JoyX","JoyY","JoyZ","KeyHistory","KeyWait","Label","LAlt","LastFound","LastFoundExist","Launch_App1","Launch_App2","Launch_Mail","Launch_Media","LButton","LControl","LCtrl","Left","Limit","Lines","Link","List","ListBox","ListHotkeys","ListLines","ListVars","ListView","Ln","local","LocalSameAsGlobal","Lock","Log","Logoff","Loop","Low","lower","Lowercase","LShift","LTrim","LV_Add","LV_Delete","LV_DeleteCol","LV_GetCount","LV_GetNext","LV_GetText","LV_Insert","LV_InsertCol","LV_Modify","LV_ModifyCol","LV_SetImageList","LWin","LWinDown","LWinUp","MainWindow","Margin","Maximize","MaximizeBox","MaxSize","MButton","Media_Next","Media_Play_Pause","Media_Prev","Media_Stop","Menu","Minimize","MinimizeBox","MinMax","MinSize","Minutes","Mod","MonthCal","Mouse","MouseClick","MouseClickDrag","MouseGetPos","MouseMove","Move","MsgBox","Multi","NA","new","No","NoActivate","NoDefault","NoHide","NoIcon","NoMainWindow","norm","Normal","NoSort","NoSortHdr","NoStandard","not","NoTab","NoTimers","number","NumGet","NumLock","Numpad0","Numpad1","Numpad2","Numpad3","Numpad4","Numpad5","Numpad6","Numpad7","Numpad8","Numpad9","NumpadAdd","NumpadClear","NumpadDel","NumpadDiv","NumpadDot","NumpadDown","NumpadEnd","NumpadEnter","NumpadHome","NumpadIns","NumpadLeft","NumpadMult","NumpadPgdn","NumpadPgup","NumpadRight","NumpadSub","NumpadUp","NumPut","ObjAddRef","ObjClone","Object","ObjGetAddress","ObjGetCapacity","ObjHasKey","ObjInsert","ObjMaxIndex","ObjMinIndex","ObjNewEnum","ObjRelease","ObjRemove","ObjSetCapacity","Off","Ok","On","OnClipboardChange","OnExit","OnMessage","or","OutputDebug","OwnDialogs","Owner","Parse","Password","Pause","PGDN","PGUP","Pic","Picture","Pixel","PixelGetColor","PixelSearch","Pos","PostMessage","Pow","PrintScreen","Priority","Process","ProcessName","ProcessPath","ProgramFiles","Progress","Radio","RAlt","Random","Range","Raw","RButton","RControl","RCtrl","Read","ReadOnly","Realtime","Redraw","REG_BINARY","REG_DWORD","REG_EXPAND_SZ","REG_MULTI_SZ","REG_SZ","RegDelete","RegExMatch","RegExReplace","Region","RegisterCallback","RegRead","RegWrite","Relative","Reload","Rename","Report","Resize","Restore","Retry","return","RGB","Right","Round","RShift","RTrim","Run","RunAs","RunWait","RWin","RWinDown","RWinUp","SB_SetIcon","SB_SetParts","SB_SetText","Screen","ScrollLock","Seconds","Section","Send","SendEvent","SendInput","SendLevel","SendMessage","SendMode","SendPlay","SendRaw","Serial","SetBatchLines","SetCapsLockState","SetControlDelay","SetDefaultMouseSpeed","SetEnv","SetFormat","SetKeyDelay","SetLabel","SetMouseDelay","SetNumLockState","SetRegView","SetScrollLockState","SetStoreCapslockMode","SetTimer","SetTitleMatchMode","SetWinDelay","SetWorkingDir","Shift","ShiftAltTab","ShiftDown","ShiftUp","Show","Shutdown","Sin","Single","Sleep","Slider","Sort","SortDesc","SoundBeep","SoundGet","SoundGetWaveVolume","SoundPlay","SoundSet","SoundSetWaveVolume","Space","SplashImage","SplashTextOff","SplashTextOn","SplitPath","Sqrt","Standard","static","Status","StatusBar","StatusBarGetText","StatusBarWait","StatusCD","StrGet","strike","StringCaseSense","StringGetPos","StringLeft","StringLen","StringLower","StringMid","StringReplace","StringRight","StringSplit","StringTrimLeft","StringTrimRight","StringUpper","StrLen","StrPut","StrSplit","Style","Submit","SubStr","Suspend","SysGet","SysMenu","Tab","Tab2","TabStop","Tan","Text","Theme","Thread","throw","Tile","time","Tip","ToCodePage","ToggleCheck","ToggleEnable","ToolTip","ToolWindow","Top","Topmost","TransColor","Transform","Transparent","Tray","TrayTip","TreeView","Trim","true","try","TryAgain","TV_Add","TV_Delete","TV_Get","TV_GetChild","TV_GetCount","TV_GetNext","TV_GetParent","TV_GetPrev","TV_GetSelection","TV_GetText","TV_Modify","TV_SetImageList","Type","UnCheck","underline","Unicode","Unlock","until","Up","UpDown","upper","Uppercase","URLDownloadToFile","UseEnv","UseErrorLevel","UseUnsetGlobal","UseUnsetLocal","VarSetCapacity","Vis","VisFirst","Visible","Volume_Down","Volume_Mute","Volume_Up","VScroll","Wait","WaitClose","WantCtrlA","WantF2","WantReturn","WheelDown","WheelLeft","WheelRight","WheelUp","while","WinActivate","WinActivateBottom","WinActive","WinClose","WinExist","WinGet","WinGetActiveStats","WinGetActiveTitle","WinGetClass","WinGetPos","WinGetText","WinGetTitle","WinHide","WinKill","WinMaximize","WinMenuSelectItem","WinMinimize","WinMinimizeAll","WinMinimizeAllUndo","WinMove","WinRestore","WinSet","WinSetTitle","WinShow","WinWait","WinWaitActive","WinWaitClose","WinWaitNotActive","Wrap","XButton1","XButton2","xdigit","Yes ","StrReplace",
	"Force"
]
CommandsList = "#IfWinActive,#IfWinExist,#IfWinNotActive,#IfWinNotExist,#InputLevel,AutoTrim,BlockInput,break,catch,ClipWait,continue,Control,ControlClick,ControlFocus,ControlGet,ControlGetFocus,ControlGetPos,ControlGetText,ControlMove,ControlSend,ControlSendRaw,ControlSetText,CoordMode,Critical,DetectHiddenText,DetectHiddenWindows,Drive,DriveGet,DriveSpaceFree,EnvAdd,EnvDiv,EnvGet,EnvMult,EnvSet,EnvSub,Exit,ExitApp,FileAppend,FileCopy,FileCopyDir,FileCreateDir,FileCreateShortcut,FileDelete,FileEncoding,FileGetAttrib,FileGetShortcut,FileGetSize,FileGetTime,FileGetVersion,FileInstall,FileMove,FileMoveDir,FileRead,FileReadLine,FileRecycle,FileRecycleEmpty,FileRemoveDir,FileSelectFile,FileSelectFolder,FileSetAttrib,FileSetTime,FormatTime,GetKeyState,gosub,goto,GroupActivate,GroupAdd,GroupClose,GroupDeactivate,Gui,GuiControl,GuiControlGet,Hotkey,IfEqual,IfExist,IfGreater,IfGreaterOrEqual,IfInString,IfLess,IfLessOrEqual,IfMsgBox,IfNotEqual,IfNotExist,IfNotInString,IfWinActive,IfWinExist,IfWinNotActive,IfWinNotExist,ImageSearch,IniDelete,IniRead,IniWrite,Input,InputBox,KeyWait,Loop,Menu,MouseClick,MouseClickDrag,MouseGetPos,MouseMove,MsgBox,OnExit,OutputDebug,Pause,PixelGetColor,PixelSearch,PostMessage,Process,Progress,Random,RegDelete,RegRead,RegWrite,Run,RunAs,RunWait,Send,SendEvent,SendInput,SendLevel,SendMessage,SendMode,SendPlay,SendRaw,SetBatchLines,SetCapsLockState,SetControlDelay,SetDefaultMouseSpeed,SetEnv,SetFormat,SetKeyDelay,SetMouseDelay,SetNumLockState,SetRegView,SetScrollLockState,SetStoreCapslockMode,SetTimer,SetTitleMatchMode,SetWinDelay,SetWorkingDir,Shutdown,Sleep,Sort,SoundBeep,SoundGet,SoundGetWaveVolume,SoundPlay,SoundSet,SoundSetWaveVolume,SplashImage,SplashTextOn,SplitPath,StatusBarGetText,StatusBarWait,StringCaseSense,StringGetPos,StringLeft,StringLen,StringLower,StringMid,StringReplace,StringRight,StringSplit,StringTrimLeft,StringTrimRight,StringUpper,Suspend,SysGet,Thread,ToolTip,Transform,TrayTip,URLDownloadToFile,WinActivate,WinActivateBottom,WinClose,WinGet,WinGetActiveStats,WinGetActiveTitle,WinGetClass,WinGetPos,WinGetText,WinGetTitle,WinHide,WinKill,WinMaximize,WinMenuSelectItem,WinMinimize,WinMove,WinRestore,WinSet,WinSetTitle,WinShow,WinWait,WinWaitActive,WinWaitClose,WinWaitNotActive ,#Warn,ListLines,#KeyHistory,#NoEnv,Process,#HotkeyInterval,#MaxHotkeysPerInterval,#SingleInstance"

# исправление регистра
def FixCaseFunc():
	for Command in CaseTable:
		# Case = re.search(r"#\b" + re.sub("^#", "", Command) + r"\b", CommandsList, re.IGNORECASE)
		Case = re.search(r"[^\w]+\b" + re.sub("^([^\w]+)", "", Command) + r"\b", CommandsList, re.IGNORECASE)
		if (Case is not None):
			editor.rereplace(Command + r"\b", Command, re.IGNORECASE)
		else:
			editor.rereplace(r"\b" + Command + r"\b", Command, re.IGNORECASE)

# исправление запятых
def FixCommasFunc(LineText, LineNumber, TotalLines):
	# console.write(str(LineNumber+1) + ". " + LineText + "\n")
	LineTextOld = LineText
	Match = re.search(r"^([;~]?(?:[\t ]+)?)" + r"(#?\b\w+\b)" + r"([\t ]{1,})" + r"([^\s])", LineText)
	# editor.gotoLine(LineNumber)
	# editor.scrollCaret()
	if (Match is not None):
		LeadingSpaces = Match.group(1)
		Command = Match.group(2)
		TrailingSpaces = Match.group(3)
		ParamsOrSomething = Match.group(4)
		Skip = re.search(r"^[,]", ParamsOrSomething, re.IGNORECASE)
		if (Skip is None):
			Match = False
			# Case = re.search(r"#\b" + re.sub("^#", "", Command) + r"\b", CommandsList, re.IGNORECASE)
			Case = re.search(r"[^\w]+\b" + re.sub("^([^\w]+)", "", Command) + r"\b", CommandsList, re.IGNORECASE)
			if (Case is not None):
				Match = re.search(Command + r"\b", CommandsList, re.IGNORECASE)
			else:
				Match = re.search(r"\b" + Command + r"\b", CommandsList, re.IGNORECASE)
			if (Match is not None):
				Match = re.search(r"^([;~]?(?:[\t ]+)?)" + Command + r"\b" + r"([\t ]{1,})" + r"([^\s]+)", LineText, re.IGNORECASE)
				if (Match is not None):
					MathSymbolsRegEx = r"\+\+|\-\-|\-\=|\+\=|\*\=|\/\=|\:\=|\.="
					Match = re.search(MathSymbolsRegEx, Match.group(3), re.IGNORECASE)
					if (Match is None):
						LineText = re.sub(r"^([;~]?(?:[\t ]+)?)" + Command + r"\b" + r"([\t ]{1,})" + r"([^\s])", r"\1" + Command + r",\2\3", LineText, 0, re.IGNORECASE)
						# console.write(LineText)
						LineText = re.sub(Command + r"\b" + r",([\t ]+;)", Command + r"\1", LineText, 0, re.IGNORECASE)
						# editor.replaceWholeLine(LineNumber, LineText)
	Match = re.search(r"^([;~]?(?:[\t ]+)?)" + r"(#?\b\w+\b)" + r"(?:[\t ]+)?,(?:[\t ]+)?" + r"([^\s])", LineText)
	if (Match is not None):
		Command = Match.group(2)
		Match = re.search(r"^([;~]?(?:[\t ]+)?)" + Command + r"\b" + r"(?:[\t ]+)?,(?:[\t ]+)?" + r"([^\s])", LineText, re.IGNORECASE)
		if (Match is not None):
			# console.write(LineText)
			LineText = re.sub(r"^([;~]?(?:[\t ]+)?)" + Command + r"\b" + r"(?:[\t ]+)?,(?:[\t ]+)?" + r"([^\s])", r"\1" + Command + r", \2", LineText, 0, re.IGNORECASE)
			# editor.replaceWholeLine(LineNumber, LineText)
	Match = re.search(r",[ \t]+,", LineText, re.IGNORECASE)
	if (Match is not None):
		for x in range(0, 2):
			LineText = re.sub(r",[ \t]+,", ",,", LineText, 0, re.IGNORECASE)
		# editor.replaceWholeLine(LineNumber, LineText)
	if (LineText != LineTextOld):
		editor.replaceWholeLine(LineNumber, LineText)
		console.write(str(LineNumber+1) + ". " + LineText)

def FixCommas():
	editor.forEachLine(FixCommasFunc)
	# editor.gotoPos(DocumentStartingPosition)
	console.write("\nFix Commas for Commands:\tDone.\n")

def FixCase():
	# editor.forEachLine(FixCaseFunc)
	# editor.gotoPos(DocumentStartingPosition)
	FixCaseFunc()
	console.write("Fix Case for Commands:\t\tDone.\n")

def ReIndent():
	notepad.runMenuCommand("Синтаксисы", "AutoHotkey (Indent)")
	editor.documentEnd()
	notepad.runPluginCommand("Indent By Fold", "Reindent File")
	notepad.runMenuCommand("Синтаксисы", "AutoHotkey")
	editor.gotoPos(DocumentStartingPosition)
	console.write("Fix Indentation for Code:\tDone.\n")

# First we"ll start an undo action, then Ctrl-Z will undo the actions of the whole script
editor.beginUndoAction()

FixCommas()
FixCase()
ReIndent()

# End the undo action, so Ctrl-Z will undo the above actions
editor.endUndoAction()
# Turn the undo recorder back on.
editor.setUndoCollection(1)

notepad.runMenuCommand("Синтаксисы", "AutoHotkey")

# editor.gotoPos(DocumentStartingPosition)

console.write("\nREADY.\n")

