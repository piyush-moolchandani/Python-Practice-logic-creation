'''41.	Reverse string '''
# l='python'
# print(l[::-1])

# l='python'
# new=""
# for i in range(len(l)-1,-1,-1):
#     new=new+l[i]
# print(new)

'''42.	Check palindrome string '''
# l='madam'
# x=l
# if l[::-1]==x:
#     print('pallindrome string')

'''43.	Character frequency count '''
'''44.	Find first repeating character '''
# l='abccddee'
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count+=1
#     if count>1:
#         print(i)
#         break

'''45.	Find first non-repeating character '''
# l='aabbcde'
# for i in l:
#     freq=0
#     for j in l:
#         if i==j:
#             freq+=1
#     if freq==1:
#         print(i)
#         break

'''47.	Reverse elements at prime indexes '''
# x="programming"
# new=""
# for i in range(len(x)):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         new=new+x[i]
# rev=new[::-1]
# x=list(x)
# pos=0
# for i in range(len(x)):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         x[i]=rev[pos]
#         pos+=1
# print("".join(x))

'''48.	Arrange digits inside number (even digits first) '''
# x=123456
# l=str(x)
# even=""
# odd=""
# for i in l:
#     if int(i)%2==0:
#         even+=i
#     else:
#         odd+=i
# print(even+odd)

'''49.	Sum of digits grouping '''
# num = 123456
# l=str(num)
# for i in range(0,len(l),2):
#     if i+1<len(l):
#         sum=int(l[i])+int(l[i+1])
#     else:
#         sum=int(l[i])
#     print(sum)
'''"I convert the number into a string, traverse digits in groups of two, 
sum each pair, and for odd-length numbers I treat the last remaining digit as 
a separate group to avoid index errors."'''

'''Sum of digits grouping odd and even digits'''
# num = 123456
# l=str(num)
# even_sum=0
# odd_sum=0
# for i in l:
#     if int(i)%2==0:
#         even_sum+=int(i)
#     else:
#         odd_sum+=int(i)
# print(even_sum)
# print(odd_sum)

'''50.	Binary 1-count prime replacement Replace by count of 1s'''
# l = [5, 6, 8] 
# l2=[]
# for i in l:
#     ch=bin(i)[2:]
#     bin_count=0
#     for j in ch:
#         if j=="1":
#             bin_count+=1
#     prime=0
#     for k in range(1,bin_count+1):
#         if bin_count%k==0:
#             prime+=1
#     if prime==2:
#         i=bin_count
#     l2.append(i)
# print(l2)


'''51.	Find element with second least frequency '''
# l=[1,2,2,3,3,3,4,4,4,4]
# min_freq=9
# se_min_freq=9
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count+=1
#     if count<min_freq:
#        se_min_freq=min_freq
#        min_freq=count
#     elif count<se_min_freq and count!=min_freq:
#         se_min_freq=count
#         se_element=i
# print(se_element)
# optimized
# l=[1,2,2,3,3,3,4,4,4,4]
# d={}
# for i in l:
#     d[i]=d.get(i,0)+1
# freq=sorted(set(d.values()))
# second_least=freq[1]
# for k,v in d.items():
#     if v==second_least:
#         print(k)
    
'''52.	Find all elements appearing odd number of times '''
# l=[1,2,2,3,3,3,4,4,4,4]
# l2=[]
# for i in l:
#     freq=0
#     for j in l:
#         if i==j:
#             freq+=1
#     if freq%2!=0 and i not in l2:
#         l2.append(i)
# print(l2)

'''53.	Remove first repeating element only '''
# l=[1,2,2,3,3,3,4,4,4,4] 
# for i in l:
#     freq=0
#     for j in l:
#         if i==j:
#             freq+=1
#     if freq>1:
#         l.remove(i)
#         break
# print(l)

'''Remove all occurrences of the first repeating element'''
# l=[1,2,2,3,3,3,4,4,4,4] 
# repeat=None
# for i in l:
#     freq=0
#     for j in l:
#         if i==j:
#             freq+=1
#     if freq>1:
#         repeat=i
#         break
# while repeat in l:
#     l.remove(repeat)
# print(l)

'''54.	Remove last repeating element only '''
# l=[1,2,2,3,3,3,4,4,4,4] 
# for i in range(len(l)-1,-1,-1):
#     freq=0
#     for j in l:
#         if l[i]==j:
#             freq+=1
#     if freq>1:
#         l.remove(l[i])
#         break
# print(l)

'''Remove all occurrences of the last repeating element'''
# l=[1,2,2,3,3,3,4,4,4,4] 
# repeat=None
# for i in range(len(l)-1,-1,-1):
#     freq=0
#     for j in l:
#         if l[i]==j:
#             freq+=1
#     if freq>1:
#         repeat=l[i]
#         break
# while repeat in l:
#     l.remove(repeat)
# print(l)


'''55.	Find first element whose frequency > average frequency '''
# l=[1,2,2,3,3,3,4,4,4,4]
# freq=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count+=1
#     if count not in freq:
#         freq.append(count)
# sum=0
# for i in freq:
#     sum+=i
# avg=sum/len(freq)
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count+=1
#     if count>avg:
#         print(i)
#         break

# optimized
# l=[1,2,2,3,3,3,4,4,4,4]
# d={}
# for i in l:
#     d[i]=d.get(i,0)+1
# total=0
# for v in d.values():
#     total+=v
# avg=total/len(d)
# for k,v in d.items():
#     if v>avg:
#         print(k)
#         break

'''56.	Count distinct repeated elements '''
# l=[1,2,2,3,3,3,4]
# c=0
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count+=1
#     if i not in l2 and count>1:
#         c+=1
#         l2.append(i)
# print(c)


'''57.	Find first element whose frequency is odd and > average '''
# l=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
# l2=[]
# for i in l:
#     freq=0
#     for j in l:
#         if i==j:
#             freq+=1
#     if freq not in l2:
#         l2.append(freq)
# x=sum(l2)
# avg=x/len(l2)
# for i in l:
#     freq=0
#     for j in l:
#         if i==j:
#             freq+=1
#     if freq%2!=0 and freq>avg:
#         print(i)
#         break
    
'''58.	Arrange array according to frequency '''
'''59.	Find majority element (> n/2) '''
# l=[2,2,1,2,3,2,2]
# n=len(l)
# half=n/2
# for i in l:
#     freq=0
#     for j in l:
#         if i==j:
#             freq+=1
#     if freq>half:
#         print(i)
#         break

'''66.	Group numbers by digit count '''
# l=[10,2,345,78,9999,100]
# d={}
# for i in l:
#     x=i
#     count=0
#     while x>0:
#         count+=1
#         x=x//10
#     if count not in d:
#         d[count]=[]
#     d[count].append(i)
# print(d)
'''"I traverse each number and count its digits by repeatedly dividing it by 10. 
The digit count becomes the dictionary key. If that key doesn't exist, 
I create an empty list for it. Then I append the original number to that list.
 Finally, all numbers having the same number of digits are grouped together."'''

'''67.	Group numbers by digit sum '''
# l=[14,25,33,42,51,60,111]
# d={}
# for i in l:
#     x=i
#     sum=0
#     while x>0:
#         digit=x%10
#         sum+=digit
#         x=x//10
#     if sum not in d:
#         d[sum]=[]
#     d[sum].append(i)
# print(d,end=' ')

'''68.	Find all pairs having same digit sum '''
# l=[10,12,21,30,15,24,42]
# d={}
# for i in l:
#     sum=0
#     for j in str(i):
#         sum+=int(j)
#     if sum not in d:
#         d[sum]=[]
#     d[sum].append(i)
# for num in d.values():
#     for i in range(len(num)):
#         for j in range(i+1,len(num)):
#             print((num[i],num[j]))
'''"First I calculate the digit sum of every number and group numbers having the same digit sum 
using a dictionary. After grouping, I traverse each group separately and generate all possible 
pairs using nested loops."'''


'''60.	Find element occurring odd number of times '''
# l=[1,2,2,3,3,3,4,4,4,4]
# l2=[]
# for i in l:
#     freq=0
#     for j in l:
#         if i==j:
#             freq+=1
#     if freq%2!=0 and i not in l2:
#         print(i)
#         l2.append(i)

'''61.	Rearrange array so duplicates come together '''
# l=[3,1,2,3,2,1]
# ans=[]
# seen=[]
# for i in l:
#     if i not in seen:
#         count=0
#         for j in l:
#             if i==j:
#                 count+=1
#         for k in range(count):
#             ans.append(i)
#         seen.append(i)
# print(ans)
'''"Main ek seen list maintain karta hoon taaki kisi element ko baar-baar process na karna pade. 
Har unique element ke liye main poori list scan karke uski frequency count karta hoon. 
Phir us frequency ke hisaab se us element ko answer list me consecutive times add karta hoon. 
Isse saare duplicate elements ek saath aa jaate hain."'''

'''62.	Rearrange array so no adjacent elements are equal '''

'''73.	Reverse subarray having maximum sum '''
# l=[1,2,3,-5,4]
# max_sum=0
# for i in range(len(l)):    
#     for j in range(i,len(l)):
#         sub=l[i:j+1]
#         sum=0
#         for k in sub:
#             sum+=k
#         if sum>max_sum:
#             max_sum=sum
#             x=sub
#             start=i
#             end=j
# rev=x[::-1]
# l[start:end+1]=rev
# print(l)
'''"I generate all possible subarrays using two nested loops. 
For each subarray, I calculate its sum and keep track of the 
maximum sum along with its starting and ending indexes. Once 
I find the maximum-sum subarray, I reverse it and replace only 
that portion of the original array using slice assignment. 
This gives the required output."'''

        
        

        
   
        


  


        



        



    
        





        