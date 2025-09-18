# a =  int("2")
# b = 2
# sum = b+a
# print(sum)
# print(type(sum))


# a=int(input("enter the num"))
# b=int(input("enter the num"))

# str="hi"
# str2="bye"
# str3="snkjlvnedkv azk"
# print(len(str+str3+str2))
# print(str3.endswith("kz"))
# print(str.capitalize())
# print(str3.replace("n","ad"))
# print(str3.find("l"))
# print(str3.count("n"))

# print(str+str2)

# name = input("enter the  name")
# print(len(name))

# s="alsdc skadcla$ $$$$"
# print(s.count("$"))

# num = int(input("enter a number"))

# if(num%2==0):
#     print(num,"is even")
# else:
#     print(num,"is odd")

# num1 = int(input("enter the number"))
# num2 = int(input("enter the number"))
# num3 = int(input("enter the number"))


# if(num1>num2 and num1>num3):
#     print(num1)
# elif(num2>num1 and num2>num3):
    
#     print(num2)
# else:
#     print(num3)

# num = int(input("enter a number"))

# if(num%7==0):
#     print(num,"is a multiple of 7")
# else:
#     print(num,"is not a multiple of 7")

# str="hihallohowareyou"

# print(str[5])

# str2=["hi","hello",58]
# print(len(str2))
# print(str2)
# str2[2] = 92
# print(str2)

# print(str2[:9])

# str2.append(47)

# str3 = [54,78,56,33,158,669,961,396,369]
# str3.sort()
# str3.reverse()
# str3.insert(0,7)

# print(str3)


# str = ["apple","banana","carrort","apple"] 
# str.sort()
# # str.remove("apple")
# str.pop()
# print(str) 

# str = (1,2,4,1,5,1,6)
# print(str.index(1))

# str = input("enter the fav car")
# str2 = input("enter the fav car")
# str3 = input("enter the fav car")
# lis = []
# lis.insert(0,str)
# lis.insert(1,str2)
# lis.insert(2,str3)
# print(lis)

# str = [1,2,3,2,1]
# rve=str.copy()
# rve.reverse()

# if(str == rve):
#     print(str,"is a palindrom")
# else:
#     print(str,"not  a palindrom")

# str = ["A","B","C","D","A","A","A","D","B","B","C"]
# str.sort()
# print(str )

# str = {
#     "name": "Prajith",
#     "Age": 18,

# }

# lis = list(str.items()) 
# print(lis[1])

# str2 = {
#     "fav" : "music",
#     "lan" : "mal"
# }

# print(str.keys())
# print(str.values())
# print(str.get("name"))
# str.update(str2)
# print(str)

# str = {1,2,8,3,4,1,19,14,5,6,7}
# str2= {1,1,2,5,5,7,8,89,11}
# print(type(str))
# str.add(45)
# str.remove(2)
# # str.clear()
# str.pop() 

# print(str.union(str2))
# c = [1,2,3,6,5,4,7,89,6,5,6,9,8,4,5,2,2,564,13,2,156]
# i=0
# while i < len(c):
#     0
    
    
#     print(c[i])
#     i+=1

# i = 0
# while i <= 5:
#     if( i== 3):
#         i+=1
#         break
#     print(i)
#     i+=1

# i = (1,2,3,4,5,6,78,9,8,84,654,3,1,64,3,2,78)
# x = 78
# idx = 0
# for e in i:
#     if(e == x):
#         print(e, idx)
#         break
#     idx+=1



# for a in range(10,-2):
#     print(a)

# for i in range(100,0,-1):
    
#     print(i)

# x=int(input("enter a number"))

# for i in x:
#     s = x*i
#     print(s)
#     if (i<=10):
#         break
#     i+=1

# for i in range(1,11):
#     s=i*x
#     print(s)

# n= 6
# s=1
# i=1
# while i<n:
#     s *= i 
#     i+=1
# print(s)

# def length(a):
#     print( len(a))

    
# b=[1,2,3,4,5,6,7,8,9,10,1548]
# length(b)

# def elm(a):
#     for i in a:
#         print(i,end=" ")

# b=[1,2,3,78,4,5,6,7,8,17,9,15]
# elm(b)

# n = int(input("enter a number"))

# def fact(a):
#     s=1
#     for i in range(1,n+1):
#         s*=i
#     print(s)
        
# fact(n)


# n= int(input("enter a number"))

# def con(a):
#     print( a/87)

# con(n)

# def cal(a):
#     if(a==0):
#         return 0
#     return cal(a-1)+a
# sum = cal(5)
# print(sum)

# def lis(list,idx):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     lis(list,idx+1)

# cars = ["ignis","baleno","city"]

# lis(cars,0)

# word = "learing"
# with open("practice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("java","Python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)

#     if(data.find(word) !=-1):
#         print("found")
#     else:
#         print("not found")

# def check_for_line():
#     word = "learing"
#     data = True
#     line_no =1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1

# check_for_line()

with  open("practice.txt","r") as f:
    data = f.read()
    print(data)

    nums  =  data.split(",")
    print(nums)

    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name,"your avg score is:", sum/3)

s1 = Student("Prajith",[100,99,98])
s1.get_avg()

s1.name = "Pranav"
s1.get_avg()

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account =  acc
    def debit(self,amount):
        self.balance -= amount
        print("RS",amount,"Was debited")
    
    def credit(self,amount):
        self.balance += amount
        print("RS",amount,"was Credited")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12345)
acc1.debit(10254)
acc1.credit(102548)

class Circle: 
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return(22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2* (22/7) * self.radius
        

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role = ",self.role)
        print("Departement",self.dept)
        print("salary is", self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","75000")


e1 = Employee("accountant","Finance","60000")
e1.showDetails()

engg1 = Engineer("Elon Musk",40)
engg1.showDetails()

# class Order:
#     def __init__(self,item,price):
#         self.item = item
#         self.price = price

        