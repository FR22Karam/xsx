

def main():
    
    
    
    function_1 = lambda func_2 , x : func_2(func_2(x+6))
    function_2 = lambda x: function_1((lambda y: y+1), x)
    print(function_2(5))
    print(function_1(function_2,5))
main()
