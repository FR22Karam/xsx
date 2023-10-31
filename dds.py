
def decoderAdbash(st):
    
    m=dict()
    nst=''
    ind=-1
    abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for ch in abc:
        m[abc[ind]]=ch
        m[ch]=abc[ind]
        ind -= 1
    for ch in st:
         nst += m[ch]
    return nst
def atbsh(st):
    m=dict()
    nst=''
    ind=-1
    abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for ch in abc:
        m[ch]=abc[ind]
        ind-= 1
    for ch in st:
        nst += m[ch]
    return nst    
        
def main():
    x= atbsh('HEAD')
    atbsh(atbsh('HAED'))
    print(decoderAdbash(x))

main()        
