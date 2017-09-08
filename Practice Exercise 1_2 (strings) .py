#Practice Exercise 1_2 (strings)

string = 'Supercalifragilisticexpialidocious'
string_2= 'Antidisestablishmentarianism'
string_3= 'Honorificabilitudinitatibus'
lst = ['Berloiz', 'Borodin', 'Brain', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein' ]

count = len(string)
print(count)

Exist_in = 'ice' in string
print(Exist_in)

longerthan = string_2 > string_3
print(longerthan)

lst.sort()
first=lst[0]
last=lst[-1]

print (first,last)