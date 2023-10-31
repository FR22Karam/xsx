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

        while(n is not None):
            print(n.get_info(),end='')
            if(n.get_next() is not None):
                print('->',end='')
            n=n.get_next()
    def __str__(self) -> str:
        st=''
        n = self
        
        return ''.join([str(i) for i in self.to_list])

        while(n != None):
            st+=str(n.get_info())
            if(n.get_next() is not None):
                st+=' -> '
            n=n.get_next()
        return st
n1=Node(1,Node(2,Node(3)))
n1.print_chain()
