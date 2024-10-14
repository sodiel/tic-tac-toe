from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

class TicTacToe:
    def __init__(self):
        self.board = [' ']*9
        self.winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # Строки
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # Столбцы
            (0, 4, 8), (2, 4, 6)             # Диагональ
        ]
    

@app.route("/")
def index():
    return render_template("index.html")
    
if __name__ == '__main__':
    app.run(debug=True)