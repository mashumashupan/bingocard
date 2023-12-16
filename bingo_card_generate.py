#tkinterおよびttkをインポート
from tkinter import *
from tkinter import ttk

import numpy as np
import random

class BingoCard:

   '''
       Bingoカードクラス
       1～15、16～30、31~45、46～60、61～75の範囲から5つ数字を選択し、
       5×5の多重リストを作成するとともに、サブウインドウを作成する
   '''
   #コンストラクタ
   def __init__(self):
       self.player_name = input("プレイヤー名を入力してください：")
       self.card = []

   #カード生成機能
   def generate_card(self):
       numbers = []
       card_numbers = []
       upper = 16
       under = 1

       #サブウインドウ作成
       window_name = self.player_name
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