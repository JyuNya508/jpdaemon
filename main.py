import sys
import tkinter as tk
import tftpy_server
import subprocess

btn_start_flag = 0

def btn_start_pushed():
    global btn_start_flag
    global prs_tftp
    #flag = 0の場合は起動させる
    if btn_start_flag == 0:
        btn_start["text"] = '停止\n[現在起動中]'
        btn_start["image"] = icon_stop
        btn_start_flag = 1
        prs_tftp = subprocess.Popen(['python','tftpy_server.py','-i','192.168.0.39','-r','C:\\subversion'],shell=False)
    #flag = 1の場合は停止させる
    else:
        btn_start["text"] = '起動\n[現在停止中]'
        btn_start["image"] = icon_start
        btn_start_flag = 0
        prs_tftp.terminate()
def select():
    pass
def endofapp():
    sys.exit()

#変数



root = tk.Tk()
root.title("JPDaemon")
root.geometry("640x480")
iconfile = 'icon/favicon.ico'
root.iconbitmap(default=iconfile)

#サッシの作成
#pw_main = tk.PanedWindow(root, orient='horizontal')
#pw_main.grid(column=100, row=100)

#pw_left = tk.PanedWindow(pw_main,orient='vertical',bg='cyan',width=200)
#pw_right = tk.PanedWindow(pw_main,orient='vertical',bg='red',width=200)
#pw_main.add(pw_left)
#pw_main.add(pw_right)

#メニューバー
menubar = tk.Menu(root)

root.config(menu = menubar)

menu_file = tk.Menu(root)
menu_view = tk.Menu(root)
menu_help = tk.Menu(root)

menubar.add_cascade(label='ファイル',menu = menu_file)
menubar.add_cascade(label='ビュー',menu = menu_view)
menubar.add_cascade(label='ヘルプ',menu = menu_help)

menu_file.add_command(label='選択したサーバーの設定変更', command=select)
menu_file.add_command(label='選択したサービスの開始/終了', command=select)
menu_file.add_separator()
menu_file.add_command(label='終了', command=endofapp)

menu_help.add_command(label='JPDaemonについて', command=select)

#ボタンのフレーム配置
frame1 = tk.Frame(root,bg='sky blue',height=480,width=120)
frame1.place(x=0,y=0)

#実際のボタン配置
#画像の取り込み
icon_config = tk.PhotoImage(file='icon/ico_config.png')
icon_start = tk.PhotoImage(file='icon/ico_start.png')
icon_stop = tk.PhotoImage(file='icon/ico_stop.png')

#画像の縮小
icon_config = icon_config.subsample(4)
icon_start = icon_start.subsample(4)
icon_stop = icon_stop.subsample(4)


btn_config = tk.Button(
    frame1,
    image=icon_config,
    text='設定変更',
    compound=tk.TOP
)
btn_start = tk.Button(
    frame1,
    image=icon_start,
    text='起動\n[現在停止中]',
    compound=tk.TOP,
    command=btn_start_pushed
)
btn_config.place(x=30,y=20)
btn_start.place(x=20,y=100)


#bu = tk.Button(root, text="ボタン", command=pushed)
#bu.grid()

#ステータスバー
#status_bar = tk.Label(root, text="For Help,press F1", borderwidth=1, relief="groove")
#status_bar.place(x=0,y=460,width=640)


#------暫定的な終了処理-------
def syori():
    prs_tftp.terminate()
import atexit
atexit.register(syori)



root.mainloop()

