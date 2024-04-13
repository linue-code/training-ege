#from itertools import *

#count = 0
#for x in product("WXYZ","ABC","ABC","ABC","ABC","WXYZ"):
#    s = ''.join(x)
#    count += 1
#print(count)]

#from itertools import *
#
#count = 0
#for x in product("œ”Àﬂ", repeat = 6):
#    s = ''.join(x)
#    if s.count('”') == 2:
#        count += 1
#print(count)

#from itertools import *
#
#count = 0
#for x in product("—¿ÀŒ",repeat = 6):
#    s = ''.join(x)
#    if 1 <= s.count('Œ') <= 3:
#        count += 1
#print(count)
#
#from itertools import *
#
#count = 0
#for x in permutations("»√–Œ "):
#    s = ''.join(x)
#    if s[0] != ' ' and not "–Œ " in s:
#        count += 1
#print(count)

#from itertools import *
#count = 0
#for x in permutations("————√√√√"):
#    s = ''.join(x)
#    if '——' not in s and '√√' not in s:
#        count += 1
#print(count)

#from itertools import *
#
#count = 0 
#for x in product("AB123", repeat = 8):
#    s = ''.join(x)
#    s = s.replace('B','A')
#   if s.count('A') == 2:
#        count += 1
#print(count)

#from itertools import *
#
#count = 0
#for x in product("01234", repeat = 6):
#    s = ''.join(x)
#    if s[0] not in '01' and s[-1] not in '34':
#        count += 1
#print(count)

#from itertools import *
#
#count = 0
#for x in permutations('01234567',5):
#    s = ''.join(x)
#    if s[0] != '0' and '1' not in s:
#        s = s.replace('2','0').replace('4','0').replace('6','0').replace('3','1').replace('5','1').replace('7','1')
#        if '00' not in s and '11' not in s:
#            count += 1
#print(count)

#from itertools import *
#
#count = 0
#for x in product("¬»ÿÕﬂ", repeat = 6):
#    s = ''.join(x)
#   if s[0] != 'ÿ' and s[-1] != '»' and s[-1] != 'ﬂ' and s.count('¬') <= 1:
#        count += 1
#print(count)

#from itertools import *
#
#count = 0
#for x in product('ABCD', repeat = 4):
#    s = ''.join(x)
#    s = s.replace('A','1').replace('B','2').replace('C','3').replace('D','4')
#    if s[0] >= s[1] >= s[2] >= s[3]:
#        count += 1
#print(count)

#from itertools import *
#
#count = 0
#for x in product('√≈œ¿–ƒ', repeat = 5):
#    s = ''.join(x)
#    if s.count('√') == 1 and s[0] != '¿' and s[-1] != '≈':
#        count += 1
#print(count)

#from itertools import *
#
#count = 0
#for x in product('0123456789', repeat = 3):
#    s = ''.join(x)
#    if s[0] != '0':
#        if s[0] <= s[1] <= s[2]:
#            count += 1
#print(count)

#from itertools import *
#
#count = 0
#for x in permutations('ƒ≈… —“–¿',6):
#    s = ''.join(x)
#    if s.count('…') == 1:
#        s = s.replace(' ','ƒ').replace('—','ƒ').replace('“','ƒ').replace('–','ƒ')
#        if '…ƒ' in s:
#            count += 1
#print(count)

#from itertools import *
#
#count = 0
#for x in permutations('¬¿…‘”',4):
#    s = ''.join(x)
#    if s[0] != '…' and not '¬‘' in s and not '‘¬' in s:
#        count += 1
#print(count)    

#from itertools import *
#
#count = 0
#for x in set(permutations("Ã»Ã» –»ﬂ")):
#    count += 1
#print(count)
