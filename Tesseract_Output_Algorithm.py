#Fix lines
editor.rereplace('(\\x0C)','\\n\\1')

#Remove empty lines
editor.rereplace('^\\n','')

# Newline  after start
editor.rereplace('(\\x0C)','\\1\\n')

# Change slash /, backslash \\ and minus - to dot
editor.rereplace('[/\\\\-]','.')

# Remove faulty lines such as "4."
editor.rereplace('^\\d{0,1}[. ]*\\d{0,1}$','')

# Fix space before or after dot
editor.rereplace(' *[\\.] *','.')

# Remove dots or spaces at end of line
editor.rereplace('[\\. ]+$','')

# Remove dot or space at start of line
editor.rereplace('^[\\. ]+','')

# Remove multiple dots in line
editor.rereplace('(\\.+)','.')

# Split line after legit year
editor.rereplace('(\\.202[2-5])[\\. ]*(.+)','\\1\\n\\2')

# Remove lines concisting of doubles such as "4.2" or "45"
# editor.rereplace('^\\.*\\d\\.*\\d$\\r*\\n','')

# Remove lines concisting of single digits
# editor.rereplace('^\\.*\\d\\.*$','')


# --------------------------------------------------
# looping algorithm for fixing dates to correct format
i=1
while (i<3):
# Fixing faulty lenght in dates example 4.3.2.1.2.3.29.03.2022 -> 29.03.2022
    editor.rereplace('(.*[\\. ])(\\d+\\.\\d+\\.2[0-3]\\d*)','\\2')

# Date Fixing fix day from example 2.02.2022 -> 02.02.2022
    editor.rereplace('^(?!0)([0-9])(\\.[0-9]+\\.[0-9]+)','0\\1\\2')

# Date Fixing fix day from example 0.02.2022 -> 10.02.2022
    editor.rereplace('^([0])(\\.[0-9]+\\.[0-9]+)','1\\1\\2')

# Date Fixing fix month from example 02.2.2022 -> 02.02.2022
    editor.rereplace('([0-9][0-9]\\.)([0-9])(\\.\\d+)','\\10\\2\\3')

# Date Fixing fix short year from example 02.02.22 -> 02.02.2022
    editor.rereplace('[\\.]2([2-9])[$\\.]*.*','.202\\1')

# Date Fixing fix monthyear example 02.022022 -> 02.02.2022
    editor.rereplace('(\\.\\d\\d)(202\\d)','\\1.\\2')

# Date Fixing fix daymonth example 0202.2022 -> 02.02.2022
    editor.rereplace('(\\d\\d)(\\d\\d\\.2022)','\\1.\\2')

# Fix Long year example 02.02.20225 -> 02.02.2022
    editor.rereplace('(\\.202[2-6]).+','\\1')

# Fix Long day example 102.02.2022 -> 02.02.2022
    editor.rereplace('.+(\\d\\d\\.\\d\\d\\.202[23])','\\1')

# Fix OCR-character mix-up, date starting with 6, 8 or 9 is 0 example 62.02.2022 -> 02.02.2022
    editor.rereplace('[689](\\d\\.\\d+\\.\\d+)','0\\1')

# Fix OCR-character mix-up, date starting with 4 or 7 is 1 example 72.02.2022 -> 02.02.2022
    editor.rereplace('[47](\\d\\.\\d+\\.\\d+)','1\\1')

# Fix OCR-character mix-up, read month start with 1 is original / example example 02/5/2022 -> 02.15.2022 -> 02.05.2022
    editor.rereplace('(\\d\\d\\.)[1-9]([3-9])(\\.202[2-5])','\\10\\2\\3')

    
    i=i+1

# -------------------------------------------------------------------


# Remove faulty text
editor.rereplace('^(?!.*\\d\\d\\.\\d\\d.\\d\\d\\d\\d)(?!.*1111111)(?!.*0000000)(?!.*[0-9]{7}).*$','')

# Remove wrong format date
editor.rereplace('^(?!\\d\\d\\.\\d\\d\\.\\d\\d\\d\\d$).+','')

# Remove empty lines
editor.rereplace('^\\x0A','')

editor.rereplace('^\\x0C','\\n1010101\\t')# New line, control text, insert ID placeholder, and format to excel (\x0C)

# Remove empty lines
editor.rereplace('^\\x0A','')

# Remove multiple dates
editor.rereplace('^(?!1010101).+\\r*\\n','')

# Fix line feed, removes \r characters
editor.rereplace('\\x0D\\x0A','\\x0A')
