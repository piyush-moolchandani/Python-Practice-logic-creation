# what are data types
""" Data types are the things we store in Variables and it
defines what data type variables are.
 Python has built-in data types for different kinds of data."""

#1 numbers

a=12
print(type(a)) # int type from negative to natural numbers whole will be integer

b=1.5
print(type(b))# float (float captures decimal and fraction value )

v=34j
print(type(v))# complex(in maths we have imaginary value that we called iota (i) in maths we are solving sum but in answer we have some missing value that is called i for using imaginary num in python we use complex but we can only write j not another alphabets)

#2 strings 
""" 
This is used to store anything in python, literally anything 

 that are available on your keyboard.

 You have to use quotes to store anything and it will be 

 considered as string. You can use double Quotes (“ ”) or 

 single quotes (‘ ’) to store both works same"""

  #to make string 
st="21321343gfnfgnfgn#$$%"
print(type(st))

#boolean
""" 
Theres nothing much to say this is the data type which 

 will and always give the result of True and False"""

k=True
print(type(k))
"""alsways right first letter in capital"""

#strings and type conversion
""" You know what strings are but you must also know string
take more space than other data types like int, float etc
 This happens because String stores every character with
their own Unicode
 unicode is a universal character encoding standard that
assigns a unique number (code point) to every character,
regardless of language
 Like “A” unicode is 65 and “ ” this emoji unicode is 128522,
you can check them by using ord() function in python and
convert them back using chr() function"""

a="A"
print(ord(a))# why it takes extra space every value of string have their special unicode to check type ord every number alpha had special unicode and string save them 
#thats why it takes extra space 

a=65
print(chr(a)) # it conversts unicode to character 

# indexing 
b="hello brother" # ok lets suppose we can access hello,h,t,or any other character here so yes we can do that and this is done through indexing
# so indexing start always from zero "sher" is a string and its indexing goes like 0123 it is called positive indexing to start from last we have 
# negative indexing "sher" from this i have to print only h we use negative indexing goes like -1,-2,-3,-4  to operate indexing we use [] which we called subscript operator
h="sher"
print(h[1]) # if we write 5 we get error beacuse we only have 0to3 values
print(h[-3]) # negative indexing

#string slicing 
"""
You must have thought there are so many characters in a
string but can you access everyone.
 Yes thats possible using slicing. slicing starts from 0 and
goes till the number of characters you have.
 eg - a = “Hello” print(a[0]) ==> output - “H
 There is negative indexing as well and it starts from -1, but
the starting position is from the back of the string
 eg - a = “Hello” print(a[-1]) ==> output - “o”
"""
# basically we take out slice of string just like a cake like we have a long string we can cut one part from it and can take out this is known as string slicing
e="SHER CODER"# so lets assume in   a[start point of index : stop point of index : steps of our slicing]
print(e[0:4:1])# slicing stops at -1 yani jaha tak likhenge uske ek pichle tak rukega
print(e[5::1])# space in between will also count as index so if we not writing any value to stop we are saying by default go till the end we can write 10 also 
# by default it takes only 1 steps if we remove start point by default it will start from 0
print(e[6:9:1])
print(e[-2:-5:-1])
print(e[2:3:1])

c="piyush"
print(c[-4:6:1])

l="python"
for i in l:
    print(i[-1:-7:-1])

fc="my name is piyush"
print(fc[8:10:1])

list=[2,4,5,6,7,8,9,3,4]
print(list[-1:5:-1])
print(list[4:5:1])

ktr="my cc is bad"
print(ktr[3:5:1])
print(ktr[-1:-4:-1])

ty=57
print(chr(ty))

#type conversion
""" to convert data from there types to another type for ex- converting integer to float
 For understanding type conversion you have to look at these 
4 things-int,float,str,bool
 There are more functions like this but these are 4 main
function, looking at these functions you can guess these are 
used to convert one data type to another
3 eg a = 12 
 a = str(a)
 print(a) ==> “12” (a will be converted to string)
 
 what is function ()-paranthesis bracket is basically a function kisi bhi work ke aage ye() lag jae wo function ban jata hai"""

a=12#type is int
a=str(a)#we convert it into string 
print(type(a))#this is what type conversion means

f="12"
f=int(f)#can we convert charcters into int so answer is no basic logic 
print(type(f))

#boolean is very imp
g=0
print(bool(g))#if above zero everything is true only there are 7 false values
#1-falseitself,2-0,3-0.0,4-emptystring,5-emptylist,6-emptytuple,7-emptydictonary
#this is what type conversion is 
#converting these from functions is known as explicit
#implicit means python automatically converts any number

c=12
print(12/3)#this is implicit type conversion python checks that fraction values come and give answer in float

