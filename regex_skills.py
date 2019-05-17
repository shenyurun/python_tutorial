import re

# use () to group things
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1) # '415'
mo.group(2) # '555-4242'
mo.group(0) # '415-555-4242'
mo.group() 	# '415-555-4242'
mo.groups() # ('415', '555-4242')

# use | to group any of patterns
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo1.group() # 'Batman'
mo2 = heroRegex.search('Tina Fey and Batman.')
mo2.group() # 'Tina Fey'

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()  # 'Batmobile'
mo.group(1) # 'mobile'

# use ? to match 0 or 1 time of pattern
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo2 = phoneRegex.search('My number is 555-4242')
mo2.group() # '555-4242'

# use * to match 0 or more times of pattern
batRegex = re.compile(r'Bat(wo)*man')
mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group() # 'Batwowowowoman'

# use + to match 1 or more times of pattern
batRegex = re.compile(r'Bat(wo)+man')
mo3 = batRegex.search('The Adventures of Batman')
mo3 == None # True

# use {} to assign times of pattern (a value or a range)
haRegex = re.compile(r'(Ha){3}')
haRegex = re.compile(r'(Ha){3,}')
haRegex = re.compile(r'(Ha){,5}')
haRegex = re.compile(r'(Ha){3,5}') # greedy match
haRegex = re.compile(r'(Ha){3,5}?') # non-greedy match, different from previous ? usage

# findall return a list of all matching string
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# ['415-555-9999', '212-555-0000']
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# [('415', '555', '1122'), ('212', '555', '0000')]

# useful
# \d 0-9
# \D any character except 0-9
# \w alphabet, digit and _
# \W any character except alphabet, digit and _
# \s space, \n and \t
# \S any character except space, \n and \t

# use [] to define by self
alnumRegex = re.compile(r'[a-zA-Z0-9]')
nonAlnumRegex = re.compile(r'[^a-zA-Z0-9]')
# . * ? () in [] do not need to use \

# use ^ to match string begins with pattern
beginsWithHello = re.compile(r'^Hello')
# use $ to match string ends with pattern
endsWithNumber = re.compile(r'\d$') 
# use ^ and $ to strictly match whole string with pattern
onlyNumber = re.compile(r'^\d+$')

# use . to match any character except \n
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
# ['cat', 'hat', 'sat', 'lat', 'mat']

# use .* to match anything (greedy)
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Yurun Last Name: Shen')

# use ? to match in a non-greedy way
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
mo.group() # '<To serve man>'

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group() # '<To serve man> for dinner.

# use re.DOTALL to match multiple lines
newlineRegex = re.compile('.*', re.DOTALL)

# use re.IGNORECASE or re.I to ignore upper or lower case
robocop = re.compile(r'robocop', re.I)

# use sub() to replace pattern
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
# 'CENSORED gave the secret documents to CENSORED.'

# use re.VERBOSE to allow multi-line pattern and comments
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?				# area code
	(\s|-|\.)? 						# separator
    \d{3}							# first 3 digits
	(\s|-|\.)						# separator
	\d{4}							# last 4 digits
	(\s*(ext|x|ext.)\s*\d{2,5})?	# extension
)''', re.VERBOSE)




