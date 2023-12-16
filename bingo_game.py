from tkinter import *
from tkinter import ttk
import numpy as np
import random

def output(*args):
   results = machine.output()
   global output_ball
   output_ball.set('今回の出力 : ' + str(results[0]))
   global output_balls_v
   try:
       output_balls.set('前回の出力：' + str(results[1][-2]))
       print(results[1])
   except Exception as e:
       pass
   
#カード生成
def card_generate(*args):
   try:
        card = BingoCard()
        globals()[card.player_name] = card.generate_card()
        print(globals()[card.player_name])

   except Exception as e:
       print(e)



class BingoMachine:

   '''
       BingoMachineクラス
       1～75までの数字のボールをクリックされる度にランダムで出力する
       出力済の数字をリスト形式で併せて還元する
   '''

   #コンストラクタ
   def __init__(self):
       self.balls = [i for i in range(1,76)]
       self.balls_output = []

   #ボール出力メソッド
   def output(self):
       output_ball = random.choice(self.balls)
       self.balls_output.append(output_ball)
       outputs = [output_ball, self.balls_output]
       self.balls.remove(output_ball)
       print(len(self.balls))
       
       return  outputs
       

class BingoCard:

   '''
       Bingoカードクラス
       1～15、16～30、31~45、46～60、61～75の範囲から5つ数字を選択し、
       5×5の多重リストを作成するとともに、サブウインドウを作成する
   '''
   #コンストラクタ
   def __init__(self):
       self.card = []

   #カード生成機能
   def generate_card(self):
       numbers = []
       card_numbers = []
       upper = 16
       under = 1

       #サブウインドウ作成
       window_name = "bingo"
       print(window_name)
       globals()[window_name] = Toplevel()
       globals()[window_name].title(window_name)
       globals()[window_name].geometry("460x475")

       #card_frame作成
       card_frame = ttk.Frame(globals()[window_name])
       card_frame.grid(row=0, column=0, sticky=(N,W,S,E))

       while len(card_numbers) < 5:
           [numbers.append(number) for number in range(under, upper)]
           #print(numbers)
           
           card_numbers.append(np.random.choice(numbers, 5 ,replace = False))
           #print(card_numbers)
           upper += 15
           under += 15
           numbers = []
       else:
           self.card = np.array(card_numbers).T.tolist()
           self.card[2][2] = 'X'

               #button_style
       button_style = ttk.Style()
       button_style.configure("button_style.TButton", font=("Lucida Console", 18), width=6)

       #ボタンコマンド
       def hit_num(event):
           positions = event.widget.cget("text")
           event.widget.config(state=DISABLED)
       
       #5×5のマスを作成して数字を格納していく
       i = 0 #行
       j = 0 #列
       for i in range(5):
           for j in range(5):
               space_name = str(i)+str(j)
               #globals()[space_name] = ttk.Label(card_frame, text=self.card[i][j], font=("Lucida Console",24))
               globals()[space_name] = ttk.Button(
                       card_frame, text = self.card[i][j],
                       style = "button_style.TButton",
                       padding=[0, 30, 0, 30]
                   )
               globals()[space_name].bind("<ButtonPress>", hit_num)
               
               globals()[space_name].grid(column=j, row=i)


       return self.card


#ビンゴマシーン生成
machine = BingoMachine()
global output_balls
output_balls = []


#ウインドウ作成
root = Tk()
root.title("ビンゴゲーム")
root.geometry("200x260")

#bord_frame作成
bord_frame = ttk.Frame(root, style="style.TFrame")
bord_frame.grid(row=0, column=0, sticky=(N, W, S, E))

#人数入力欄
# player_num_label = ttk.Label(bord_frame, text="プレイヤー人数を入力", font=("Lucida Console",12))
# player_num_label.grid(column=0, row=2, sticky=(N, W, E, S), ipadx= 5, ipady = 5,padx=5, pady=5)
# player_num = StringVar()
# player_num_entry = ttk.Entry(bord_frame, width=2, textvariable=player_num, font=("Lucida Console",12))
# player_num_entry.grid(column=0, row=3, sticky=(N, W, E, S),ipadx = 5, ipady=5,padx=5, pady=5)

# 出力されたボールの番号表示欄
global output_ball
output_ball = StringVar()
output_ball_label = ttk.Label(bord_frame, textvariable = output_ball, font=("Lucida Console",12))
output_ball_label.grid(column=0, row=6, sticky=(N,W,E,S), ipadx = 5, ipady = 5, padx = 5, pady=5)

#出力済のボール一覧の表示欄
output_balls = StringVar(value=output_balls)
output_balls = StringVar()
output_balls_label = ttk.Label(bord_frame, textvariable=output_balls, font=("Lucida Console",12))
output_balls_label.grid(column=0, row=7, sticky=(N, W, E, S), ipadx = 5, ipady = 5, padx = 5, pady=5)

#開始ボタン
start_button = ttk.Button(bord_frame, text="カード作成", command=card_generate)
start_button.grid(column=0, row=4, sticky=(N, W, E, S),ipadx = 10, ipady = 5,padx=5, pady=5)

#ボール出力ボタン
ball_button = ttk.Button(bord_frame, text="ボ―ル出力", command=output)
ball_button.grid(column=0, row=5, sticky=(N, W, E, S), ipadx = 10, ipady = 5,padx=5, pady=5)
card_generate()
root.mainloop()
