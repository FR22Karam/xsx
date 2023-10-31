class Point:
    def __init__(self,x,y):
        if x<0 or x>3840 or y<0 or y>2160:
            raise  Exception ('out of range')
        self.__x=x
        self.__y=y
        
        
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,x):
        if x<0 or x>3840 :
            raise  Exception('out of range')
        self.__x=x
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,y):
        
        if  y<0 or y>2160:
            raise  Exception('out of range ')
        self.__y=y    
     
    def __str__(self):
        return f"({self.__x},{self.__y})"
def main():
    try:
        p1=Point(23,569)
        print(p1.x)
        p1.x=100
        print(p1.x)
    except Exception as er:
        print(er)
main()    

    