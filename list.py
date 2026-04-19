'''1.	Find largest element '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# max=l[0]
# for i in l:
#     if i>max:
#         max=i
# print(max)

'''3.	Find second largest '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# large=0
# second_largest=0
# for i in l:
#     if i>large:
#        second_largest=large
#        large=i
#     elif i>second_largest and i!=large:
#         second_largest=i
# print(second_largest)
    

'''4.	Find second smallest '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# small=l[0]
# second_small=l[0]
# for i in l:
#     if i<small:
#         second_small=small
#         small=i
#     elif i<second_small and i!=small:
#         second_small=i
# print(second_small)

'''6.	Count even numbers '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# count=0
# for i in l:
#     if i%2==0:
#         count=count+1
# print(count)
   
'''8.	Find average of list '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# div=len(l)
# sum=0
# for i in l:
#     sum=sum+i
# avg=sum/div
# print(avg)

'''9.	Print elements greater than average '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# div=len(l)
# sum=0
# for i in l:
#     sum=sum+i
# avg=sum/div
# for j in l:
#     if j>avg:
#         print(j)

'''11.	Print all even numbers '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# for i in l:
#     if i%2==0:
#         print(i)

'''13.	Remove all even numbers '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# for i in l:
#     if i%2!=0:
#         l2.append(i)
# print(l2)

'''15.	Replace even numbers with 0 '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# for i in l:
#     if i%2==0:
#         i=0
#     l2.append(i)
# print(l2)

'''17.	Keep only numbers divisible by 3 '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# for i in l:
#     if i%3==0:
#         l2.append(i)
# print(l2)

'''18.	Remove numbers divisible by 5 '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# for i in l:
#     if i%5!=0:
#         l2.append(i)
# print(l2)
        
'''19.	Replace negative numbers with 0 '''
# l=[4,5,-6,3,-5,6,-43,35,-65,32,-4]
# l2=[]
# for i in l:
#     if i<0:
#         i=0
#     l2.append(i)
# print(l2)


'''20.	Count numbers greater than 10 '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# count=0
# for i in l:
#     if i>10:
#         count=count+1
# print(count)

'''21.	Replace each element with its square '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# for i in l:
#     l2.append(i**2)
# print(l2)

'''23.	Replace even numbers with their square '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# for i in l:
#     if i%2==0:
#         sq=i**2
#     else:
#         sq=i
#     l2.append(sq)
# print(l2)    

'''25.	Replace numbers > 10 with 100 '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# for i in l:
#     if i>10:
#         i=100
#     l2.append(i)
# print(l2)

'''26.	Replace numbers < 5 with -1 '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# for i in l:
#     if i<5:
#         i=i-1
#     l2.append(i)
# print(l2)
  
'''27.	Replace each element with difference from max '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# max=l[0]
# for i in l:
#     if i>max:
#         max=i
# for j in l:
#     j=j-max
#     l2.append(abs(j))
# print(l2)

'''reverse of a list'''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# for i in range(len(l)-1,-1,-1):
#     l2.append(l[i])
# print(l2)

'''29.	Replace each element with sum of all elements '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# l2=[]
# sum=0
# for i in l:
#     sum=sum+i
# for j in l:
#     j=sum
#     l2.append(j)
# print(l2)

'''31.	Count frequency of each element '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# for i in l:
#     count=0
#     for j in l:
#       if i==j:
#         count=count+1
#     print(i,"==",count)

'''32.	Find most frequent element '''
# l=[4,5,6,3,5,6,43,35,65,32,4]
# max_count = 0
# most = 0
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count>max_count:
#         max_count=count
#         most=i
# print("Most frequent element =", most)
# print("Frequency =", max_count)

"Find Least Frequency "
# l=[4,5,6,3,5,6,43,35,65,32,4]
# min=l[0]
# minimun=0
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count<min:
#         min=count
#         minimun=i
# print("Most frequent element =", minimun)
# print("Frequency =", min)


'''34.	Count elements appearing more than once '''
# l=[4,5,6,3,5,6,43,35,65,32,4,4]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
# if count>1:
#     print(count)

'''35.	Print duplicate elements '''
# l=[4,5,6,3,5,6,43,35,65,32,4,4]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count>1:
#         l2.append(i)
# print(l2)

'''36.	Remove duplicates '''
# l=[4,5,6,3,5,6,43,35,65,32,4,4]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count==1:
#         l2.append(i)
# print(l2)

'''37.	Count unique elements '''
# l=[4,5,6,3,5,6,43,35,65,32,4,4]
# count2=0
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count==1:
#         count2=count2+1
# print(count2)

'''38.	Replace duplicates with 0 '''
# l=[4,5,6,3,5,6,43,35,65,32,4,4]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count>1:
#         i=0
#     l2.append(i)
# print(l2)

'''39.	Find first non-repeating element '''
# l=[4,5,6,3,5,6,43,35,65,32,4,4]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count==1:
#          print("First non-repeating element =", i)
#          break

'''40.	Find second most frequent element '''
# l = [4,5,6,3,5,6,43,35,65,32,4,4]
# max1 = 0
# max2 = 0
# first = 0
# second = 0
# done = []
# for i in l:
#     if i not in done:
#         count = 0
#         for j in l:
#             if i == j:
#                 count = count + 1
#         if count > max1:
#             max2 = max1
#             second = first
#             max1 = count
#             first = i
#         elif count > max2:
#             max2 = count
#             second = i
#         done.append(i)
# print("Second most frequent =", second)

'''42.	Rotate list left by 1 '''
# l=[10,20,30,40]
# fi=l[0]
# for i in range(len(l)-1):
#     l[i]=l[i+1]
# l[-1]=fi
# print(l)

'''43.	Rotate list right by 1 '''
# l=[10,20,30,40]
# lv=l[-1]
# for i in range(len(l)-1,0,-1):
#     l[i]=l[i-1]
# l[0]=lv
# print(l)

'''44.	Rotate list by k positions '''
# l=[1,2,3,4,5]
# k=2
# for j in range(2):
#     lv=l[-1]
#     for i in range(len(l)-1,0,-1):
#         l[i]=l[i-1]
#     l[0]=lv
# print(l)

'''Rotate list by k 7 '''
# l=[1,2,3,4,5]
# k=7
# k=k%len(l)
# for j in range(k):
#     lv=l[-1]
#     for i in range(len(l)-1,0,-1):
#         l[i]=l[i-1]
#     l[0]=lv
# print(l)

'''Left rotate by k'''
# l=[1,2,3,4,5]
# k=2
# for j in range(k):
#     fi=l[0]
#     for i in range(len(l)-1):
#         l[i]=l[i+1]
#     l[-1]=fi
# print(l)

'''Left rotate by k3 '''
# l=[1,2,3,4,5,6,7,8]
# k=3
# for j in range(k):
#     fi=l[0]
#     for i in range(len(l)-1):
#         l[i]=l[i+1]
#     l[-1]=fi
# print(l)

'''right rotate by k3 '''
# l=[1,2,3,4,5,6,7,8]
# k=3
# for i in range (k):
#     lv=l[-1]
#     for i in range(len(l)-1,0,-1):
#         l[i]=l[i-1]
#     l[0]=lv
# print(l)

'''45.	Move all zeros to end '''
# l=[1,0,2,0,3,0,4,0,5,0]
# l2=[]
# l3=[]
# for i in l:
#     if i!=0:
#         l2.append(i)
# for i in l:
#     if i==0:
#         l3.append(i)
# print(l2+l3)

'''46.	Move all zeros to front '''
# l=[1,0,2,0,3,0,4,0,5,0]
# l2=[]
# l3=[]
# for i in l:
#     if i==0:
#         l2.append(i)
# for i in l:
#     if i!=0:
#         l3.append(i)
# print(l2+l3)

'''48.	Sort list (without using sort) '''
'''🔹 Ascending Order (small to big)'''
# l=[4,2,7,1,5]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             x=l[i]
#             l[i]=l[j]
#             l[j]=x
# print(l)

'''🔹 descending Order (big to small)'''
# l=[4,2,7,1,5]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]<l[j]:
#             x=l[i]
#             l[i]=l[j]
#             l[j]=x
# print(l)


'''49.	Merge two lists '''
# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10]
# for i in l2:
#     l1.append(i)
# print(l1)

'''50.	Find intersection of two lists '''
# l1=[1,2,3,4]
# l2=[3,4,5,6]
# l3=[5,6,7,8]
# l4=[]
# for i in l1:
#     if i in l2:
#         l4.append(i)
# for i in l2:
#     if i in l3:
#         l4.append(i)
# print(list(l4))

  
'''51.	Check if list is palindrome '''
# l=[1,2,1]
# l2=[]
# for i in range(len(l)-1,-1,-1):
#     l2.append(l[i])
# if l==l2:
#     print("the list is pallindrome")
# else:
#     print("the list is not pallindrome")

'''52.	Find pair with given sum target = 100'''
# l=[20,30,50,70]
# t=100
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==t:
#             print(l[i],l[j])
#             break

'''53.	Find all pairs with sum = k '''
# l = [1,2,3,4,5]
# k = 5
# for i in range(len(l)):
#     for j in range(i+1, len(l)):
#         if l[i] + l[j] == k:
#             print(l[i], l[j])

'''54.	Find maximum difference between elements '''
# l = [1,2,3,4,5]
# max=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#        dif = abs(l[i]-l[j])
#        if dif>max:
#            max=dif
# print(max)            excellent work

'''55.	Find minimum difference '''
# l=[5,3,8,4]
# min=9
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         dif=abs(l[i]-l[j])
#         if dif<min:
#             min=dif
# print(min)
        
''''Find all pairs with sum k  '''
# l=[3,5,7,9,3]
# k=12
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==k:
#             print(l[i],l[j])

'''find maximum difference '''
# l=[3,5,7,9,3]
# max=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         diff=l[i]-l[j]
#         if diff>max:
#             max=diff
# print(max)

'''9.	Print elements equal to average '''
# l=[3,5,7,9,3]
# l2=[]
# pos=len(l)
# sum=0
# for i in l:
#     sum=sum+i
# avg=int(sum/pos)
# for j in l:
#     if sum==j:
#         print(j)
  
'''10.	Find difference between max and min '''
# l=[3,5,7,9,3]
# max=0
# min=9
# for i in l:
#     if i>max:
#         max=i
#     elif i<min:
#         min=i
# diff=max-min
# print(diff)

'''27.	Replace each element with max + element '''
# l=[3,5,7,9,3]
# max=0
# l2=[]
# for i in l:
#     if i>max:
#         max=i
# for i in l:
#     i=i+max
#     l2.append(i)
# print(l2)

'''34.	Count elements appearing exactly twice '''
# l=[3,5,7,9,3]
# count2=0
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count==2:
#         count2=count2+1
# print(count2)

'''41.	Reverse only even elements '''
# l=[12,45,34,24]
# l2=[]
# for i in l:
#     if i%2==0:
#         rev=0
#         x=i
#         while x>0:
#             digit=x%10
#             rev=rev*10+digit
#             x=x//10
#         l2.append(rev)
#     else:
#         l2.append(i)
# print(l2)

'''56.	Find longest increasing sequence '''
# l = [1,2,3,1,2,5,6,0]
# curr=[l[0]]
# long=[l[0]]
# for i in range(1,len(l)):
#     if l[i]>l[i-1]:
#         curr.append(l[i])
#     else:
#         curr=[l[i]]
#     if len(curr)>len(long):
#         long=curr
# print(long)

# whole logic of this ques
'''🧠 Goal of Code
Find the longest continuous increasing sequence.
Input:
[1,2,3,1,2,5,6,0]
Output:
[1,2,5,6]
🔹 Line 1
l = [1,2,3,1,2,5,6,0]
We create a list named l.
The list has 8 elements.
Index	Value
0	1
1	2
2	3
3	1
4	2
5	5
6	6
7	0
🔹 Line 2
current = [l[0]]
Meaning
Create a list called current.
It stores the increasing sequence we are building right now.
Since:
l[0] = 1
So:
current = [1]
Why start with first element?
Because at beginning, we only know first number.
So current sequence starts there.
🔹 Line 3
longest = [l[0]]
Meaning
Create another list called longest.
It stores the best / longest sequence found so far.
Initially:
longest = [1]
Why separate lists?
current = current streak
longest = best streak saved
🔹 Line 4
for i in range(1, len(l)):
This starts a loop.
Step A: len(l)
List has 8 elements.
len(l) = 8
Step B: range(1,8)
Gives:
1,2,3,4,5,6,7
So i becomes:
1
2
3
4
5
6
7
Why start from 1?
Because we compare:
l[i] with l[i-1]
If i = 0, previous item doesn’t fit this logic.
🎬 Dry Run Starts
Initial:
current = [1]
longest = [1]
🔹 Line 5
if l[i] > l[i-1]:
Meaning
Check if current number is greater than previous number.
If yes:
👉 sequence is still increasing.
🔹 Iteration 1: i = 1
Current:
l[1] = 2
Previous:
l[0] = 1
Check:
2 > 1 ? YES
🔹 Line 6
current.append(l[i])
Meaning
Add current number to current sequence.
So:
current = [1,2]
🔹 Next Check
if len(current) > len(longest):
Lengths:
2 > 1 ? YES
🔹 Line 7
longest = current[:]
Meaning
Copy current sequence into longest.
Now:
longest = [1,2]
Why [:] ?
It creates a copy.
Without copy:
longest = current
Both names point to same list.
Then future changes in current would also change longest.
We don’t want that.
🔹 Iteration 2: i = 2
Compare:
3 > 2 ? YES
Append:
current = [1,2,3]
Length compare:
3 > 2 ? YES
Update:
longest = [1,2,3]
🔹 Iteration 3: i = 3
Compare:
1 > 3 ? NO
Sequence broke.
🔹 Else Block
current = [l[i]]
Set:
current = [1]
Why reset?
Old increasing run ended.
Start new run from current number.
🔹 Length Compare
1 > 3 ? NO
No update.
🔹 Iteration 4: i = 4
Compare:
2 > 1 ? YES
Append:
current = [1,2]
Length:
2 > 3 ? NO
🔹 Iteration 5: i = 5
Compare:
5 > 2 ? YES
Append:
current = [1,2,5]
Length:
3 > 3 ? NO
Equal is not greater.
So longest stays old one.
🔹 Iteration 6: i = 6
Compare:
6 > 5 ? YES
Append:
current = [1,2,5,6]
Length:
4 > 3 ? YES
Update:
longest = [1,2,5,6]
🔹 Iteration 7: i = 7
Compare:
0 > 6 ? NO
Reset:
current = [0]
Length:
1 > 4 ? NO
🔹 Final Line
print(longest)
Output:
[1,2,5,6]
🧠 Whole Logic in Human Language
Move through list:
If number goes up → continue current streak
If it drops / stops → start new streak
If current streak is best so far → save it
💡 Important Concepts Learned
list indexing
comparing neighbors
append
reset sequence
track best answer
copy list with [:]
🎯 Memory Trick
Increase? add
Break? restart
Bigger than best? save'''

'''57.	Find longest decreasing sequence '''
# l = [1,2,3,1,2,5,6,0]
# curr=[l[0]]
# dec=[l[0]]
# for i in range(1,len(l)):
#     if l[i]<l[i-1]:
#         curr.append(l[i])
#     else:
#         curr=[l[i]]
#     if len(curr)>len(dec):
#         dec=curr[:]
# print(dec)

'''58.	Replace element with next greater element '''
# l=[1,2,3,4]
# l2=[]
# for i in range(len(l)):
#     count=0
#     for j in range(i+1,len(l)):
#         if l[j]>l[i]:
#             l2.append(l[j])
#             count=1
#             break
#     if count==0:
#         l2.append(-1)
# print(l2)

'''59.	Replace element with previous smaller element '''
# l=[4,5,2,10]
# l2=[]
# for i in range(len(l)):
#     count=0
#     for j in range(i-1,-1,-1):
#         if l[j]<l[i]:
#             l2.append(l[j])
#             count=1
#             break
#     if count==0:
#         l2.append(0)
# print(l2)

''' 60.	Find equilibrium index (left sum = right sum)'''
# l=[1,3,5,2,2]
# for i in range(len(l)):
#     left=0
#     right=0
#     for j in range(0,i):
#         left=left+l[j]
#     for j in range(i+1,len(l)):
#         right=right+l[j]
#     if left==right:
#         print(i)
#         break

'''21.	Replace each element with double value '''
# l=[1,3,5,2,2]
# l2=[]
# for i in l:
#     i=i*2
#     l2.append(i)
# print(l2)

'''31.	Count how many times a given number appears '''
# l=[1,3,5,2,2]
# num=2
# count=0
# for i in l:
#     if i==2:
#         count=count+1
# print(count)


'''32.	Find all unique elements '''
# l=[1,3,5,2,2]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count==1:
#         l2.append(i)
# print(l2)

'''33.	Find all repeating elements '''
# l=[1,3,5,2,2]
# l2=[]
# count=0
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count>1:
#         print(i)
  
'''34.	Count elements appearing exactly twice '''
# l=[1,3,5,2,2]
# l2=[]
# count=0
# for i in l:
#     if i not in l2:
#      count2=0
#     for j in l:
#         if i==j:
#             count2=count2+1
#     if count2==2:
#         count=count+1
#         l2.append(i)
# print(count)

'''35.	Count elements appearing exactly once '''
# l=[1,3,5,2,2]
# l2=[]
# count=0
# for i in l:
#     if i not in l2:
#         count2=0
#         for j in l:
#             if i==j:
#                 count2=count2+1
#         if count2==1:
#             count=count+1
#             l2.append(i)
# print(count)

'''36.	Remove all repeated elements '''
# l=[1,3,5,2,2]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count==1:
#         l2.append(i)
# print(l2)

'''37.	Replace unique elements with 0 '''
# l=[1,3,5,2,2]
# l2=[]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count>1:
#         l2.append(i)
# print(l2)

'''38.	Find last non-repeating element '''
# l=[1,2,2,3,4,4,5,6,6]
# for i in range(len(l)-1,-1,-1):
#     count=0
#     for j in l:
#         if l[i]==j:
#             count=count+1
#     if count==1:
#         print(l[i])
#         break

'''39.	Find first repeating element '''
# l=[1,2,2,3,4,4,5,6,6]
# for i in l:
#     count=0
#     for j in l:
#         if i==j:
#             count=count+1
#     if count>1:
#         print(i)
#         break

'''41.	Reverse only even elements '''
# l=[19,12,34,24,79]
# l2=[]
# for i in l:
#     if i%2==0:
#         rev=0
#         x=i
#         while x>0:
#             digit=x%10
#             rev=rev*10+digit
#             x=x//10
#         l2.append(rev)
#     else:
#         l2.append(i)
# print(l2)

'''43.	Swap first and last element '''
# l=[19,12,34,24,79]
# x=l[0]
# l[0]=l[-1]
# l[-1]=x
# print(l)

'''44.	Swap largest and smallest element '''
# l=[19,12,34,24,79]
# large=0
# small=0
# for i in range(len(l)):
#     if l[i]>l[large]:
#         large=i
#     if l[i]<l[small]:
#         small=i
# x=l[large]
# l[large]=l[small]
# l[small]=x
# print(l)

'''45.	Move all negative numbers to front '''
# l=[-1,2,3,4,-5,6,-7]
# l2=[]
# for i in l:
#     if i<0:
#         l2.append(i)
# for i in l:
#     if i>0:
#         l2.append(i)
# print(l2)

'''47.	Arrange odd first then even '''
# l=[1,2,3,4,5,6,7,8,9]
# l2=[]
# for i in l:
#     if i%2!=0:
#         l2.append(i)
# for i in l:
#     if i%2==0:
#         l2.append(i)
# print(l2)


'''48.	Sort list in descending order (without sort) '''
# l=[5,6,3,9,1,2,3]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]<l[j]:
#             x=l[i]
#             l[i]=l[j]
#             l[j]=x
# print(l)

'''49.	Concatenate two lists '''
# l1=[1,2,3,4]
# l2=[5,6,7,8]
# for i in l2:
#     l1.append(i)
# print(l1)

'''50.	Find union of two lists '''
# l1=[1,2,3,4]
# l2=[3,4,5,6]
# for i in l1:
#     if i in l2:
#         print(i)

'''51.	Check if all elements are same '''
# l=[1,1,1,2,1]
# same=1
# for i in l:
#     if i!=l[0]:
#         same=0
#         break
# if same==1:
#     print("all ements are same")
# else:
#     print("all elements are not same")

'''52.	Check if list is strictly increasing '''
# l=[1,2,3,4]
# count=1
# for i in range(1,len(l)):
#     if l[i]<=l[i-1]:
#         count=0
#         break
# if count==1:
#     print("strictly increasing")
# else:
#     print("not increasing strictly")

'''53.	Check if list is strictly decreasing '''
# l=[5,4,3,2,1]
# count=1
# for i in range(1,len(l)):
#     if l[i]>=l[i-1]:
#         count=0
#         break
# if count==1:
#     print("strictly decreasing")
# else:
#     print("not strictly decreasing")

'''54.	Find pair with maximum sum '''
# l=[1,2,3,4]
# max=l[0]+l[1]
# a=l[0]
# b=l[1]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         s=l[i]+l[j]
#         if s>max:
#             max=s
#             a=l[i]
#             b=l[j]
# print(a,b)
# print(max)


'''55.	Find pair with minimum sum '''
# l=[1,2,3,4]
# min=l[0]+l[1]
# a=l[0]
# b=l[1]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         s=l[i]+l[j]
#         if s<min:
#             min=s
#             a=l[i]
#             b=l[j]
# print(a,b)
# print(min)

'''56.	Find longest consecutive sequence '''
# l = [100,4,200,1,3,2]
# l.sort()
# l2=[]
# temp=[l[0]]
# for i in range(1,len(l)):
#     if l[i]==l[i-1]+1:
#         temp.append(l[i])
#     elif l[i]==l[i-1]:
#         pass
#     else:
#         if len(temp)>len(l2):
#             l2=temp[:]
#         temp=[l[i]]
#     if len(temp)>len(l2):
#         l2=temp[:]
# print(l2)
    
''''''





    






    




       


        












       

    


        






















   
   




        
     


