def make(mat):
   
    
        return[j for i in mat for j in i]

def main():
    mat=[[12, 33], [44, 66], [7, 4], [32, 55]]
    print(make(mat))
main()    