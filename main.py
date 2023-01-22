#ライブラリのインポート
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import math

#開発者用
name = 'Yamada'
ver = '0.0.0'
debug = True

#変数の宣言
num = '0'

#ボタンが押されたときの処理(素数判定)
def push_judge(num):
	if num.isdecimal():
		num = int(num)
		if num >= 2:
			prime = judge_num(num)
			num = str(num)
			if prime:
				print(num + 'は素数です')
			else:
				print(num + 'は素数ではありません')
		else:
			messagebox.showwarning('無効な入力', '2以上の整数を入力してください')
	else:
		messagebox.showwarning('無効な入力', '2以上の整数を入力してください')

#素数判定
def judge_num(top):
	number = math.floor(top ** (1 / 2))
	bottom = 1
	for i in range(number - 1):
		bottom += 1
		if top % bottom == 0:
			return False
	return True

#パスの設定
path = os.path.dirname(__file__)
data_path = path + '\\Data\\'

#ウィンドウの設定
app = tk.Tk()
app.title('Prime Tool')
app.geometry('300x200')
app.resizable(width = False, height = False)

#ウィンドウアイコンの設定
icon_path = data_path + 'app.ico'
app.iconbitmap(default = icon_path)
#https://ja.pngtree.com/freepng/alphabet-p-design-3d-letter_5957610.htmlより引用

#ディスプレイの作成
disp = tk.Label(app, text = num, font = ('MSゴシック', '40', 'bold'))
disp.pack(anchor = 'ne')

#注意書きの作成
attn = tk.Label(app, text = '任意の2以上の整数を入力してください')
attn.pack(anchor = 'n')

#下のフレームの作成
frame_bottom = tk.Frame(app)
frame_bottom.pack(fill = 'x', side = 'bottom', anchor = 's')

#作者の表記
author = tk.Label(frame_bottom, text = 'Created by ' + name)
author.pack(side = 'left')

#バージョンの表記
version = tk.Label(frame_bottom, text = 'Ver.' + ver)
version.pack(side = 'right')

#ボタンの作成(素数判定)
judge = ttk.Button(app, text = '判定', command = lambda:push_judge(num))
judge.pack()

#ディスプレイの更新
def update_disp(mode, char):
	global num
	if mode == 'update':
		num = char
	elif mode == 'add':
		num += char
	elif mode == 'delete':
		num = num[:-1]
	disp.config(text = num)

#入力確認
def key_check(key):
	enter = key.keysym
	if enter.isdecimal():
		if num == '0':
			update_disp('update', enter)
		else:
			update_disp('add', enter)
	elif enter == 'BackSpace':
		update_disp('delete', None)

#キーボード入力の受け取り
app.bind("<KeyPress>", key_check)

#メインループ
app.mainloop()