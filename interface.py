import tkinter as tk

class hang():
    step = 0
    letters = [chr(i+ord('a')) for i in range(26)]

    def __init__(self, word):
        self.flip = False
        self.root = tk.Tk()
        self.fig = tk.PhotoImage(file = hang.file())
        self.image = tk.Label(self.root, image = self.fig)
        self.image.pack(pady = 20, padx = 30)
        self.word = 'Word: ' + word
        self.text = tk.Label(self.root, 
                           text = self.word, 
                           font = ('20'))
        self.text.pack()
        test = tk.Frame(self.root)
        test.pack()
        self.letter = tk.StringVar(self.root)
        self.letter.set('letter')
        self.chute = tk.OptionMenu(test, self.letter, *hang.letters)
        self.chute.config(width = 5)
        self.chute.grid(row = 0, column = 0)
        tk.Button(test, text = "Guess", 
                  command = self.check).grid(row = 0, column = 1)

    def wrong(self):
        try:
            hang.step += 1
            self.fig = tk.PhotoImage(file = hang.file())
            self.image['image'] = self.fig
        except:
            self.root.destroy()

    def right(self, word):
        self.word = 'Word: ' + word
        self.text['text'] = self.word

    def file():
        return 'Hangman{}.gif'.format(str(hang.step))

    def update(self):
        self.root.update()

    def check(self):
        self.flip = True

    def guess(self):
        var = self.flip
        self.flip = False
        return var

    def input(self):
        return self.letter.get()

    def end(self):
        self.fig = tk.PhotoImage(file = 'HangmanSafe.gif')
        hang.step = 10
        self.image['image'] = self.fig
