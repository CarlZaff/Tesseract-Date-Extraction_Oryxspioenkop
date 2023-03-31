#Whitelist of unit definitions
units = []
units2 = []
u = 0

units.append('Tanks')
units.append('Armoured Fighting Vehicles')
units.append('Infantry Fighting Vehicles')
units.append('Armoured Personnel Carriers')
units.append('Mine-Resistant Ambush Protected \\(MRAP\\) Vehicles')
units.append('Infantry Mobility Vehicles')
units.append('Command Posts And Communications Stations')
units.append('Engineering Vehicles And Equipment')
units.append('Self-Propelled Anti-Tank Missile Systems')
units.append('Artillery Support Vehicles And Equipment')
units.append('Towed Artillery')
units.append('Self-Propelled Artillery')
units.append('Multiple Rocket Launchers')
units.append('Self-Propelled Anti-Aircraft Guns')
units.append('Surface-To-Air Missile Systems')
units.append('Radars')
units.append('Jammers And Deception Systems')
units.append('Helicopters')
units.append('Unmanned Combat Aerial Vehicles')
units.append('Reconnaissance Unmanned Aerial Vehicles')
units.append('Naval Ships')
units.append('Trucks, Vehicles and Jeeps')

# Whitelist 2 with different ruleset
units2.append('Anti-Aircraft Guns')
units2.append('Aircraft')


# HTTPS URL to new row
editor.rereplace('(<a href=")','\\n\\1')

# HTTPS URL to new row
editor.rereplace('(https:)','\\n\\1')

# Remove wikimedia links (flags, etc.)
editor.rereplace('^.+wikimedia.+\\.png','')

# Summary to new row
editor.rereplace('(Russia - .+)','\\n// Summary \\1')

# Move whitelisted units to new row
while u < len(units):
    editor.rereplace('.+'+(units[u]),'\\n// new unit below '+units[u]+'\\t\\t\\t')
    u = u+1

# Move whitelisted units2 to new row, using ruleset that doesn't mess upp other units
editor.rereplace('(?!.*Self-Propelled Anti-Aircraft Guns)^.*'+(units2[0]),'\\n// new unit below '+units2[0]+'\\t\\t\\t')
editor.rereplace('(?!.*Anti-Aircraft)^.*'+(units2[1]),'\\n// new unit below '+units2[1]+'\\t\\t\\t')


# Clean-up headers
editor.rereplace('<br></span></h3><p style="text-align: left;"><br></p><h3>','')

# Clean-up headers 2
editor.rereplace('</h3><h3>','')

# Clean vehicle row
editor.rereplace('(&nbsp;)','\\n\\1')

# Correct URLs and move status to 5th column
i=1
while (i<3):
 editor.rereplace('^(https:.+/.+)">* *(\\(*)','\\1\\t\\t\\t\\t\\t\\2')
 i=i+1

# mark new vehicles
editor.rereplace('width="\\d*">','\\n// new vehicle below')

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

# Fix new vehicle, instance where vehicle quantity is not in correct place
editor.rereplace('(// new vehicle below) *(\\d.*)','\\1\\n\\2')

# Fix new vehicle, move vehicle quantity to correct place
editor.rereplace('(// new vehicle below) *\\n(?!https.*)(.*)\\n*(?!https.*)(.*)','\\1\\n\\2 \\3')

# Remove unwanted characters
editor.rereplace('<.+>','')

# Remove unwanted lines
editor.rereplace('^<.*["=]+.+\\n','')

# Fix URL with status
editor.rereplace('(?!^.*https.*\\t\\t\\t\\t\\t.*$)(^https.+)(".+)','\\1\\t\\t\\t\\t\\t\\2')

# Remove forbidden characters
editor.rereplace('["<>]','')

# Remove double spaces
editor.rereplace(' +',' ')

# Patch // new vehicles/units
editor.rereplace('(^//.+$)\\n(.+)','\\1 \\2')

# Remove contributors
editor.rereplace('(^Special thanks to.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*\\r*\\n*.*)','')

# Remove faulty lines
editor.rereplace('(?!^[h/])^.+','')

# Fix blank rows
editor.rereplace('^ *\\r*\\n','')

# Restore // new vehicles
editor.rereplace('(// new vehicle below) *(.+)','\\1\\n\\2')

# Restore // new unit
editor.rereplace('(// new unit below) *(.+)','\\1\\n\\2')

# Restore // summary
editor.rereplace('(// Summary) *(.+)','\\1\\n\\t\\t\\t\\t\\2')

# Format document to fix excel sheet -------------------------------------

# Move links
editor.rereplace('(https:)','\\t\\t\\t\\1')

# Move unit types
editor.rereplace('(// new unit below.*\\r*\\n)(.+)','\\t\\1\\t\\2')

# Move vehicles
editor.rereplace('(// new vehicle below.*\\r*\\n)(\\d+) *(.+)','\\t\\t\\1\\2\\t\\t\\3')

# Fix extensive tabs
editor.rereplace('\\t\\t\\t\\t\\t','\\t')

# Move unit status to correct column
# Pause, might be resolved on line 69 editor.rereplace(' +(\\(\\d.+\\))','\\t\\t\\t\\1')

# Remove meta text marked with //
editor.rereplace('// .+','')

# Fix faulty URL (status)
editor.rereplace('(?!https://.+\\t)(https:.+) *(\\()','\\1\\t\\2')
