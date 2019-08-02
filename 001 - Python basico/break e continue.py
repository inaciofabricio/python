# -*- coding: utf-8 -*-

#usando o break
for i in range(10):
    print(i)
    if(i == 5):
        break

print('')
print('')

#usando continue e break
i = 0
while(i<10):
    i += 1
    if(i%2==0):
        continue
    if(i>5):
        break
    print(i)
else:
    print('else')
print('fim')
print('')


