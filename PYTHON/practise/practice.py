# Cars=int(input("Enter no of cars "))
# Bikes=int(input("Enter no of bikes "))
# Caramount=Cars*40
# Bikeamount=Bikes*20
# print("No of Vehicles=",Cars+Bikes)
# print("caramount=",Caramount)
# print("bikeamount=",Bikeamount)
# print("Total Amount = ",Caramount+Bikeamount)


#Store management software

# product1=40
# product2=50
# product3=60
# qtyproduct1=int(input("Enter the quantity of Product 1 "))
# qtyproduct2=int(input("Enter the quantity of Product 2 "))
# qtyproduct3=int(input("Enter the quantity of Product 3 "))
# totalPayment=(product1*qtyproduct1)+(product2*qtyproduct2)+(product3*qtyproduct3)
# print("Totol Amount = ",totalPayment)


#if else

# family=["prakash","srinivas","sridevi","prasanna","pavan","krishnveni"]
# for i in family:
#     print(i)

# qtyproduct1=int(input("Enter the quantity of Product 1 "))
# qtyproduct2=int(input("Enter the quantity of Product 2 "))
# qtyproduct3=int(input("Enter the quantity of Product 3 "))
# l=[qtyproduct1*400,qtyproduct2*300,qtyproduct3*300]
# T=0
# for i in l:
#     print("Amount of Product",i)
#     T=+i
# print(T)


# product_1 = int(input('enter a  product quantity'))
# product_2 = int(input('enter a  product quantity'))
# product_3 = int(input('enter a  product quantity'))
# product_4 = int(input('enter a  product quantity'))
# product_5 = int(input('enter a  product quantity'))

# l=[product_1, product_2, product_3, product_4, product_5]
# for i in l:
#     print(i)
# if (product_1<=0 or product_2<=0 or product_3<=0 or product_4<=0 or product_5<=0):
#     print('please enter the positive values')
# else:
#     print(product_1*100 + product_2*200 + product_3*300 + product_4*400 + product_5*500)


#list
# l=[1,2,3,4,5,'aditya',True]
# print(l)
# print(l[0])
# print(l[5])
# print(l[1:6])
# print(l[3:])
# print(l*2)


# #tuple
# t=(1,2,3,4,5,6,7,8) #tuple cant modified after creating
# print(t[5])
# print(t[2:6])
# print(t[4:])

# #dictionary

# d={"prabhas":6.2,"allu Arjun":5.8,"NTR":5.7,"Ramcharan":5.7}
# print(d)
# print(d.values())
# print(d.keys())
# print(d[2])



# clgname=input("Enter college name :")
# rollno=input("Enter Roll no:")
# d1={clgname:rollno}
# print(d1)


product_1 = int(input('enter of product 1 quantity'))
product_2 = int(input('enter of product 2 quantity'))
product_3 = int(input('enter of product 3 quantity'))
product_4 = int(input('enter of product 4 quantity'))
product_5 = int(input('enter of product 5 quantity'))

if((product_1<=0) or (product_2<=0) or (product_3<=0) or (product_4<=0) or (product_5<=0)):
    print("please enter the correct value")
else:
    print("The product quantity with price: ")
    total = product_1*200 + product_2*300 + product_3*400 + product_4*100 + product_5*200
    entries = {product_1 : 200,product_2 : 300, product_3 : 400, product_4 : 100, product_5 : 200}  
    x = open("mydata.txt","a") 
    print("The amount of all products")
    print("The amount of all products",file=x)
    for i,p in entries.items():
      print(i,p)
      print(i,p,file=x)
    print("The amount that you need: ")
    print("The amount that you need: ",file=x)
    print(total)
    print(total,file=x)










