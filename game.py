class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['.','.','.'],
                              ['.','.','.'],
                              ['.','.','.']]

        # Player X always plays first
        self.player_turn = 'X'

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
        return self.current_state[x][y] == "."

    def play_2_player(self):

        while True:
            self.print_board()
            print("It is " +self.player_turn+"'s turn.")
            x = int(input("Please provide an x-coordinate: "))
            y = int(input("Please provide an y-coordinate: "))
            self.update_board(x,y)
            self.update_player_turn()

def main():
    g = Game()
    g.play_2_player()

if __name__ == "__main__":
    main()
