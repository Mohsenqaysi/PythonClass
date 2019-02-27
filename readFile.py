import os
x_file = '/home/ubuntu/workspace/filename.txt'
lines = tuple(open(x_file, 'r'))

for line in lines:
    print(line, end='')
    

print('\n---------------')
newArray = []
for line in lines:
    if line == '\n':
        print('new line was removed...\n',end='')
        line.strip()
    else:
        newArray.append(line)
        print(line, end='')
print('\n---------------')
      
print('\n\n\nnew array: \n {}'.format(newArray))
print('\n---------------')

for line in newArray:
    print(line, end ='')
