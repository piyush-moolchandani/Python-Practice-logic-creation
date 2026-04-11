#output
#  You probably know till now, how to provide the output of the
# code you have written and that is with print() function
#  There is no other functions to provide the result on the
# terminal we just have to use print() function
#  Now when providing the output we can use variables in print
# statement using a formatted string as shown in the below
# example.
#by writting print() function we give output output and terminal both give output

name="piyush"
b=22
# print(a,b)#exampleit gives output

#formatted string-example dont make multiple strings make only one
# print("my name is",name,"and my age is",b) normal
#using f string
print(f"my name is {name} and my age is {b}")#its simple and clean use f for access it 
#when you insert { } in it it automatically captures now you want to do a mathematicall calculation or you want to use a variable or you are doing something different jo strings ke formation me nahi aane wala

# raw string-

#input statements-to take input from user we ask question from user in terminal
# input("enter your name")#example we are not saving it now so it is going in garbage where to save it very simple in variables beacause it is storage example

name=input("enter your name")# it has default data type which is string
print(name)

#to convert it into onteger type int infront of it ex-
int(input("enter your number"))

print(int(input("enter your number")))

num=int(input("enter your age"))
print(num)

j=input("enter your name")
print(j)
