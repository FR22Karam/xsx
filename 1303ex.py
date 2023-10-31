class Student:

    def __init__(self,name,id,age):
        self.__name=name #properties in class starting with '__' are "private"
        self.__id=id
        self.__age=age

    def __str__(self): #string repr returns str
        return f'Name is: {self.__name}\nID is: {self.__id}\nAge is: {self.__age}'
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name



class Node:
    def __init__(self,info,next=None):
        self.__info=info
        self.__next=next
    
    def get_info(self):
        return self.__info
    
    def set_info(self,info):
        self.__info=info
    
    def get_next(self):
        return self.__next

    def set_next(self,next):
        self.__next=next

    def print_chain(self):
        n = self
        while(n != None): #while(n != null)
            print(n.get_info(),end='')
            if(n.get_next() != None):
                print(' -> ',end='')
            n=n.get_next()

    def to_list(self) -> list:
        ls=[]
        n = self
        while(n != None):
            ls.append(n.get_info())
            n = n.get_next()
        return ls

    def __str__(self) -> str:
        
        return ' -> '.join([str(i) for i in self.to_list() ])
        '''while(n != None): 
            st+=str(n.get_info())
            if(n.get_next() != None):
                st+=' -> '
            n=n.get_next()
        return st'''



def print_chain(n):

    while(n != None): #while(n != null)
        print(n.get_info(),end='')
        if(n.get_next() != None):
            print(' -> ',end='')
        n=n.get_next()

n1=Node(1,Node(2,Node(3)))
#print(n1) #works because we implemented __str__

s=Student("Dan","1",27)
s1=Student("Kenan","2",26)

sn1=Node(s,Node(s1,Node([1,2,4])))

sn1.print_chain()