import tkinter as tk
import tkinter.messagebox
import re


def main():
    flag = True
    top = tk.Tk()
    top.geometry('450x640')
    contentVar = tk.StringVar(top, '')
    operators = ('+', '-', '*', '/', )

    def input_num(btn):
        content = contentVar.get()
        if btn in '0123456789':
            content += btn
        elif btn in operators:
            content = content + str(btn)
        elif btn == 'AC':
            content = ''
        elif btn == '=':
            content = str(eval(content))
        contentVar.set(content)

    top.title('Caculator')
    contentEntry = tk.Entry(top, textvariable=contentVar)
    contentEntry['state'] = 'readonly'
    contentEntry.grid(row=0, rowspan=2, columnspan=3, sticky='E')

    # E1 = tk.Entry(top)
    # E1.grid(row=0, column=3)
    button1 = tk.Button(top, text='1', activeforeground='black', fg='red', height='5', highlightcolor='green',
                        width='10', command=lambda: input_num('1'))
    button1.grid(row=2, column=0)
    button2 = tk.Button(top, text='2', height='5', activeforeground='black', fg='red', width='10',
                        command=lambda: input_num('2'))
    button2.grid(row=2, column=1)
    button3 = tk.Button(top, text='3', height='5', activeforeground='black', fg='red', width='10',
                        command=lambda: input_num('3'))
    button3.grid(row=2, column=2)
    button4 = tk.Button(top, text='4', height='5', activeforeground='black', fg='red', width='10',
                        command=lambda: input_num('4'))
    button4.grid(row=3, column=0)
    button5 = tk.Button(top, text='5', height='5', activeforeground='black', fg='red', width='10',
                        command=lambda: input_num('5'))
    button5.grid(row=3, column=1)
    button6 = tk.Button(top, text='6', height='5', activeforeground='black', fg='red', width='10',
                        command=lambda: input_num('6'))
    button6.grid(row=3, column=2)
    button7 = tk.Button(top, text='7', height='5', activeforeground='black', fg='red', width='10',
                        command=lambda: input_num('7'))
    button7.grid(row=4, column=0)
    button8 = tk.Button(top, text='8', height='5', activeforeground='black', fg='red', width='10',
                        command=lambda: input_num('8'))
    button8.grid(row=4, column=1)
    button9 = tk.Button(top, text='9', height='5', activeforeground='black', fg='red', width='10',
                        command=lambda: input_num('9'))
    button9.grid(row=4, column=2)
    button0 = tk.Button(top, text='0', height='5', activeforeground='black', fg='red', width='10',
                        command=lambda: input_num('0'))
    button0.grid(row=5, column=1)
    button_set = tk.Button(top, text='AC', height='5', activeforeground='black', fg='red', width='10',
                           command=lambda: input_num('AC'))
    button_set.grid(row=5, column=0)
    button_equal = tk.Button(top, text='=', height='5', activeforeground='black', fg='red', width='10',
                             command=lambda: input_num('='))
    button_equal.grid(row=5, column=2)
    button_plus = tk.Button(top, text='+', height='5', activeforeground='black', fg='red', width='10',
                            command=lambda: input_num('+'))
    button_plus.grid(row=2, column=3)
    button_sub = tk.Button(top, text='-', height='5', activeforeground='black', fg='red', width='10',
                           command=lambda: input_num('-'))
    button_sub.grid(row=3, column=3)
    button_mul = tk.Button(top, text='*', height='5', activeforeground='black', fg='red', width='10',
                           command=lambda: input_num('*'))
    button_mul.grid(row=4, column=3)
    button_div = tk.Button(top, text='/', height='5', activeforeground='black', fg='red', width='10',
                           command=lambda: input_num('/'))
    button_div.grid(row=5, column=3)
    tk.mainloop()


if __name__ == '__main__':
    main()
