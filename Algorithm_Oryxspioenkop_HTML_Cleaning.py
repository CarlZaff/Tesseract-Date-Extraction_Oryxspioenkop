# ------------------- HTML Cleaning and sorting -------------------------

# HTTPS URL to new row
editor.rereplace('(<a href=")','\\n\\1')

# HTTPS URL to new row
editor.rereplace('(https:)','\\n\\1')

# Remove wiki links
editor.rereplace('^.+wikimedia.+\\.png','')

# Summary to new row
editor.rereplace('(Russia - .+)','\\n\\1')

# Clean-up headers
editor.rereplace('<br></span></h3><p style="text-align: left;"><br></p><h3>','')

# Clean-up headers 2
editor.rereplace('</h3><h3>','')

# Move vehicles to new row
editor.rereplace('(&nbsp;)','\\n\\1')

# Correct URLs and move status to 5th column
editor.rereplace('^(https:.+/.+)">* *(\\(*)','\\1\\t\\t\\t\\t\\t\\2')

# mark new units
editor.rereplace('width="\\d*">','\\n// new vehicle below')

# Move unit to new row
editor.rereplace('<h3>','\\n// new unit below\\n')

# Move unit to new row 2
editor.rereplace('.+Pistols">','\\n// new unit below\\n')

# Remove unnecessary text after status text
editor.rereplace('(\\(\\d+,.+\\)).+','\\1')
 
# Remove unnecessary text 2
editor.rereplace('<a href="','')

# Remove unnecessary text 3
editor.rereplace('&nbsp;','')

# Remove html
editor.rereplace('</*span>','')

# Remove html
editor.rereplace('</*div>','')

# Remove html
editor.rereplace('</*h3>','')

# Remove html
editor.rereplace('</*li>','')

# Remove html
editor.rereplace('</*ul>','')

# Fix blank rows
editor.rereplace('^ *\\r*\\n','')

# Fix new vehicle
editor.rereplace('(// new vehicle below) *(\\d.*)','\\1\\n\\2')

# Fix new vehicle 2
editor.rereplace('(// new vehicle below) *\\n(?!https.*)(.*)\\n*(?!https.*)(.*)\\n*(?!https.*)(.*)\\n*(?!https.*)(.*)','\\1\\n\\2 \\3')

# run 3 times to fix any itteration of multiple "unit below"
i=1
while (i<3):
 editor.rereplace('// new unit below\\r*\\n(// new unit below)','\\1') # Fix double units
 i=i+1

# Remove unwanted characters
editor.rereplace('<.+>','')

# Remove unwanted lines
editor.rereplace('^<.*["=]+.+\\n','')

editor.rereplace('(?!^.*https.*\\t\\t\\t\\t\\t.*$)(^https.+)(".+)','\\1\\t\\t\\t\\t\\t\\2')# Fix URL with status

# Remove forbidden characters
editor.rereplace('["<>]','')

# Remove double spaces
editor.rereplace(' +',' ')

# Patch // new vehicles/units
editor.rereplace('(^//.+$)\\n(.+)','\\1 \\2')

# Remove faulty lines
editor.rereplace('(?!^[h/])^.+','')

# Fix blank rows
editor.rereplace('^ *\\r*\\n','')

# Restore // new vehicles
editor.rereplace('(// new vehicle below) (.+)','\\1\\n\\2')

# Restore // new unit
editor.rereplace('(// new unit below) (.+)','\\1\\n\\2')


#-------------- Format document to fix excel sheet ----------------------

# Move links
editor.rereplace('(https:)','\\t\\t\\t\\1')

# Move unit types
editor.rereplace('(// new unit below.*\\r*\\n)(.+)','\\t\\1\\t\\2')

# Move vehicles
editor.rereplace('(// new vehicle below.*\\r*\\n)(\\d+) *(.+)','\\t\\t\\1\\2\\t\\t\\3')

# Fix extensive tabs
editor.rereplace('\\t\\t\\t\\t\\t','\\t')

# Move unit status to correct column
editor.rereplace(' +(\\(\\d.+\\))','\\t\\t\\t\\1')

# Remove meta text // new unit/vehicle
editor.rereplace('// new .+','')
