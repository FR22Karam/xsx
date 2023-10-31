def sumDigit(num):
    Sum=0
    while(num>0):
        Sum+=num%10
        Sum=num//10
    return Sum


def main():
 print(sumDigit(123))

main()    
    

