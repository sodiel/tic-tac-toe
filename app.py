from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

class TicTacToe:
    def __init__(self):
        self.board = [' ']*9

        self.current_player = "X"


        self.winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # Строки
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # Столбцы
            (0, 4, 8), (2, 4, 6)             # Диагональ
        ]
    

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if self.current_player == "X":
                self.current_player = "O"
            else:
                 self.current_player = "X"
            return True
        return False


    def check_winner(self):
        for combo in self.winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        if ' ' not in self.board:
            return "Ничья"
        return None
    


    def get_winning_combination(self):
        for combo in self.winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return combo
        return None

    

    def reset_board(self):
        self.board = [' ']*9


game = TicTacToe()


@app.route("/")
def index():
    return render_template("index.html", board=game.board)
    

@app.route("/make_move", methods=["POST"])
def make_move():
    data = request.get_json()
    position = data['position']
    if game.make_move(position):
        winner = game.check_winner()
        winning_combination = game.get_winning_combination()
        return jsonify({"status": "success", "winner": winner, "board": game.board, "winning_combination": winning_combination})
    else:
        return jsonify({"status": "error", "message": "Invalid move"})


@app.route("/restart", methods=["POST"])
def clear():
    game.reset_board()
    return jsonify({"status": "success"})


if __name__ == '__main__':
    app.run(debug=True)