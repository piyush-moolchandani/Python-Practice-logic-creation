'''                                     STRINGS                                  '''
'''•	Reverse String '''
# n="python"
# new=""
# for i in range(len(n)-1,-1,-1):
#     new=new+n[i]
# print(new)
'''two pointers approach'''
# n="python"
# convert=list(n)
# i=0
# j=len(n)-1
# while i<j:
#     convert[i],convert[j]=convert[j],convert[i]
#     i+=1
#     j-=1
# n="".join(convert)
# print(n)

'''•	Reverse Words '''

