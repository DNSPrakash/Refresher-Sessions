# print('Hello World')
# name_Mother="Sridevi"
# print(name_Mother)

# x=3
# y=x+3
# print(y)

# name='prakash'

# print(name[0],name[3],name[-1],name[0:4],'satya '+ name[0:6])

# multiple values assigning in single line

# x,y,z='srinu','sridevi','prasanna'
# print(x)
# print(y)
# print(z)
# # using collection
# cars=['bmw','benz','audi']
# x,y,z=cars
# print(y)

# global and local variables
#global
# x="opportunity"
# def newfunc():
#     print('job is '+ x)
# newfunc()
# # local
# x="opportunity"
# def newfunc():
#     x="acheivement"
#     print("job is "+x)
# newfunc()

# # global in function
# x="opputunity"
# def newfunc():
#     global x
#     x="everything"
# newfunc()
# print('job is '+x)

# Data types




# a=int(input())
# b=int(input())

# if(a&b):
#     print(True)
# else:
#     print(False)

n=int(input("Enter no of Products"))
for i in range(n):
    l=list(n)
    l[i-1]=int(input("Enter quantity of product",i))
print(l)
