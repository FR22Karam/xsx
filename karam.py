def get_text():
    while True:
        fName = input("enter file ")
        try:
            f=open(fName,'r')
            break 
        except FileNotFoundError as error:
            print(error)
    text=f.read()  
    f.close()
    return text      
def main():
    text=get_text()
    delete=input("delete word ")
    newStr=''
    newStr= text.replace(delete,'')
    f_out=open('remove.txt','w')
    f_out.write(" ")
    f_out.close()
main()
