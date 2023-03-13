editor.rereplace('^\\n','') #Remove empty lines

editor.rereplace('(\\x0C)(0000000)','\\11111111\\n\\2') # Remove faulty start

editor.rereplace('[1-9]000000','0000000') # Fix faulty end

editor.rereplace('(000000[0-9])[\\. ]*([1-3][0-9]{6})','\\1 \\2') # Fix fault End Control

editor.rereplace('[/\\\\-]','.') # Change slash /, backslash \\ and minus - to dot

editor.rereplace('^\\d{0,1}[. ]*\\d{0,1}\\r*\\n','') # Remove faulty characters


editor.rereplace(' *[\\.] *','.') # Fix dots

editor.rereplace('(\\x0C)','\\n\\1') # Newline on start

editor.rereplace('(^[1]{7})(\\d)','\\1 \\2') # Fix start


editor.rereplace('[\\. ]+$','') # Remove faulty characters 2

editor.rereplace('^[\\. ]+','') # Remove faulty character 3

editor.rereplace('(\\.+)','.') # Remove multiple dots

editor.rereplace('^\\d\\.* \\d$\\n','') # Remove doubles

editor.rereplace('^\\d ','') # Remove solo digits

editor.rereplace('(\\.202[2-5])[\\. ]*(.+)','\\1\\n\\2') # Newline  after year


# --------------------------------------------------
i=1
while (i<3):
    editor.rereplace('(.*\\d*\\.)(\\d+\\.\\d+\\.20\\d+)','\\2') # Date Fixing faulty dates

    editor.rereplace('^(?!0)([0-9])(\\.[0-9]+\\.[0-9]+)','0\\1\\2') # Date Fixing fix day from example 2.02.2022 02.02.2022

    editor.rereplace('^([0])(\\.[0-9]+\\.[0-9]+)','1\\1\\2') # Date Fixing fix day from example 0.02.2022 10.02.2022

    editor.rereplace('([0-9][0-9]\\.)([0-9])(\\.\\d+)','\\10\\2\\3') # Date Fixing fix month from example 02.2.2022 02.02.2022

    editor.rereplace('[\\.]2([2-9])[$\\.]*.*','.202\\1') # Date Fixing fix year from example 02.02.22 02.02.2022

    editor.rereplace('(\\.\\d\\d)(202\\d)','\\1.\\2') # Date Fixing fix monthyear example 02.022022 02.02.2022

    editor.rereplace('(\\d\\d)(\\d\\d\\.2022)','\\1.\\2') # Date Fixing fix daymonth example 0202.2022 02.02.2022

    editor.rereplace('(\\.202[23]).+','\\1') # Fix Long year example 02.02.20225 02.02.2022

    editor.rereplace('\\d(\\d\\d\\.\\d\\d\\.202[23])','\\1') # Fix Long day example 102.02.2022 02.02.2022

    editor.rereplace('[689](\\d\\.\\d+\\.\\d+)','0\\1') # Fix OCR-wrong read date start with 6, 8 or 9 is 0

    editor.rereplace('[47](\\d\\.\\d+\\.\\d+)','1\\1') # Fix OCR-wrong read date start with 4 or 7 is 1

    editor.rereplace('(\\d\\d\\.)[1-9]([3-9])(\\.202[2-5])','\\10\\2\\3') # Fix OCR-wrong read month start with 1 is original /
    i=i+1

# -------------------------------------------------------------------

editor.rereplace('^[0]{4,6} ','0000000 ') # Fix missing controlltext 1 Start and Finish

editor.rereplace('^[1]{4,6} ','1111111 ') # Fix missing controlltext 1 Start and Finish

editor.rereplace('^[1]{4,6}$','1111111') # Fix missing controlltext 1 Start and Finish

editor.rereplace('^[0]{4,6}$','0000000') # Fix missing controlltext 1 Start and Finish

editor.rereplace('^(?!.*\\d\\d\\.\\d\\d.\\d\\d\\d\\d)(?!.*1111111)(?!.*0000000)(?!.*[0-9]{7}).*$','') # Remove faulty text

editor.rereplace('(\\x0C)','\\n\\1') # Newline on start

editor.rereplace('1111111','\#\#\#\#\#\#\#') # Change start

editor.rereplace('0000000','-------') # Change end

# run 3 times
i=1
while (i<3):
    editor.rereplace('(?!------- )(-------)\\r*\\n*(?!\#\#\#\#\#\#\#)(.+\\r*\\n*)(?!\#\#\#\#\#\#\#)(.*\\r*\\n*)(?!\#\#\#\#\#\#\#)(.*\\r*\\n*)(?!\#\#\#\#\#\#\#)(.*)','\\2\\3\\4\\5\\1\\r\\n') # Move end to end
    i=i+1
editor.rereplace('(^\\n)(-------)','\\2\\1') # Fix lines

# run 3 times
i=1
while (i<3):
    editor.rereplace('(\\d\\d\\.\\d\\d\\.202[23])\\r*\\n*(?!-------)(.+\\r*\\n*)(?!-------)(.*\\r*\\n*)(?!-------)(.*\\r*\\n*)(?!-------)(.*\\r*\\n*)','\\2\\3\\4\\5\\1\\r\\n') # Move date to end
    i=i+1


# run 3 times
i=1
while (i<3):
    editor.rereplace('(\\x0C\#*)(\\d.+)','\\1\\n\\2') # Fix Start non control
    editor.rereplace('(\\x0C)$','\\1\#\#\#\#\#\#\#') # Fix missing Start control
    editor.rereplace('(\\x0C)(?!\#)','\\1\#\#\#\#\#\#\#') # Fix missing Start control 2
    editor.rereplace('(\\x0C)(?!.*[0-9]{7}).*\\r*\\n([0-9]{7})','\\1 \\2') # Fix Start Control
    editor.rereplace('^([0-9]{7})\\r*\\n*(\\d\\d\\.\\d\\d\\.202[23])\\r*\\n*(?!-------)(.*)\\r*\\n*(?!-------)(.*)','\\2\\3\\4\\r\\n\\1') # Move date to mid
    editor.rereplace('^([0-9]{7})\\r*\\n(-------)','\\2 \\1') # Fix End Control
    editor.rereplace('(\\d)(\\x0C\#\#\#\#\#\#\#)','\\1\\r\\n\\r\\n\\2') # Control Start
    editor.rereplace('(\\d\\d\\.\\d\\d\\.202[23])\\r*\\n*(\\d\\d\\.\\d\\d\\.202[23])','\\1') # Fix double dates
    editor.rereplace('(\\x0C.+)\\r*\\n*(?!-------)(.*)\\r*\\n*(-*.*)','\\1\\t\\2\\t\\3') # Merge lines
    editor.rereplace('.(\\x0C)','\\n\\n\\1') # Fix merge
    editor.rereplace('(\\x0C\#\#\#\#\#\#\#)(?! [0-9]{7}).*(\\t.*\\t.+)([0-9]{7})','\\1 \\3\\2\\3') # Fix start missing control
    i=i+1

editor.rereplace('(\\x0C.+)\\r*\\n(.+)','\\1 \\2') #Remove anomalies (double lines)

editor.rereplace('(.+)\\n','\\1') # New line and tab on start

editor.rereplace('(.+)(\\x0C)','\\1\\n\\2') # Fix linebreak

editor.rereplace('[\\x0C\#-]+ *','') # Remove symbols (# -)

editor.rereplace('(^[0-9]{7}.+)[\\.\\t*][0-9]{7}','\\1') # Remove last control

editor.rereplace('([0-9]{7}).+(\\d\\d\\.\\d\\d.\\d{4})','\\1\\t\\2') # Fix format

editor.rereplace('(\\d)[\\t ]+$','\\1') # Fix ending

editor.rereplace('([0-9]{7}\\t\\d{2}\\.\\d{2}\\.\\d{4})\\t*(?!\\d\\d\\.\\d\\d\\.\\d\\d\\d\\d$).+','\\1') # Remove wrong format data

editor.rereplace('([0-9]{7})(?!\\t\\d\\d\\.\\d\\d\\.\\d\\d\\d\\d$).+','\\1') # Remove faulty data

editor.rereplace('^\\n','') # Remove blanks

editor.rereplace('^\\t+ *(.+)','\\1') # Fix faulty placement of control

editor.rereplace('^\\.','') # Remove dots from start

editor.rereplace('(^\\d)+ (\\d+)','\\1\\2') # Fix wrong format

editor.rereplace('^(?!1)\\d+','Wrong Format') # Finds and marks out faulty control text

editor.rereplace('\\x0D\\x0A','\\x0A') # Fix line feed
