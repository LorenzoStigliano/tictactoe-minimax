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
        # Check rows
        for x in range(3):
            if self.current_state[x] == ["X","X","X"]:
                self.result = "X"
                return
            if self.current_state[x] == ["O","O","O"]:
                self.result = "O"
                return
        # Check columns
        for y in range(3):
            column = []
            for x in range(3):
                column.append(self.current_state[x][y])
            if column == ["O","O","O"]:
                    self.result ="O"
                    return
            if column == ["X","X","X"]:
                    self.result = "X"
                    return

        # Check diagonals
        # Main diagonal win
        if (self.current_state[0][0] != '.' and
        self.current_state[0][0] == self.current_state[1][1] and
        self.current_state[0][0] == self.current_state[2][2]):
            self.result = self.current_state[0][0]
            return

        # Second diagonal win
        if (self.current_state[0][2] != '.' and
        self.current_state[0][2] == self.current_state[1][1] and
        self.current_state[0][2] == self.current_state[2][0]):
            self.result = self.current_state[0][2]
            return

        # Check if board is full
        for x in range(3):
            for y in range(3):
                if self.current_state[x][y] == ".":
                    self.result = None
                    return
        self.result = "D"

    def play_player(self):

        play = True
        while play:
            print("It is " +self.player_turn+"'s turn.")
            x = int(input("Please provide an x-coordinate: "))
            y = int(input("Please provide an y-coordinate: "))
            self.update_board(x,y)
            self.update_player_turn()
            self.print_board()
            self.result_updater()
            if self.result != None:
                if(self.result == "D"):
                    print("Its a Draw!")
                else:
                    print(self.result + " won the game!")
                play = False

    #AI implemataion
    def best_move(self):
        bestScore = -2
        best_x = 0
        best_y = 0
        for x in range(3):
            for y in range(3):
                if self.current_state[x][y] == ".":
                    self.current_state[x][y] = "O"
                    score = self.minimax(False)
                    self.current_state[x][y] = "."
                    if score>bestScore:
                        bestScore = score
                        best_x = x
                        best_y = y
        return best_x, best_y

    def minimax(self,isMaximising):
        self.result_updater()
        if self.result != None:
            if self.result == "O":
                return 1
            elif self.result == "X":
                return -1
            else:
                return 0

        if isMaximising:
            bestScore = -2
            for x in range(3):
                for y in range(3):
                    if self.current_state[x][y] == ".":
                        self.current_state[x][y] = "O"
                        score = self.minimax(False)
                        self.current_state[x][y] = "."
                        bestScore = max(score,bestScore)
            return bestScore

        else:
            bestScore = 2
            for x in range(3):
                for y in range(3):
                    if self.current_state[x][y] == ".":
                        self.current_state[x][y] = "X"
                        score = self.minimax(True)
                        self.current_state[x][y] = "."
                        bestScore = min(score,bestScore)
            return bestScore

    def play_bot(self):

        while True:
            self.result_updater()
            if self.result == "D":
                print("Its a Draw!")
                return
            elif self.result != None:
                print(self.result + " won the game!")
                return
            else:
                if self.player_turn == "X":
                    print("It is " +self.player_turn+"'s turn.")
                    x = int(input("Please provide an x-coordinate: "))
                    y = int(input("Please provide an y-coordinate: "))
                    self.update_board(x,y)
                    self.update_player_turn()
                    self.print_board()
                #AI Bot plays is isMaximising player
                else:
                    print("Its the bot's turn.")
                    x, y = self.best_move()
                    self.update_board(x,y)
                    self.update_player_turn()
                    self.print_board()

def main():
    g = Game()
    g.play_bot()

if __name__ == "__main__":
    main()
