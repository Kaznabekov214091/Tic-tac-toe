class Board:
    def __init__(self):
        self.board = [" "] * 9

    def show_board(self):
        print(f"""
               |        |    
           {self.board[0]}   |    {self.board[1]}   |   {self.board[2]}
               |        |
       - - - - - - - - - - - - - 
               |        |    
           {self.board[3]}   |    {self.board[4]}   |   {self.board[5]}
               |        | 
       - - - - - - - - - - - - - 
               |        |
           {self.board[6]}   |    {self.board[7]}   |   {self.board[8]}
               |        |
        """)
