import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("名簿作成")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
names = []
# ↑↑↑ お約束のコード ↑↑↑


def name():
    names.append(entry1.get())
    name_out = ""
    for i in names:
        name_out += f"{i}\n"
    label1.config(text=f"{name_out}\n")


# 入力フィールドの作成
label2 = tk.Label(window, text="名前を入力してください", bg=bg_color, fg=fg_color)
label2.pack()
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)


# ボタンの作成
button1 = tk.Button(window, text="追加", command=name)
button1.pack(pady=10)


# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
