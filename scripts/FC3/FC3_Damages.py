# -*- coding: utf8 -*-

import re

console.show()
console.clear()

# get sign of a number by Greg Pinero
# http://www.answermysearches.com/python-how-to-get-the-sign-of-a-number/35/

# Here's a better way provided by Florent Guillaume:
def sign(number):return cmp(number,0)

# Count the number of characters, words and lines in the current editor window of Notepad++.
# http://www.sivachandran.in/2012/04/scripting-notepad-with-python.html
from Npp import *
def Count(string):
  numChars = 0
  numWords = 0
  numLines = 0

  editorContent = editor.getText()
  for line in editorContent.splitlines():
    numLines += 1
    for word in re.findall(string, line):
      numWords += 1
      numChars += len(word)
  return (numChars, numWords, numLines)
  
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

# notepad.messageBox("Number of characters: %d \nNumber of words: %d \nNumber of lines: %d" % Count("[a-zA-Z0-9]+"))
# notepad.messageBox("Number of characters: %d \nNumber of words: %d \nNumber of lines: %d" % (Count("[a-zA-Z0-9]+")[0],Count("[a-zA-Z0-9]+")[1],Count("[a-zA-Z0-9]+")[2]))

# определение переменных
fHeadDamageMultiplier  = 2
fTorsoDamageMultiplier = 1
fLegsDamageMultiplier  = 1
fBaseDamagePower       = 1
fBaseDamageMultiplier  = 1
fRecoilPerShotPower = 1
fRecoilPerShotMultiplier = 1
fRecoilMaxPitchMultiplier = 1
fSpreadMultiplier = 1
iBulletsShotNumber = 1

def selWeaponClass(m):
    try:
      #Get value from string
      global fRecoilPerShotPower
      global fBaseDamagePower
      global fBaseDamageMultiplier
      global fRecoilPerShotPower
      global fRecoilPerShotMultiplier
      global fRecoilMaxPitchMultiplier
      global fSpreadMultiplier
      global iBulletsShotNumber
      
      selWeaponClass = m.group(1)
      if selWeaponClass == 'Pistol':
        fBaseDamagePower = 0.5
        fBaseDamageMultiplier = float(pow(50*pow(2/fHeadDamageMultiplier,2), fBaseDamagePower))
        fRecoilPerShotPower = 1
        fRecoilPerShotMultiplier = 3
        
      if selWeaponClass == 'SMG':
        fBaseDamagePower = 0.5
        fBaseDamageMultiplier = float(pow(50*pow(2/fHeadDamageMultiplier,2), fBaseDamagePower))
        fRecoilPerShotPower = 1
        fRecoilPerShotMultiplier = 1.5
        
      if selWeaponClass == 'Shotgun':
        fBaseDamagePower = 0.5
        fBaseDamageMultiplier = float(pow(50*pow(2/fHeadDamageMultiplier,2), fBaseDamagePower))
        fSpreadMultiplier = 0.5
        iBulletsShotNumber = 15
        
      if selWeaponClass == 'Sniper':
        fBaseDamagePower = 0.5
        fBaseDamageMultiplier = float(pow(100*pow(2/fHeadDamageMultiplier,2), fBaseDamagePower))
        fRecoilPerShotPower = 1
        fRecoilPerShotMultiplier = 10
        
      if selWeaponClass == 'Assault':
        fBaseDamagePower = 0.5
        fBaseDamageMultiplier  = float(pow(120*pow(2/fHeadDamageMultiplier,2), fBaseDamagePower))
        fRecoilPerShotPower = 1 
        fRecoilPerShotMultiplier = 4.5
        
      if selWeaponClass == 'LMG':
        fBaseDamagePower = 0.5
        fBaseDamageMultiplier  = float(pow(80*pow(2/fHeadDamageMultiplier,2), fBaseDamagePower))
        fRecoilPerShotPower = 1 
        fRecoilPerShotMultiplier = 4.5
        fRecoilMaxPitchMultiplier = 10
        
      if selWeaponClass == 'RepairTool':
        return
        
    except:
      return m.group(0)
      
str_selWeaponClass = '<field name="selWeaponClass" type="Enum">(.*?)</field>'
editor.research(str_selWeaponClass, selWeaponClass, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))

# Get values from prompt window
expression = notepad.prompt(
  ''.decode('utf-8').encode('cp1251'),
  'Ввод данных:'.decode('utf-8').encode('cp1251'),
  ('fHeadDamageMultiplier = %s' + '; ' + 'fTorsoDamageMultiplier = %s' + '; ' + 'fLegsDamageMultiplier = %s' + '; ' + 'fBaseDamagePower = %s'+ '\r\n' + 'fBaseDamageMultiplier = %s' + '\r\n' + 'fRecoilPerShotPower = %s' + '; ' + 'fRecoilPerShotPower = %s' + '; ' + 'fRecoilMaxPitchMultiplier = %s') % (fHeadDamageMultiplier, fTorsoDamageMultiplier, fLegsDamageMultiplier, fBaseDamagePower, fBaseDamageMultiplier, fRecoilPerShotPower, fRecoilPerShotMultiplier, fRecoilMaxPitchMultiplier)
)

if expression != None:

  # преобразование кодировки ANSI в UTF-8
  expression = expression.decode('cp1251').encode('utf-8')

  console.show()
  console.clear()

  expression = re.sub('\r\n', '; ', expression)
  list = expression.split('; ')

  eqString = r'(\s+)?=(\s+)?'

  val_fHeadDamageMultiplier = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[0], 0, 0)))
  val_fTorsoDamageMultiplier = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[1], 0, 0)))
  val_fLegsDamageMultiplier = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[2], 0, 0)))

  val_fBaseDamagePower = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[3], 0, 0)))
  val_fBaseDamageMultiplier = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[4], 0, 0)))
  
  val_fRecoilPerShotPower = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[5], 0, 0)))
  val_fRecoilPerShotMultiplier = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[6], 0, 0)))
  
  val_fRecoilMaxPitchMultiplier = float(re.sub(',', '.', re.sub('[A-Za-z \t_=]', '', list[7], 0, 0)))
  
  def fBaseDamage(m):
    try:
      #Get value from string
      fLevel = float(m.group(3))
      # Normalizing value
      roundTo = 0

      if abs(fLevel) > 1:
        fLevel = round(pow(abs(fLevel), val_fBaseDamagePower)*val_fBaseDamageMultiplier, roundTo)*sign(fLevel)
      else:
        fLevel = round(pow(abs(fLevel), 1 / val_fBaseDamagePower)*val_fBaseDamageMultiplier, roundTo)*sign(fLevel)
        
      fLevel = int(fLevel)
        
      result = '%s<field name="fLevel" type="Float32">%s</field>' % (m.group(1), fLevel)
      console.write("BaseDamage >\n\tfLevel = %s\n\n" % fLevel)
    
      return result
    except:
      return m.group(0)
      
  def fDamageMultipliers(m):
    try:
      #Get value from string
      fHeadDamageMultiplier = val_fHeadDamageMultiplier
      fTorsoDamageMultiplier = val_fTorsoDamageMultiplier
      fLegsDamageMultiplier = val_fLegsDamageMultiplier
      
      result = '%s<field name="fHeadDamageMultiplier" type="Float32">%s</field>%s<field name="fTorsoDamageMultiplier" type="Float32">%s</field>%s<field name="fLegsDamageMultiplier" type="Float32">%s</field>' % (m.group(1), fHeadDamageMultiplier, m.group(3), fTorsoDamageMultiplier, m.group(5), fLegsDamageMultiplier)
      console.write("HitLocationMultiplier >\n\tfHeadDamageMultiplier = %s\n\tfTorsoDamageMultiplier = %s\n\tfLegsDamageMultiplier = %s\n\n" % (fHeadDamageMultiplier, fTorsoDamageMultiplier, fLegsDamageMultiplier))
      
      return result
    except:
      return m.group(0)
      
  def fRecoilMaxYaw(m):
    try:
      #Get value from string
      fRecoilMaxPitch = float(m.group(1))*val_fRecoilMaxPitchMultiplier
      fRecoilMaxYaw = float(m.group(3))
      fRecoilMaxYaw = round((fRecoilMaxPitch + fRecoilMaxYaw)/2, 1)
      result = '<field name="fRecoilMaxPitch" type="Float32">%s</field>%s<field name="fRecoilMaxYaw" type="Float32">%s</field>' % (fRecoilMaxPitch, m.group(2), fRecoilMaxYaw)
      console.write("Recoil >\n\tfRecoilMaxPitch = %s\n\tfRecoilMaxYaw = %s\n\n" % (fRecoilMaxPitch, fRecoilMaxYaw))
      return result
    except:
      return m.group(0)
      
  def fRange(m):
    try:
      #Get value from string
      fRange = int(m.group(1))
      fRange = int(pow(170, 0.5) * pow(fRange, 0.5))
      
      result = '<field name="fRange" type="Float32">%s</field>' % (fRange)
      console.write("CommonProperties >\n\tfRange = %s\n\n" % (fRange))
      
      return result
    except:
      return m.group(0)
      
  def fRecoilPerShot(m):
    try:
      #Get value from string
      value = pow(val_fRecoilPerShotMultiplier, val_fRecoilPerShotPower)
      fLeftRecoilPerShot = round(float(m.group(1))*value, 1)
      fRightRecoilPerShot = round(float(m.group(3))*value, 1)
      fVerticalRecoilPerShot = round(float(m.group(5))*value, 1)
      
      fLeftRollPerShot = round(float(m.group(7))*value, 1)
      fRightRollPerShot = round(float(m.group(9))*value, 1)
      
      result = '<field name="fLeftRecoilPerShot" type="Float32">%s</field>%s<field name="fRightRecoilPerShot" type="Float32">%s</field>%s<field name="fVerticalRecoilPerShot" type="Float32">%s</field>%s<field name="fLeftRollPerShot" type="Float32">%s</field>%s<field name="fRightRollPerShot" type="Float32">%s</field>' % (fLeftRecoilPerShot, m.group(2), fRightRecoilPerShot, m.group(4), fVerticalRecoilPerShot, m.group(6), fLeftRollPerShot, m.group(8), fRightRollPerShot)
      console.write("Recoil >\n\tfLeftRecoilPerShot = %s\n\tfRightRecoilPerShot = %s\n\tfVerticalRecoilPerShot = %s\n\tfLeftRollPerShot = %s\n\tfRightRollPerShot = %s\n\n" % (fLeftRecoilPerShot, fRightRecoilPerShot, fVerticalRecoilPerShot, fLeftRollPerShot, fRightRollPerShot))
      
      return result
    except:
      return m.group(0)
      
  def fSpread(m):
    try:
      #Get value from string          
      if fSpreadMultiplier != 1:
        fBaseSpread = round(float(m.group(1))*fSpreadMultiplier, 2)
        fMaxBulletSpread = round(float(m.group(3))*fSpreadMultiplier, 2)
      else:
        fBaseSpread = m.group(1)
        fMaxBulletSpread = m.group(3)   
     
      result = '<field name="fBaseSpread" type="Float32">%s</field>%s<field name="fMaxBulletSpread" type="Float32">%s</field>' % (fBaseSpread, m.group(2), fMaxBulletSpread)
      if fSpreadMultiplier != 1:
        console.write("BulletSpread >\n\tfBaseSpread = %s\n\tfMaxBulletSpread = %s\n\n" % (fBaseSpread, fMaxBulletSpread))
      
      return result
    except:
      return m.group(0)
      
  def iBulletsShot(m):
    try:
      #Get value from string    
      iBulletsShot = int(m.group(1))
      if iBulletsShotNumber != 1:
        iBulletsShot = int(iBulletsShotNumber)
     
      result = '<field name="iBulletsShot" type="Int32">%s</field>' % (iBulletsShot)
      if iBulletsShot != 1:
        console.write("FireStrategyProperties >\n\tiBulletsShot = %s\n\n" % (iBulletsShot))
      
      return result
    except:
      return m.group(0)

  # First we'll start an undo action, then Ctrl-Z will undo the actions of the whole script
  editor.beginUndoAction()

  str_fDamageMultipliers = '(\s+)<field name="fHeadDamageMultiplier" type="Float32">(.*?)</field>(\s+)<field name="fTorsoDamageMultiplier" type="Float32">(.*?)</field>(\s+)<field name="fLegsDamageMultiplier" type="Float32">(.*?)</field>'
  editor.rereplace(str_fDamageMultipliers, fDamageMultipliers, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))

  str_BaseDamage_fLevel = '(<object name="BaseDamage">(\s+.*?)+)<field name="fLevel" type="Float32">(.*?)</field>'
  editor.rereplace(str_BaseDamage_fLevel, fBaseDamage, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
  
  str_fRecoilMaxYaw = '<field name="fRecoilMaxPitch" type="Float32">(.*?)</field>(\s+)<field name="fRecoilMaxYaw" type="Float32">(.*?)</field>'
  editor.rereplace(str_fRecoilMaxYaw, fRecoilMaxYaw, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))

  str_fRange = '<field name="fRange" type="Float32">(.*?)</field>'
  editor.rereplace(str_fRange, fRange, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))

  str_fRecoilPerShot = '<field name="fLeftRecoilPerShot" type="Float32">(.*?)</field>(\s+)<field name="fRightRecoilPerShot" type="Float32">(.*?)</field>(\s+)<field name="fVerticalRecoilPerShot" type="Float32">(.*?)</field>(\s+)<field name="fLeftRollPerShot" type="Float32">(.*?)</field>(\s+)<field name="fRightRollPerShot" type="Float32">(.*?)</field>'
  editor.rereplace(str_fRecoilPerShot, fRecoilPerShot, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))

  str_fSpread = '<field name="fBaseSpread" type="Float32">(.*?)</field>(\s+)<field name="fMaxBulletSpread" type="Float32">(.*?)</field>'
  editor.rereplace(str_fSpread, fSpread, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))

  str_iBulletsShot = '<field name="iBulletsShot" type="Int32">(.*?)</field>'
  editor.rereplace(str_iBulletsShot, iBulletsShot, 0, editor.positionFromLine(editor.getUserLineSelection()[0]),editor.positionFromLine(editor.getUserLineSelection()[1]))
  
  # End the undo action, so Ctrl-Z will undo the above two actions
  editor.endUndoAction()
  # Turn the undo recorder back on.
  editor.setUndoCollection(1)

  # Write to the console window
  # console.write("START\n")

  # console.write("fHeadDamageMultiplier * %s\n" % val_fHeadDamageMultiplier)

  # console.write("END\n")
