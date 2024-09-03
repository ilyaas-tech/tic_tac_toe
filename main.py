from tkinter import *
def step(row, col):
    global player

    if board[row][col]['text'] == '' and check_winner() is False:
        if player == 'x':
            board[row][col]['text'] = 'x'

            if check_winner() is False:
                label.config(text='Ходит: O')

            if check_winner() is True:
                label.config(text='Победил: X')

            if check_winner() is False and empty_spaces() is False:
                label.config(text='Ничья')
                for row in range(3):
                    for col in range(3):
                        board[row][col].config(bg='#ffff00')


            player = 'o'

        else:
            board[row][col]['text'] = 'o'

            if check_winner() is False:
                label.config(text='Ходит: X')

            if check_winner() is True:
                label.config(text='Победил: O')

            if check_winner() is False and empty_spaces() is False:
                label.config(text='Ничья')
                for row in range(3):
                    for col in range(3):
                        board[row][col].config(bg='#ffff00')

            player = 'x'


def check_winner():
    for row in range(3):
        if board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text'] != '':
            board[row][0].config(bg="green")
            board[row][1].config(bg="green")
            board[row][2].config(bg="green")

            return True

    for col in range(3):
        if board[0][col]['text'] == board[1][col]['text'] == board[2][col]['text'] != '':
            board[0][col].config(bg="green")
            board[1][col].config(bg="green")
            board[2][col].config(bg="green")

            return True

    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != '':
        board[0][0].config(bg="green")
        board[1][1].config(bg="green")
        board[2][2].config(bg="green")

        return True

    elif board[2][0]['text'] == board[1][1]['text'] == board[0][2]['text'] != '':
        board[2][0].config(bg="green")
        board[1][1].config(bg="green")
        board[0][2].config(bg="green")

        return True

    else:
        return False

def empty_spaces():
    for row in range(3):
        for col in range(3):
            if board[row][col]['text'] == '':
                return True
    return False

def reset():
    global player

    for row in range(3):
        for col in range(3):
            board[row][col].config(text = '', bg = '#f0f0f0')
    player = 'x'
    label.config(text='Ходит: X')


window = Tk()
window.title("крестики нолики")
window.geometry("600x620")

label = Label(text="добро пожаловать в игру")
label.pack()
restart = Button(text = 'Перезапустить игру', command = reset)
restart.pack()

players = ['x', 'o']
player = 'x'

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

frame = Frame(window)
frame.pack()

for row in range(3):
    for col in range(3):
        board[row][col] = Button(frame, font = ('consolas', 20), text = '', width = 10, height = 5, command = lambda row = row, col = col: step(row, col))
        board[row][col].grid(row = row, column = col)


window.mainloop()