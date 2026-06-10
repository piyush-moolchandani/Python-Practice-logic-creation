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

''''''


