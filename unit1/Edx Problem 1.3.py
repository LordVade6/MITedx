s = 'azcbobobegghaklabcd'
n = 0
a=[]

for letter in s:
    if str(s[n:n+1]) < str(s[n+1:n+2]):
        a.append(len(s[n:n+2]))
        print(s[n:n+2])
        
        if str(s[n+1:n+2]) < str(s[n+2:n+3]):
            
            a.append((str(s[n:n+3])))
            
            if str(s[n+2:n+3]) < str(s[n+3:n+4]):
                 print(str(s[n:n+4]))
                 a.append(4)
                 
    n+=1


a.index.max
        

#while n < len(s):
    #print(str(s[n:n+2]))
    #n=n+1
    #if str(s[n:n+1]) < str(s[n+1:n+2]):
        #a.append(n+2)

#print(a)


#for letter in s:  
 #   if str(s[n:n+1]) < str(s[n+1:n+2]):
  #      a=2
   #     print(str(s[n:n+2]))
    #    
     #   if str(s[n+1:n+2]) < str(s[n+2:n+3]):
      #      a+=1
       #     print(a)
        #    print(str(s[n:n+3]))
#
 #           if str(s[n+2:n+3]) < str(s[n+3:n+4]):
  #              a+=1
   #             print(a)
    #            print(str(s[n:n+4]))
    #n+=1

#print(a)


print('Longest substring in alphabetical order is: ')


