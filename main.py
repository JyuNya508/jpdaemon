import tkinter as tk

def pushed():
    bu["text"] = "clicked"

def select():
    pass


root = tk.Tk()
root.title("JPDaemon")
root.geometry("640x480")
iconfile = 'favicon.ico'
root.iconbitmap(default=iconfile)

#メニューバー
menubar = tk.Menu(root)

root.config(menu = menubar)

menu_file = tk.Menu(root)
menu_view = tk.Menu(root)
menu_help = tk.Menu(root)

menubar.add_cascade(label='ファイル',menu = menu_file)
menubar.add_cascade(label='ビュー',menu = menu_view)
menubar.add_cascade(label='ヘルプ',menu = menu_help)

menu_file.add_command(label='tt', command=select)
menu_file.add_command(label='tte', command=select)
menu_file.add_separator()

#ステータスバー
status_bar = tk.Label(root, text="For Help,press F1", borderwidth=1, relief="groove",anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

#ボタン
bu = tk.Button(root, text="ボタン", command=pushed)
#bu.grid()

root.mainloop()

