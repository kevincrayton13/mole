import tkinter as tk
import random

class gamedata:
    def __init__(self):
        self.isRunning = False
        self.indexlist = [0, 0, 0]
        self.pace = 750
        self.score = 0
        self.timeLeft = 30
        self.odds = 15

def score_increment():
    '''adds one to game's score and updates display'''
    game.score += 1
    score.config(text = 'Score: ' + str(game.score))

def button_selector(index):
    '''selects a game button based on the index returned'''
    if index == 0:
        return m
    elif index == 1:
        return m1
    elif index == 2:
        return m2
    elif index == 3:
        return m3
    elif index == 4:
        return m4
    elif index == 5:
        return m5
    elif index == 6:
        return m6
    elif index == 7:
        return m7
    elif index == 8:
        return m8
    else:
        return 'blank'

def button_changer(button, mode):
    '''switches buttons between being a mole to being a normal button'''
    if button == 'blank': return
    if mode == 0:
        button.config(text = '', bg = '#222222', command = '')
    else:
        button.config(text = 'CLICK ME', bg = '#0000ff', command = lambda: (score_increment(), board_reset()))

def cancel_reset():
    '''Resets the game variables as a reset of pressing end game button'''
    game.isRunning = False
    game.timeLeft = 30
    start.configure(text = 'Start Game', bg = '#00FF00', command = lambda: (gstart(), gloop(), clock()))

def board_reset():
    '''removes all moles from the board'''
    for index in game.indexlist:
        button_changer(button_selector(index), 0)

def gstart():
    '''sets the appropriate variables at the start of a game'''
    game.isRunning = True
    game.score = 0
    start.configure(text = 'End Game', bg = '#ff0000', command = cancel_reset)
    score.config(text = 'Score: ' + str(game.score))


def clock():
    '''counts down from thirty'''
    if game.isRunning == False: return
    game.timeLeft -= 1
    timeLeft.config(text = 'Time Left: ' + str(game.timeLeft))
    if game.timeLeft == 0:
        game.isRunning = False
        game.timeLeft = 30
        start.configure(text = 'Start Game', bg = '#00FF00', command = lambda: (gstart(), gloop(), clock()))
        return
    root.after(1000, clock)

def gloop():
    """game's main loop"""
    if game.isRunning:
        #resets previous selections
        board_reset()
        game.indexlist = [random.choice(range(game.odds)), random.choice(range(game.odds)), random.choice(range(game.odds))]
        #applies new moles
        for index in game.indexlist:
            button_changer(button_selector(index), 1)
    else:
        return
    root.after(game.pace, gloop)




def main():
    global root, m, m1, m2, m3, m4, m5, m6, m7, m8, start, timeLeft, score, pic, game
    root = tk.Tk()
    root.title('Wack-a-Mole: Tkinter edition')
    #root.iconbitmap('images\\icon.ico')

    game = gamedata()

    #the mole buttons
    m = tk.Button(root, height = 10, width = 30, bg = '#222222')
    m1 = tk.Button(root, height = 10, width = 30, bg = '#222222')
    m2 = tk.Button(root, height = 10, width = 30, bg = '#222222')
    m3 = tk.Button(root, height = 10, width = 30, bg = '#222222')
    m4 = tk.Button(root, height = 10, width = 30, bg = '#222222')
    m5 = tk.Button(root, height = 10, width = 30, bg = '#222222')
    m6 = tk.Button(root, height = 10, width = 30, bg = '#222222')
    m7 = tk.Button(root, height = 10, width = 30, bg = '#222222')
    m8 = tk.Button(root, height = 10, width = 30, bg = '#222222')
    #list of buttons used to update the game
    buttons = [m, m1, m2, m3, m4, m5, m6, m7, m8]

    #Lower display
    start = tk.Button(root, text = 'Start Game', width = 30, bg = '#00FF00', relief = tk.RAISED, command = lambda: (gstart(), gloop(), clock()))
    timeLeft = tk.Label(root, text = 'Time Left: ' + str(game.timeLeft))
    score = tk.Label(root, text = 'Score: ' + str(game.score))

    #packing
    m.grid(row = 0, column = 0)
    m1.grid(row = 0, column = 1)
    m2.grid(row = 0, column = 2)
    m3.grid(row = 1, column = 0)
    m4.grid(row = 1, column = 1)
    m5.grid(row = 1, column = 2)
    m6.grid(row = 2, column = 0)
    m7.grid(row = 2, column = 1)
    m8.grid(row = 2, column = 2)
    start.grid(row = 3, column = 0)
    timeLeft.grid(row = 3, column = 1, sticky = tk.W)
    score.grid(row = 3, column = 2, sticky = tk.W)

    root.mainloop()


if __name__ == '__main__':
    main()
