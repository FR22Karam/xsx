def func(*lists):
    for   i in range(*lists):
        first=0
        last=0
        
        first+=lists[i][0]
        last+=lists[i][len(lists[i]-1)]
    return first,last
    

def main():
    l1=[7,6,1]
    l7=[2,4,6,8]
    l10=[9,3,1,4,2,8]
    func(l1,l7,l10)
main()    