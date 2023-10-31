def max_of_all(lst):
    out=[]
    for i in range(len(lst)):
        out.append(lst[i](2))
    max=out[0]
    for i in range(len(lst)):
        if(out[i]>max):
          max=out[i]
          ind=i
        
    return lst[i]
def main():
    f1 = lambda x: x+1 
    f2 = lambda x: x**2
    f_all = max_of_all([f1,f2])
    print(f_all(0))
    print(f_all(1))
    print(f_all(20))

main()    


    
        