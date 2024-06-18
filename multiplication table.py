'''write a program to print the first 10 trems of the multiplication
table for given number'''

n=int(input("enter the number:"))
for i in range(1,11):
  print(n,"*",i,"=","%2d"%(n*i))
