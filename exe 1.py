def divide_list(arr,num_list):
    
    n=len(arr)//num_list
    
    
    return[[item for item in arr[s:s+n:1]]for s in range(0,len(arr),n)]
    
    
def main():
    arr=[12,33,44,6,6,7,4,3,2,5,5,9]
    print(divide_list(arr,3))
    
main()
    