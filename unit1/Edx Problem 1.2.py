s = 'azcbobobegghakl'
count = 0
N = 0

for letter in s:
    if letter == 'b':
        if s[count:count+3]=='bob':
            N+=1
        
    count+=1

print('Number of times bob occurs is: '+str(N))



