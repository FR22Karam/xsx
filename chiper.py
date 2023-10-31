class simple_chiper():
    
    def __init__(self,text,moves=5):
        
        self.text = text
        self.chr_list = self.create_chr_list()
        self.moves = self.corrent_moves(moves)

    def create_chr_list(self):
        
        
        temp_list = []
        for i in range(65,121):
           
           
            temp_list.append(chr(i))
        print(temp_list)
       
        return temp_list
    def corrent_moves(self , moves):
        set_moves = moves
        length= len(self.chr_list)
        if(set_moves > 0):
            while(set_moves > length -1):
                set_moves = set_moves - length
       
        elif(set_moves < 0):
            while(set_moves < length -1):
                set_moves = set_moves + length
            set_moves = set_moves - length 
        print(set_moves)
        return set_moves

chiper = simple_chiper('karam' ,95)
