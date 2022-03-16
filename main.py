from turtle import left
import ScrollableFrame

import tkinter as tk
import tkinter.ttk as ttk
import pandas

# ここにクラスのコードを書き込む

class Application():
    def __init__(self, master=None):
        self.root = tk.Tk()
        self.root.title('scrollbar trial')
       
        self.create_widgets()

        self.root.mainloop()

    def create_widgets(self):
        self.buttonFrame = tk.Frame(self.root)
        self.buttonFrame.pack()
        self.button = tk.Button(self.buttonFrame, text='Open')
        self.button.pack()

        self.canvas_frame = ScrollableFrame.ScrollableFrame(self.root, minimal_canvas_size)
        self.canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(side=tk.TOP, fill=tk.Y, expand=False)

        self.label_title1 = ttk.Label(self.control_frame, text='Window coordinate')
        self.label_title1.pack()

        # canvasに画像をセットする
        self.ReadCsv()


    def ReadCsv(self):
        self.read_csv = pandas.read_csv('OLYMPICS_athlete_events.csv')
        self.GridView(self.read_csv)

    def GridView(self, Data):
         for r in len(Data):
            for c in len(Data.columns):
                e = tk.Entry(self)
                e.insert(0, Data.iloc[r,c])
                e.grid(row=r,column=c)
        
    

minimal_canvas_size = 300, 400

# アプリケーション起動
#root = tk.Tk()
app = Application()
    