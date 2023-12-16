from tkinter import *
from tkinter import ttk
import random

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
       