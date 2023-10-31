def noAlpha(st):

    st1=''
    for i in st:
        
        if(i>='a' and i<='z' or i>='A' and i<='Z'):
           
           
           st1+=i
       
        else:
            
             st1=''
    return st1




def main():
    
    st='Please enter a string: this@is a_test! O1K '

    print(noAlpha(st))


main()

