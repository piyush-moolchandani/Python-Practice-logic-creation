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


'''63.	Keep only values appearing exactly twice '''
# l=[1,2,2,3,3,3,4,4]
# l2=[]
# for i in l:
#     freq=0
#     for j in l:
#         if i==j:
#             freq+=1
#     if freq==2:
#         l2.append(i)
# print(l2)
        

# '''64.	Remove first duplicate occurrence '''
# l=[1,2,2,3,3,3]
# for i in l:
#     freq=0
#     for j in l:
#         if i==j:
#             freq+=1
#     if freq>1:
#         l.remove(i)
#         break
# print(l)

'''71.	Longest consecutive increasing subarray '''
# l=[5,6,7,1,2,3,4]
# max_len=0
# for i in range(len(l)):
#     sub=[]
#     sub.append(l[i])
#     for j in range(i+1,len(l)):
#         if l[j]>l[j-1]:
#             sub.append(l[j])
#         else:
#             break
#     if len(sub)>max_len:
#         max_len=len(sub)
#         ans=sub
# print(ans)        
'''"Main har index ko starting point maanta hoon aur usse ek increasing subarray banana start karta hoon. 
Jab tak current element previous element se bada hota hai, main usse subarray me add karta rehta hoon. 
Jaisi hi condition fail hoti hai, main us subarray ki length ko maximum length se compare karta hoon. 
Agar wo badi hoti hai to answer update kar deta hoon. Aakhir me mere paas longest consecutive increasing 
subarray hoti hai."'''

'''72.	Longest consecutive decreasing subarray '''
# l=[20,15,10,8,12,9,5]
# max_len=0
# for i in range(len(l)):
#     sub=[]
#     sub.append(l[i])
#     for j in range(i+1,len(l)):
#         if l[j]<l[j-1]:
#             sub.append(l[j])
#         else:
#             break
#     if len(sub)>max_len:
#         max_len=len(sub)
#         ans=sub
# print(ans)

'''74.	Rotate subarray having maximum sum '''
# l=[1,2,3,-5,4]
# max_sum=0
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         sub=l[i:j+1]
#         sum=0
#         for k in sub:
#             sum+=k
#             if sum>max_sum:
#                 max_sum=sum
#                 ans=sub
#                 start=i
#                 end=j
# ans=ans[1:]+ans[:1]
# l[start:end+1]=ans
# print(l)

'''76.	Reverse every subarray whose sum is prime '''
# l=[1,3,2,4]
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         sub=l[i:j+1]
#         sum=0
#         for k in sub:
#             sum+=k
#         count=0
#         for m in range(1,sum+1):
#             if sum%m==0:
#                 count+=1
#         if count==2:
#             rev=sub[::-1]
#             print(rev)


'''36.	Arrange positives first, negatives later '''
# l=[1,-2,3,-4,5,-6]
# res1=list(filter(lambda x:x>0,l))
# res2=list(filter(lambda x:x<0,l))
# print(res1+res2)

'''75.	Longest mountain subarray '''
# l=[1,3,5,4,2,6]
# max_len=0
# for i in range(len(l)):
#     sub=[l[i]]
#     inc=False
#     dec=False
#     for j in range(i+1,len(l)):
#         if l[j]>l[j-1] and dec==False:
#             sub.append(l[j])
#             inc=True
#         elif l[j]<l[j-1] and inc==True:
#             sub.append(l[j])
#             dec=True
#         else:
#             break
#     if inc==True and dec==True:
#         if len(sub)>max_len:
#             max_len=len(sub)
#             ans=sub
# print(ans)
'''"Main har index ko mountain ka starting point maanta hoon. 
Do boolean flags (inc aur dec) maintain karta hoon. 
Jab tak elements increasing hote hain, increasing part build karta hoon. 
Jaise hi decreasing start hoti hai, decreasing part build karta hoon. 
Agar decreasing ke baad fir increasing aa jaye, mountain invalid ho jati hai aur loop break kar deta hoon. 
Jis valid mountain ki length sabse badi hoti hai, use answer bana deta hoon."'''

'''Jab tak neeche utarna start nahi hua hai (dec=False), tab tak hi increasing allow hai. 
Ek baar decreasing start ho gayi (dec=True), uske baad increasing bilkul allow nahi hai.
Interview me agar interviewer puche:
Why did you use dec == False?
Tum confidently bol sakte ho:
"I used dec == False to ensure that increasing is allowed only before the decreasing phase starts. 
Once the subarray starts decreasing (dec=True), any new increasing element would mean the mountain
has ended, because a valid mountain can have only one peak."'''


'''77.	Partition array into maximum increasing chunks '''
# l=[1,2,3,2,4,5]
# sub=[l[0]]
# for i in range(1,len(l)):
#     if l[i]>l[i-1]:
#         sub.append(l[i])
#     else:
#         print(sub)
#         sub=[l[i]]
# print(sub)
'''"Main pehle element se first increasing chunk start karta hoon. 
Har next element ko previous element se compare karta hoon. 
Agar current element bada hai to usse current chunk me add kar deta hoon. 
Agar increasing order toot jata hai, to current chunk complete ho jata hai, 
use print/store kar deta hoon aur current element se naya chunk start kar deta hoon.
 Loop ke end me last chunk ko bhi print kar deta hoon."'''
# logical explanation 2
'''"I start the first chunk with the first element. Then I scan the array from left to right.
If the current element is greater than the previous element, I append it to the current increasing chunk.
If the increasing order breaks, I output/store the current chunk and start a new chunk from the current element. 
After the loop finishes, I print the last chunk because it would not have been printed 
inside the loop if the array ended while still increasing."'''


'''78.	Rotate longest increasing subarray '''
# l=[5,1,2,3,4,0]
# max_array=0
# for i in range(len(l)):
#     sub=[l[i]]
#     for j in range(i+1,len(l)):
#         if l[j]>l[j-1]:
#             sub.append(l[j])
#         else:
#             break
#     if len(sub)>max_array:
#         max_array=len(sub)
#         ans=sub
#         start=i
#         end=i+len(sub)-1
# ans=ans[-1:]+ans[:-1]
# l[start:end+1]=ans
# print(l)
'''Tum bol sakte ho:
"j break hone ke baad invalid comparison wale index par hota hai.
Isliye main end = i + len(sub) - 1 use karta hoon, kyunki sub me sirf 
valid increasing elements hi store hote hain."'''

'''"I first find the longest increasing subarray by checking every possible 
starting index and extending it while the elements remain in increasing order. 
Whenever I find a longer increasing subarray, I store that subarray along with 
its start and end indexes. After identifying the longest increasing subarray, 
I perform a right rotation on it and replace only that portion back into the 
original array using slice assignment. This keeps the rest of the array unchanged."'''
# unoptimized approach for this ques
# l=[5,1,2,3,4,0]
# max_array=0
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         sub=l[i:j+1]
#         inc=True
#         for k in range(1,len(sub)):
#             if sub[k]<=sub[k-1]:
#                 inc=False
#                 break
#         if inc==True:
#             if len(sub)>max_array:
#                 max_array=len(sub)
#                 ans=sub
#                 start=i
#                 end=j
# print(ans)

'''79.	Find subarray with sum closest to zero '''
# l=[6,-5,2]
# min_sum=999
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         sub=l[i:j+1]
#         sum=0
#         for k in sub:
#             sum+=k
#         if abs(sum)<min_sum:
#             min_sum=abs(sum)
#             ans=sub
# print(ans)
'''"The question asks for the subarray whose sum is closest to zero, not the smallest sum. 
A negative sum like -5 is actually farther from zero than 1. Therefore, I compare abs(sum) 
because it gives the distance from zero irrespective of whether the sum is positive or negative."'''

'''80.	Find longest subarray with equal even and odd elements '''
# l=[1,2,4,3,5]
# max_array=0
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         sub=l[i:j+1]
#         even_count=0
#         odd_count=0
#         for k in sub:
#             if k%2==0:
#                 even_count+=1
#             else:
#                 odd_count+=1
#         if even_count==odd_count and len(sub)>=max_array:
#             max_array=len(sub)
#             ans=sub
# print(ans)
'''"I generate all possible subarrays using two nested loops. 
For each subarray, I count the number of even and odd elements. 
If both counts are equal, it is a valid subarray. 
Among all valid subarrays, I keep the one with the maximum length as the answer."'''
# Rule to remember
# > → First maximum ko preserve karta hai.
# >= → Last maximum ko preserve karta hai. ✅

'''81.	Find subarray where first and last element are equal '''
# l=[2,3,2,5]
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         sub=l[i:j+1]
#         if sub[0]==sub[-1]:
#             print(sub)

'''82.	Find maximum product subarray and reverse it '''
# l=[2,3,-2,4]
# max_prod=0
# for i in range(len(l)):
#     for j in range(i,len(l)):
#         sub=l[i:j+1]
#         prod=1
#         for k in sub:
#             prod*=k
#         if prod>max_prod:
#             max_prod=prod
#             ans=sub
#             start=i
#             end=j
# rev=ans[::-1]
# l[start:end+1]=rev
# print(l)

'''83.	Find longest consecutive sequence '''
# l=[100,4,200,1,3,2]
# max_len=0
# for i in l:
#     seq=[i]
#     num=i
#     while num+1 in l:
#         seq.append(num+1)
#         num+=1
#     if len(seq)>max_len:
#         max_len=len(seq)
#         ans=seq
# print(ans)

'''84.	Longest alternating even-odd subarray '''

   

    
    




        
        

    


       

        



        
   
        


  


        



        



    
        





        