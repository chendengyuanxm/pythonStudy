import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText
import main


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.init_data()
        self.init_window()
        self.create_menu()
        self.create_widgets()

    def init_data(self):
        self.progress_text = StringVar(value='0/1')

    def init_window(self):
        root.title = '医药数据处理'
        width = 500
        height = 500
        # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)

    def create_menu(self):
        menu_bar = Menu(root)

        menu1 = Menu(root)
        menu1.add_command(label='保存')
        menu1.add_command(label='退出')

        menu2 = Menu(root)
        menu2.add_command(label='复制')
        menu2.add_command(label='粘贴')

        menu_bar.add_cascade(label='文件', menu=menu1)
        menu_bar.add_cascade(label='编辑', menu=menu2)
        root.config(menu=menu_bar)

    def create_widgets(self):
        l_console = Label(self, text='输出:')
        l_console.grid(row=0, column=0, sticky='w')

        self.console = ScrolledText(self, bg='white', height=30)
        # console.insert(END, __doc__)
        # console.pack(fill=BOTH, side=LEFT, expand=True)
        self.console.focus_set()
        self.console.grid(row=1, rowspan=10, column=0, columnspan=5)

        self.progress = tk.Label(self, textvariable=self.progress_text)
        self.progress.grid(row=11, sticky='w')

        start = tk.Button(self, text="运行", padx=20, command=self.process)
        start.grid(row=12, column=0, pady=30)

        b_clear = tk.Button(self, text="清除", padx=20, command=self.clear)
        b_clear.grid(row=12, column=1, pady=30)

        back = tk.Button(self, text="退出", padx=20, command=self.master.destroy)
        back.grid(row=12, column=2, pady=30)

    def process(self):
        self.console_log('开始运行...')
        main.start_work(self)
        # showinfo(title='信息', message='运行成功！')

    def clear(self):
        self.console.delete(1.0, END)

    def update_progress(self, count, total):
        self.progress_text.set('%s/%s' % (count, total))
        root.update_idletasks()

    def console_log(self, log):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        f_log = '%s %s \n' % (current_time, log)
        self.console.insert(END, f_log)


root = tk.Tk()
app = Application(master=root)
app.mainloop()


