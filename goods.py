def goods_price():
    d=dict()
    try:
        f = open('goods.txt','r')
    except  IOError() as e:
        print(e)
    st=f.read()
    ls=st.split(' ')
    for i in range(0,len(ls),3):
        d[ls[i]]=[ls[i+1],ls[i+2]]
        price=0
        item=input('enter prod num')
        cnt=int(input('Enter the gty'))
        while(item != 'n'):
            if item in d:
                if cnt <= d[item][1]:
                    price += d[item][0]*cnt
                    d[item][1]-= cnt
                else:
                    print('Not enough ')
        else:
            
            print('there no a cuch prod')
            
        item=input('enter prod num')
        cnt=int(input('Enter the gty'))
            
    ls=[]
    for i in d:
        
        
        ls.append(i,d[i][0],d[i][1])
        st=''
        for i in range(0,len(ls),3):
            
            st+=ls[i]+' '+ls[i+1]+' '+ls[i+2]+'\n'
            f=open('good.txt','w').write(st)
            f.close()
                    
                    
def main():

 print(goods_price())        
main()    
