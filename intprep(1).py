# Radha
'''1.	Reverse a list '''
'''Time Complexity?
Loop runs n times.Each append() is O(1).
Total:O(n)
Space Complexity?You created a new list l2.
Extra space:O(n)'''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in range(len(l)-1,-1,-1):                               
#     l2.append(l[i])
# print(l2)
'''2.	Rotate list left by 1 '''
'''Why save first element?Without:fi=l[0]
After first operation:l[0]=l[1]the value 1 is permanently lost.
Time ComplexityLoop runs:n-1 times So:O(n)
Space ComplexityOnly one extra variable:fi So:O(1)'''
# l=[1,2,3,4,5]
# fi=l[0]
# for i in range(len(l)-1):
#     l[i]=l[i+1]
# l[-1]=fi
# print(l)
'''optimized'''
# l=[1,2,3,4,5]
# l=l[1:]+l[:1]
# print(l)
'''3.	Rotate list right by 1 '''
# l=[1,2,3,4,5]
# lv=l[-1]
# for i in range(len(l)-1,0,-1):
#     l[i]=l[i-1]
# l[0]=lv
# print(l)
'''optimized'''
# l=[1,2,3,4,5]
# l=l[-1:]+l[:-1]
# print(l)
'''4.	Rotate list left by k positions '''
# l=[1,2,3,4,5]
# k=2
# for i in range(k):
#     fi=l[0]
#     for j in range(len(l)-1):
#         l[j]=l[j+1]
#     l[-1]=fi
# print(l)
'''optimized solution'''
# l=[1,2,3,4,5]
# k=2
# k=k%len(l)
# l=l[k:]+l[:k]
# print(l)
'''5.	Rotate list right by k positions '''
'''optimized solution'''
# l=[1,2,3,4,5]
# k=2
# k=k%len(l)
# l=l[-k:]+l[:-k]
# print(l)

'''6.	Move all zeros to end '''
# l=[1,0,2,0,3,4,0]
# l2=[]
# l3=[]
# for i in l:
#     if i!=0:
#         l2.append(i)
# for i in l:
#     if i==0:
#         l3.append(i)
# print(l2+l3)
'''Interview mein kya bolna hai?
"Main non-zero elements ko front mein maintain kar raha hoon using a pointer pos.
 Jab bhi non-zero milta hai, usko pos index par swap kar deta hoon aur pos ko aage 
 badha deta hoon. Isse saare non-zero elements front mein aa jate hain aur zeros 
 automatically end mein chale jate hain."'''
# l=[1,0,2,0,3,4,0]
# pos=0
# for i in range(len(l)):
#     if l[i]!=0:
#         l[pos],l[i]=l[i],l[pos]
#         pos+=1
# print(l)
'''Agar interviewer pooche "Can you optimize it?"
Tum confidently bol sakte ho:
"This solution already runs in O(n) time and O(1) extra space, so it is optimal for this problem."
Aur ye statement bilkul sahi hoga.
Service-based company interview mein agar tum ye solution likh do aur explain kar do, to main 
ise expected se better answer maanunga. 👍'''

'''7.	Separate even and odd numbers '''
# l=[1,2,3,4,5,6,7,8,9]
# pos=0
# for i in range(len(l)):
#     if l[i]%2==0:
#         l[pos],l[i]=l[i],l[pos]
#         pos+=1
# print(l)
'''Logic explain karo.
Bolna:
"I maintain a pointer pos which represents the next position where an even number should be placed. 
I scan the array using i. Whenever I find an even number, I swap it with the element at pos and 
increment pos. This ensures all even numbers are grouped at the beginning in O(n) time and O(1) 
extra space."'''

'''8.Sort list without using sort (ascending) '''
# l=[4,2,7,1,5]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             x=l[i]
#             l[i]=l[j]
#             l[j]=x
# print(l)
'''Interview Explanation
Agar interviewer bole:
Explain the logic.
Bolna:
"For each position i, I compare it with all elements after it using j. 
If I find a smaller element, I swap it. After every outer loop iteration, 
the smallest element among the remaining unsorted part gets placed at its 
correct position.
---------------------------------------------------------------------------
Important Observation
Ye exact Selection Sort nahi hai.
Selection Sort normally:
Minimum index find karta hai.
End mein ek hi swap karta hai.
Tumhara version:
Chhota milte hi swap karta rehta hai.
Interview mein isse generally Selection Sort style sorting ya basic nested-loop 
sorting maan lenge, especially service-based companies mein.
Ye question tab truly click karta hai jab tum list ko har iteration ke baad paper
par draw karte ho. Tumne jo confusion bataya hai, wo usually i aur j ke roles
clear na hone ki wajah se hota hai. Once you remember:
i = jis position ko fix karna hai
j = uske aage search karna hai
to poora algorithm samajh aa jata hai. 🚀"'''

'''Sort list without using sort (descending)'''
# l=[4,2,7,1,5]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]<l[j]:
#             x=l[i]
#             l[i]=l[j]
#             l[j]=x
# print(l)
'''Ascending mein bada left mein nahi hona chahiye, isliye > par swap.
Descending mein chhota left mein nahi hona chahiye, isliye < par swap.'''


'''10.	Merge two lists '''
# l1=[1,2,3]
# l2=[4,5,6]
# print(l1+l2)
'''"+ operator performs list concatenation. It creates a new list and copies
 all elements of the first list followed by all elements of the second list."'''
# l1=[1,2,3]
# l2=[4,5,6]
# for i in l2:
#     l1.append(i)
# print(l1)
'''extend()
l1.extend(l2)Modifies:Existing List No new merged list variable needed.'''
# l1=[1,2,3]
# l2=[4,5,6]
# l1.extend(l2)
# print(l1)

'''11.	Find pair with given sum '''
# l=[1,2,3,4,5]
# sum=9
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==sum:
#             print((l[i],l[j]))

'''12.	Find all pairs with sum = k '''
# l=[1,2,3,4,5]
# k=5
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==k:
#             print((l[i],l[j]))

'''13.	Find maximum difference between elements '''
# l=[7,2,9,1]
# max_diff=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if j>i:
#            diff=l[j]-l[i]
#            if diff>max_diff:
#                max_diff=diff
# print(max_diff)

'''14.	Find longest increasing sequence '''
# l=[1,2,3,1,2,3,4,0]
# current=1
# maximum=1
# for i in range(1,len(l)):
#         if l[i]>l[i-1]:
#             current+=1
#         else:
#               maximum=max(maximum,current)
#               current=1
# maximum=max(maximum,current)
# print(maximum)
'''"I traverse the array once. If the current element is greater than the previous element, 
the increasing sequence continues and I increase the current count. Otherwise the sequence breaks,
so I update the maximum length and reset the current count."'''

'''15.	Replace element with next greater element '''
# l=[4,5,2,10]
# res=[]
# for i in range(len(l)):
#     found=-1
#     for j in range(i+1,len(l)):
#         if l[j]>l[i]:
#             found=l[j]
#             break
#     res.append(found)
# print(res)

'''16.	Replace element with previous smaller element '''
'''Ek Golden Formula Yaad Rakho
Question   ->     Direction
Next Greater  ->	Right (i+1 → end)
Next Smaller  ->	Right (i+1 → end)
Previous Greater  ->	Left (i-1 → 0)(i-1,-1,-1)
Previous Smaller  ->	Left (i-1 → 0)
Aur condition badlegi:
Question	Condition
Greater	>
Smaller	<'''
# l=[4,5,2,10]
# res=[]
# for i in range(len(l)):
#     found=-1
#     for j in range(i-1,-1,-1):
#         if l[j]<l[i]:
#             found=l[j]
#             break
#     res.append(found)
# print(res)
         
'''17.	Find equilibrium index '''
# l=[1,3,5,2,2]
# for i in range(len(l)):
#     left=0
#     right=0
#     for j in range(0,i):
#         left=left+l[j]
#     for k in range(i+1,len(l)):
#         right=right+l[k]
#     if left==right:
#         print(i)
'''"For every index, I calculate the sum of all elements on its left side 
and the sum of all elements on its right side. If both sums become equal, 
that index is an equilibrium index."'''

'''18.	Swap first and last element '''
# l=[1,2,3,4]
# l[0],l[-1]=l[-1],l[0]
# print(l)
'''"Python supports multiple assignment. 
The values on the right side are evaluated first, 
then assigned simultaneously to the variables on the left side, 
allowing us to swap values without using a temporary variable."'''

'''19.	Swap largest and smallest element '''
# l=[4,5,1,8,9,4]
# max_element=l[0]
# min_element=l[0]
# large_index=0
# small_index=0
# for i in range(len(l)):
#     if l[i] > max_element:
#         max_element=l[i]
#         large_index=i
#     if l[i] < min_element:
#         min_element=l[i]
#         small_index=i
# l[large_index],l[small_index]=l[small_index],l[large_index]
# print(l)
'''"I scan the array once to find the indices of the maximum and minimum elements, 
then I swap those two positions. 
This takes O(n) time and O(1) extra space.

"Main array ko ek baar traverse karta hoon. Ek variable mein ab tak ka largest element aur 
uska index store karta hoon. Dusre variable mein ab tak ka smallest element aur uska index 
store karta hoon. Jab bhi koi bada element milta hai to largest update kar deta hoon, aur 
jab bhi koi chhota element milta hai to smallest update kar deta hoon. Loop ke end mein mere 
paas largest aur smallest dono ke indexes hote hain. Fir un dono positions ko swap kar deta hoon.""'''

'''20.	Zigzag arrange (> < > < big to small) '''
# l=[4,3,7,8,6,2,1]
# for i in range(len(l)-1):
#     if i%2==0:
#         if l[i]<l[i+1]:
#             l[i],l[i+1]=l[i+1],l[i]
#     else:
#         if l[i]>l[i+1]:
#             l[i],l[i+1]=l[i+1],l[i]
# print(l)

'''"I traverse the array once. For every even index, 
I ensure the current element is greater than the next element. 
For every odd index, I ensure the current element is smaller than 
the next element. If the condition is violated, I swap the adjacent elements. 
This creates the zigzag pattern in a single pass."'''

'''23.	Find pair whose sum is closest to k '''
# l=[1,4,7,10]
# k=15
# min_sum=999
# for i in  range(len(l)):
#     for j in range(i+1,len(l)):
#         sum=l[i]+l[j]
#         diff=abs(sum-k)
#         if diff<min_sum:
#             min_sum=diff
#             x=l[i]
#             y=l[j]
# print(x,y)


'''24.	Find pair whose product is minimum '''
# l=[5,7,2,9]
# min_pair=999
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         prod=l[i]*l[j]
#         if prod<min_pair:
#             min_pair=prod
#             x=l[i]
#             y=l[j]
# print((x,y))

'''25.	Count pairs with both numbers prime '''
# l=[2,3,4,5,6]
# count=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         x=l[i]
#         y=l[j]
#         c=0
#         for k in range(1,x+1):
#             if x%k==0:
#                 c+=1
#         c2=0
#         for m in range(1,y+1):
#             if y%m==0:
#                 c2+=1
#         if c==2 and c2==2:
#             count+=1
# print(count)

# optimized version
# l=[2,3,4,5,6]
# prime=[]
# for num in l:
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     if count==2:
#         prime.append(num)
# n=len(prime)
# count=n*(n-1)//2
# print(count)
'''"Instead of checking every pair and testing primality repeatedly, 
I first count how many prime numbers are present in the array. 
If there are n prime numbers, then the number of pairs where 
both numbers are prime is nC2 = n(n−1)/2."'''

'''26.	Find pair with same last digit '''
# l=[17,27,38,49]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         x=l[i]
#         y=l[j]
#         if x%10==y%10:
#             print((x,y))
'''"I generate all unique pairs using nested loops. For each pair, 
I compare their last digits using the modulo operator %10. If both last digits are equal, 
I print the pair."'''
# optimized
# l=[17,27,38,49]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]%10 == l[j]%10:
#             print((l[i],l[j]))

'''27.	Count pairs where one is square of another '''
# l=[2,4,3,9]
# count=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#          if l[i]**2 == l[j] or l[j]**2 == l[i]:
#             count+=1
# print(count)
'''"For every unique pair, I check both possibilities: 
whether the first number is the square of the second or the second number 
is the square of the first. If either condition is true, I count that pair."'''

'''21.	Sort only even elements '''
# l=[8,3,6,1,4,7,2]
# l2=[]
# for i in l:
#     if i%2==0:
#         l2.append(i)
# for i in range(len(l2)):
#     for j in range(i+1,len(l2)):
#         if l2[i]>l2[j]:
#             x=l2[i]
#             l2[i]=l2[j]
#             l2[j]=x
# pos=0
# for i in range(len(l)):
#     if l[i]%2==0:
#         l[i]=l2[pos]
#         pos+=1
# print(l)
"First I extract all even numbers and sort them. "
"Then I traverse the original array again."
" Whenever I encounter an even number,"
" I replace it with the next element from the sorted even list,"
" while keeping odd numbers unchanged."


        



      
         



      




