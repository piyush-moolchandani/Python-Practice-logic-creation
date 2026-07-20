'''•	Reverse Array '''
# l=[1,2,3,4,5]
# l2=[]
# for i in range(len(l)-1,-1,-1):
#     l2.append(l[i])
# print(l2)

# optimized approach
# l=[1,2,3,4,5]
# left = 0
# right = len(l)-1
# while left<right:
#     l[left],l[right]=l[right],l[left]
#     left+=1
#     right-=1
# print(l)
'''Real answer ye hai:
Reverse Array me hum actually kar kya rahe hain?
Hum opposite positions wale elements ko swap karte hain. 
Har swap ke baad un dono elements ki final position fix ho jaati hai. 
Isliye unhe dobara touch nahi karte. Phir pointers ko ek step andar le aate hain. 
Jab pointers mil jaate hain ya cross kar jaate hain, poora array reverse ho chuka hota hai.

Why do we use two pointers?
Answer:
Kyunki ek pointer first element ko represent karta hai aur doosra last element ko.
Reverse me opposite elements exchange hote hain, isliye dono ends se start karke 
beech ki taraf move karna sabse efficient approach hai.
time compexity:o(n)
space o(1)'''




