class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['.','.','.'],
                              ['.','.','.'],
                              ['.','.','.']]

        # Player X always plays first
        self.player_turn = 'X'
        self.result = None

    def print_board(self):
        board = ""
        for i in range(3):
            for j in range(3):
                if(j==2):
                    board = board +self.current_state[i][j]+"|"+"\n"
                else:
                    board = board +self.current_state[i][j]+"|"
        print(board)

    def update_board(self,x,y):
        if self.is_valid(x,y):
            self.current_state[x][y] = self.player_turn
        else:
            print("\n")
            x = int(input("Please provide a valid x-coordinate: "))
            y = int(input("Please provide a valid y-coordinate: "))
            self.update_board(x,y)

    def update_player_turn(self):
        if self.player_turn == "X":
            self.player_turn = "O"
        else:
            self.player_turn = "X"

    def is_valid(self,x,y):
        if  (x<3 and x>-1 and y<3 and y>-1):
            return self.current_state[x][y] == "."

    def result_updater(self):
        #check rows
        for x in range(3):
            if self.current_state[x] == ["X","X","X"]:
                self.result = "X"
            if self.current_state[x] == ["O","O","O"]:
                self.result = "O"

        #check columns

        #check diagonals

        #check if board is full

    #def max(self):

    #def min(self):

    def play_2_player(self):

        while True:
            self.result_updater()
            if self.result != None:
                print(self.result + "won the game!")
            else:
                print("It is " +self.player_turn+"'s turn.")
                x = int(input("Please provide an x-coordinate: "))
                y = int(input("Please provide an y-coordinate: "))
                self.update_board(x,y)
                self.update_player_turn()
                self.print_board()


    def play(self):

        while True:
            self.result()
            if self.result != None:
                print(self.result + "won the game!")
            else:
                if self.player_turn == "X":
                    print("It is " +self.player_turn+"'s turn.")
                    x = int(input("Please provide an x-coordinate: "))
                    y = int(input("Please provide an y-coordinate: "))
                    self.update_board(x,y)
                    self.update_player_turn()
                    self.print_board()
                #AI Bot plays
                else:
                    print("Its the bot's turn.")
                    #minimax check should return x and y
                    self.update_board(x,y)
                    self.update_player_turn()
                    self.print_board()

def main():
    g = Game()
    g.play_2_player()

if __name__ == "__main__":
    main()
