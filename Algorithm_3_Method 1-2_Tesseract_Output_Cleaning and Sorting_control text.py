#Remove empty lines
editor.rereplace('^\\n','')

# Remove faulty start
editor.rereplace('(\\x0C)(0000000)','\\11111111\\n\\2')

# Fix faulty end
editor.rereplace('[1-9]000000','0000000')

# Fix fault End Control
editor.rereplace('(000000[0-9])[\\. ]*([1-3][0-9]{6})','\\1 \\2')

# Change slash /, backslash \\ and minus - to dot
editor.rereplace('[/\\\\-]','.')

# Remove faulty characters
editor.rereplace('^\\d{0,1}[. ]*\\d{0,1}\\r*\\n','')


# Fix dots
editor.rereplace(' *[\\.] *','.')

# Newline on start
editor.rereplace('(\\x0C)','\\n\\1')

# Fix start
editor.rereplace('(^[1]{7})(\\d)','\\1 \\2')


# Remove faulty characters 2
editor.rereplace('[\\. ]+$','')

# Remove faulty character 3
editor.rereplace('^[\\. ]+','')

# Remove multiple dots
editor.rereplace('(\\.+)','.')

# Remove doubles
editor.rereplace('^\\d\\.* \\d$\\n','')

# Remove solo digits
editor.rereplace('^\\d ','')

# Newline  after year
editor.rereplace('(\\.202[2-5])[\\. ]*(.+)','\\1\\n\\2')


# --------------------------------------------------
i=1
while (i<3):
# Date Fixing faulty dates
    editor.rereplace('(.*\\d*\\.)(\\d+\\.\\d+\\.20\\d+)','\\2')

# Date Fixing fix day from example 2.02.2022 02.02.2022
    editor.rereplace('^(?!0)([0-9])(\\.[0-9]+\\.[0-9]+)','0\\1\\2')

# Date Fixing fix day from example 0.02.2022 10.02.2022
    editor.rereplace('^([0])(\\.[0-9]+\\.[0-9]+)','1\\1\\2')

# Date Fixing fix month from example 02.2.2022 02.02.2022
    editor.rereplace('([0-9][0-9]\\.)([0-9])(\\.\\d+)','\\10\\2\\3')

# Date Fixing fix year from example 02.02.22 02.02.2022
    editor.rereplace('[\\.]2([2-9])[$\\.]*.*','.202\\1')

# Date Fixing fix monthyear example 02.022022 02.02.2022
    editor.rereplace('(\\.\\d\\d)(202\\d)','\\1.\\2')

# Date Fixing fix daymonth example 0202.2022 02.02.2022
    editor.rereplace('(\\d\\d)(\\d\\d\\.2022)','\\1.\\2')

# Fix Long year example 02.02.20225 02.02.2022
    editor.rereplace('(\\.202[23]).+','\\1')

# Fix Long day example 102.02.2022 02.02.2022
    editor.rereplace('\\d(\\d\\d\\.\\d\\d\\.202[23])','\\1')

# Fix OCR-wrong read date start with 6, 8 or 9 is 0
    editor.rereplace('[689](\\d\\.\\d+\\.\\d+)','0\\1')

# Fix OCR-wrong read date start with 4 or 7 is 1
    editor.rereplace('[47](\\d\\.\\d+\\.\\d+)','1\\1')

# Fix OCR-wrong read month start with 1 is original /
    editor.rereplace('(\\d\\d\\.)[1-9]([3-9])(\\.202[2-5])','\\10\\2\\3')
    i=i+1

# -------------------------------------------------------------------

# Fix missing controlltext 1 Start and Finish
editor.rereplace('^[0]{4,6} ','0000000 ')

# Fix missing controlltext 1 Start and Finish
editor.rereplace('^[1]{4,6} ','1111111 ')

# Fix missing controlltext 1 Start and Finish
editor.rereplace('^[1]{4,6}$','1111111')

# Fix missing controlltext 1 Start and Finish
editor.rereplace('^[0]{4,6}$','0000000')

# Remove faulty text
editor.rereplace('^(?!.*\\d\\d\\.\\d\\d.\\d\\d\\d\\d)(?!.*1111111)(?!.*0000000)(?!.*[0-9]{7}).*$','')

# Newline on start
editor.rereplace('(\\x0C)','\\n\\1')

# Change start
editor.rereplace('1111111','\#\#\#\#\#\#\#')

# Change end
editor.rereplace('0000000','-------')

# run 3 times
i=1
while (i<3):
# Move end to end
    editor.rereplace('(?!------- )(-------)\\r*\\n*(?!\#\#\#\#\#\#\#)(.+\\r*\\n*)(?!\#\#\#\#\#\#\#)(.*\\r*\\n*)(?!\#\#\#\#\#\#\#)(.*\\r*\\n*)(?!\#\#\#\#\#\#\#)(.*)','\\2\\3\\4\\5\\1\\r\\n')
    i=i+1
# Fix lines
editor.rereplace('(^\\n)(-------)','\\2\\1')

# run 3 times
i=1
while (i<3):
# Move date to end
    editor.rereplace('(\\d\\d\\.\\d\\d\\.202[23])\\r*\\n*(?!-------)(.+\\r*\\n*)(?!-------)(.*\\r*\\n*)(?!-------)(.*\\r*\\n*)(?!-------)(.*\\r*\\n*)','\\2\\3\\4\\5\\1\\r\\n')
    i=i+1


# run 3 times
i=1
while (i<3):
# Fix Start non control
    editor.rereplace('(\\x0C\#*)(\\d.+)','\\1\\n\\2')
# Fix missing Start control
    editor.rereplace('(\\x0C)$','\\1\#\#\#\#\#\#\#')
# Fix missing Start control 2
    editor.rereplace('(\\x0C)(?!\#)','\\1\#\#\#\#\#\#\#')
# Fix Start Control
    editor.rereplace('(\\x0C)(?!.*[0-9]{7}).*\\r*\\n([0-9]{7})','\\1 \\2')
# Move date to mid
    editor.rereplace('^([0-9]{7})\\r*\\n*(\\d\\d\\.\\d\\d\\.202[23])\\r*\\n*(?!-------)(.*)\\r*\\n*(?!-------)(.*)','\\2\\3\\4\\r\\n\\1')
# Fix End Control
    editor.rereplace('^([0-9]{7})\\r*\\n(-------)','\\2 \\1')
# Control Start
    editor.rereplace('(\\d)(\\x0C\#\#\#\#\#\#\#)','\\1\\r\\n\\r\\n\\2')
# Fix double dates
    editor.rereplace('(\\d\\d\\.\\d\\d\\.202[23])\\r*\\n*(\\d\\d\\.\\d\\d\\.202[23])','\\1')
# Merge lines
    editor.rereplace('(\\x0C.+)\\r*\\n*(?!-------)(.*)\\r*\\n*(-*.*)','\\1\\t\\2\\t\\3')
# Fix merge
    editor.rereplace('.(\\x0C)','\\n\\n\\1')
# Fix start missing control
    editor.rereplace('(\\x0C\#\#\#\#\#\#\#)(?! [0-9]{7}).*(\\t.*\\t.+)([0-9]{7})','\\1 \\3\\2\\3')
    i=i+1

#Remove anomalies (double lines)
editor.rereplace('(\\x0C.+)\\r*\\n(.+)','\\1 \\2')

# New line and tab on start
editor.rereplace('(.+)\\n','\\1')

# Fix linebreak
editor.rereplace('(.+)(\\x0C)','\\1\\n\\2')

# Remove symbols (# -)
editor.rereplace('[\\x0C\#-]+ *','')

# Remove last control
editor.rereplace('(^[0-9]{7}.+)[\\.\\t*][0-9]{7}','\\1')

# Fix format
editor.rereplace('([0-9]{7}).+(\\d\\d\\.\\d\\d.\\d{4})','\\1\\t\\2')

# Fix ending
editor.rereplace('(\\d)[\\t ]+$','\\1')

# Remove wrong format data
editor.rereplace('([0-9]{7}\\t\\d{2}\\.\\d{2}\\.\\d{4})\\t*(?!\\d\\d\\.\\d\\d\\.\\d\\d\\d\\d$).+','\\1')

# Remove faulty data
editor.rereplace('([0-9]{7})(?!\\t\\d\\d\\.\\d\\d\\.\\d\\d\\d\\d$).+','\\1')

# Remove blanks
editor.rereplace('^\\n','')

# Fix faulty placement of control
editor.rereplace('^\\t+ *(.+)','\\1')

# Remove dots from start
editor.rereplace('^\\.','')

# Fix wrong format
editor.rereplace('(^\\d)+ (\\d+)','\\1\\2')

# Finds and marks out faulty control text
editor.rereplace('^(?!1)\\d+','Wrong Format')

# Fix line feed
editor.rereplace('\\x0D\\x0A','\\x0A')
