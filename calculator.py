from tkinter import *
import math

first = None
opp = None

# ---------- logic ----------
def get_digit(d):
    cur = result_label['text']
    if cur == '0':
        result_label.config(text=str(d))
    else:
        result_label.config(text=cur + str(d))

def add_decimal():
    cur = result_label['text']
    if '.' not in cur:
        result_label.config(text=cur + '.' if cur else '0.')

def clear():
    global first, opp
    first = opp = None
    result_label.config(text='')

def delete():
    result_label.config(text=result_label['text'][:-1])

def operator(op):
    global first, opp
    if result_label['text'] == '':
        return
    first = float(result_label['text'])
    opp = op
    result_label.config(text='')

def equal():
    global first, opp
    if first is None or result_label['text'] == '':
        return

    second = float(result_label['text'])

    try:
        if opp == '+': result = first + second
        elif opp == '-': result = first - second
        elif opp == '*': result = first * second
        elif opp == '/': result = first / second
        elif opp == '^': result = first ** second

        format_result(result)
    except:
        result_label.config(text='Error')

def scientific(func):
    try:
        x = float(result_label['text'])
        if func == 'sqrt': result = math.sqrt(x)
        elif func == 'square': result = x ** 2
        elif func == 'sin': result = math.sin(math.radians(x))
        elif func == 'cos': result = math.cos(math.radians(x))
        elif func == 'tan': result = math.tan(math.radians(x))
        elif func == 'log': result = math.log10(x)
        elif func == 'ln': result = math.log(x)

        format_result(result)
    except:
        result_label.config(text='Error')

def constant(val):
    format_result(val)

def format_result(res):
    text = f"{res:.6f}".rstrip('0').rstrip('.')
    result_label.config(text=text)

# ---------- UI ----------
root = Tk()
root.title('Scientific Calculator')
root.geometry('320x385')
root.resizable(False, False)
root.configure(bg='black')

result_label = Label(
    root, text='0', bg='#141414', fg='white',
    anchor='e', padx=10,
    font=('Helvetica', 24,'bold')
)
result_label.grid(row=0, column=0, columnspan=5, pady=15, sticky='we')

btn_cfg = {
    'width': 6,
    'height': 2,
    'bg': '#1c1c1e',
    'fg': 'white',
    'font': ('Helvetica', 13)
}

# ---------- Scientific buttons ----------
Button(text='sin', command=lambda: scientific('sin'), **btn_cfg).grid(row=1, column=0)
Button(text='cos', command=lambda: scientific('cos'), **btn_cfg).grid(row=1, column=1)
Button(text='tan', command=lambda: scientific('tan'), **btn_cfg).grid(row=1, column=2)
Button(text='√', command=lambda: scientific('sqrt'), **btn_cfg).grid(row=1, column=3)
Button(text='x²', command=lambda: scientific('square'), **btn_cfg).grid(row=1, column=4)

Button(text='log', command=lambda: scientific('log'), **btn_cfg).grid(row=2, column=0)
Button(text='ln', command=lambda: scientific('ln'), **btn_cfg).grid(row=2, column=1)
Button(text='π', command=lambda: constant(math.pi), **btn_cfg).grid(row=2, column=2)
Button(text='^', command=lambda: operator('^'), **btn_cfg).grid(row=2, column=3)
Button(text='DEL', command=delete, **btn_cfg).grid(row=2, column=4)

# ---------- Numbers ----------
Button(text='7', command=lambda: get_digit(7), **btn_cfg).grid(row=3, column=0)
Button(text='8', command=lambda: get_digit(8), **btn_cfg).grid(row=3, column=1)
Button(text='9', command=lambda: get_digit(9), **btn_cfg).grid(row=3, column=2)

Button(text='4', command=lambda: get_digit(4), **btn_cfg).grid(row=4, column=0)
Button(text='5', command=lambda: get_digit(5), **btn_cfg).grid(row=4, column=1)
Button(text='6', command=lambda: get_digit(6), **btn_cfg).grid(row=4, column=2)

Button(text='1', command=lambda: get_digit(1), **btn_cfg).grid(row=5, column=0)
Button(text='2', command=lambda: get_digit(2), **btn_cfg).grid(row=5, column=1)
Button(text='3', command=lambda: get_digit(3), **btn_cfg).grid(row=5, column=2)

Button(text='0', command=lambda: get_digit(0), **btn_cfg).grid(row=6, column=1)
Button(text='.', command=add_decimal, **btn_cfg).grid(row=6, column=2)
Button(text='AC', command=clear, **btn_cfg).grid(row=6, column=0)

# ---------- Operators ----------
Button(text='+', command=lambda: operator('+'), **btn_cfg).grid(row=3, column=3)
Button(text='-', command=lambda: operator('-'), **btn_cfg).grid(row=4, column=3)
Button(text='*', command=lambda: operator('*'), **btn_cfg).grid(row=5, column=3)
Button(text='/', command=lambda: operator('/'), **btn_cfg).grid(row=6, column=3)

Button(text='=', command=equal, **btn_cfg).grid(
    row=3, column=4, rowspan=4, sticky='ns'
)

root.mainloop()
