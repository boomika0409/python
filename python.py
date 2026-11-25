

# a ={'a':[10,20,30] ,'b':20}
# print(a['a'][0])

# a="microorganisms"
# print(a[10:-2])

# a="good morning"

# # print(a[5:11+1:3])
# # print(a[-7::3])
# # print(a[-12::3])
# print(a[-2:-8-1:-3])


# a=10
# print(a)

# a=input("enter ")
# print(a)


# a=int(input("enter "))
# print(a)

# a=eval(input("enter "))
# print(type(a))


# a=int(input("enter:"))
# if a%2==0:
#     print("even")
# else:
#     print    


# l=eval(input("enter list"))

# if len(l)==5:
#     print("yes")
# else:
#     print("no")    

# ch=input("enter the word:")

# if "A"<=ch<="Z":
#     print("upper")
# elif "a"<=ch<="z":
#     print("lower") 
# else:
#     print("not an alpha")   

# un=input("enter:")
# if un=="haapy":
#     print("corect username")
#     pw=input("enter:")
#     if pw== "123456":
#         print("succesful login")
#     else:
#         print("incorrect password") 
# else:
#     Print("incorrect password")   


# i=1
# while i<=100:
#     if i%2==0:
#        print(i)
#     i+=1



# i=1
# while i<=100:
#     if i%2==0:
#        print(i)
#     i+=1


# n=int(input("enter num: "))
# rev=0

# while n>0:
#     id=n%10
#     n=n//10
#     rev=rev*10+id
#     print(rev)




# for i in range(1,50):
#          if i%2==0:  
#             print(i,"even" )

# l=[10,20,30]
# for i in l: 
#     print(i)

# s=input("enter:")
# out=" "

# for i in s:

#   if "A"<=i<="Z":
#       out+=chr(ord(i)+32)
#   elif "a"<=i<="z":
#       out+=chr(ord(i)-32)
#   else:
#       out+=id
# print(out)  
# # 
# s=input("enter:")
# out=" "

# for i in s:
#     rev=i+rev
# print(rev)    
    
# for i in range(1,6):
#     for j in range(1,6):
#        if i==j:
#           print(" * ",end=" ")
#        else:   
#           print(" ",end=" ")
#     print()   


# def convert(s,out):
#     out=" "
#     for i in s:
#         if'a'<=i<='z':
#            out+=chr(ord(i)-32)
#         else:
#             out+=i
#     print( out)
# convert(input('enter a string:'),' ')


# def convert():
#     s=input('enter:')
#     out=" "
#     for i in s:
#         if'a'<=i<='z':
#            out+=chr(ord(i)-32)
#         else:
#             out+=i
#     return(out)
# # print(convert())

# class college:
#     cname='GCEM'
#     cloc='Hoodi'
# s1=college()
# print(s1.cname,s1.cloc)
# college.cloc='KR Puram'
# print(college.cloc) 



# class college:
#     cname='GCEM'
#     cloc='Hoodi'
# s1=college()
# s2=college()
# print(s1.cname,s1.cloc)
# college.cloc='KR Puram'
# print(college.cloc) 
# print('changing loc wtsrp obj')
# s1.cloc='hoodi'

# print(s1.cloc)
# print(college.cloc)
# s1.name='boomi'
# s1.phone=1234567890


# s2.name='neetu'
# s2.phone=12345678456

# print('after changing')
# print(s1.cloc)
# print(s2.cloc)
# print(college.cloc)

class college:
    def __init__ (self,name,phone,usn):
      self.name=name
      self.phone=phone
      self.usn=usn 
    def display(self):
      print(self.name,self.phone,self.usn)

s1=college('boomi',12345,'gd12345')
s2=college('neetu',67890,'gd67899')
s1.display()
s2.display()        
        



