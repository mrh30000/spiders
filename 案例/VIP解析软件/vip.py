"""
Asdasd
"""
# 导入模块
import tkinter as tk
import requests
import re
import webbrowser

# 创建窗口
root = tk.Tk()
# 设置标题
root.title('在线观看电影')
# 设置窗体大小
root.geometry('800x300+200+200')


def show():
    num = number_int_var.get()
    html = link_va.get()
    if num == 1:
        link = 'https://jiexi.pengdouw.com/jiexi1/?url=' + html
        response = requests.get(url=link)
        show_url = re.findall('<iframe id="baiyug" scrolling="no" src="(.*?)"', response.text)[0]
        webbrowser.open(show_url)
        print(show_url)

    elif num == 2:
        link = 'https://jiexi.pengdouw.com/jiexi2/?url=' + html
        response = requests.get(url=link)
        show_url = re.findall('<iframe id="baiyug" scrolling="no" src="(.*?)"', response.text)[0]
        webbrowser.open(show_url)

    elif num == 3:
        link = 'https://jiexi.pengdouw.com/jiexi3/?url=' + html
        response = requests.get(url=link)
        show_url = re.findall('<iframe id="baiyug" scrolling="no" src="(.*?)"', response.text)[0]
        webbrowser.open(show_url)


img = tk.PhotoImage(file='img\\封面.png')
tk.Label(root, image=img).pack()


choose_frame = tk.LabelFrame(root)
choose_frame.pack(pady=10, fill='both')

tk.Label(choose_frame, text='选择接口:', font=('黑体', 20)).pack(side=tk.LEFT)
number_int_var = tk.IntVar()
number_int_var.set(1)
tk.Radiobutton(choose_frame, text='①号通用vip引擎系统【稳定通用】', variable=number_int_var, value=1).pack(side=tk.LEFT, anchor=tk.W)
tk.Radiobutton(choose_frame, text="②号通用vip多线路系统【稳定通用】", variable=number_int_var, value=2).pack(side=tk.LEFT,
                                                                                               anchor=tk.W)
tk.Radiobutton(choose_frame, text="③号通用vip引擎系统【稳定通用】", variable=number_int_var, value=3).pack(side=tk.LEFT, anchor=tk.W)

input_frame = tk.LabelFrame(root)
input_frame.pack(pady=10, fill='both')
link_va = tk.StringVar()
tk.Label(input_frame, text='播放地址:', font=('黑体', 20)).pack(side=tk.LEFT)
tk.Entry(input_frame, relief='flat', width=100, textvariable=link_va).pack(side=tk.LEFT, fill='both')

Button_frame = tk.Frame(root)
Button_frame.pack(pady=10)

tk.Button(Button_frame, text='Go点击在线解析播放', font=('微软雅黑', 15), bg='#449d44', relief='flat', width='100',
          command=show).pack()

root.mainloop()
