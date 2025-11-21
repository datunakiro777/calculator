from tkinter import *

def add_text(value):
    current_text = output_label.cget('text')
    new_text = current_text + value
    print(new_text)
    output_label.config(text=new_text)
    
def equal():
    text = output_label.cget('text')
    if '+' in text:
        numbers = text.split('+')
        answer = int(numbers[0]) + int(numbers[1])
        output_label.config(text=str(answer))
    elif '-' in text:
        numbers = text.split('-')
        answer = int(numbers[0]) - int(numbers[1])
        output_label.config(text=str(answer))
    elif '/' in text:
        numbers = text.split('/')
        if numbers[1] == '0':
            output_label.config(text='ERROR')
        answer = int(numbers[0]) / int(numbers[1])
        output_label.config(text=str(answer))
    elif '*' in text:
        numbers = text.split('*')
        answer = int(numbers[0]) * int(numbers[1])
        output_label.config(text=str(answer))
    elif '^2' in text:
        numbers = text.split('^2')
        answer = int(numbers[0]) ** 2
        output_label.config(text=str(answer))
    elif '^3' in text:
        numbers = text.split('^3')
        answer = int(numbers[0]) ** 3
        output_label.config(text=str(answer))

def clear_text():
    output_label.config(text='')



window = Tk()
window.title('calculator')

output_label = Label(window, text='', fg='grey')
add_button = Button(window , text='+', fg='black', activebackground='grey', padx=20, pady=20, command=lambda: add_text('+'))
subtract_button = Button(window , text='-', fg='black', activebackground='grey', padx=20, pady=20, command=lambda: add_text('-'))
divide_button = Button(window , text='/', fg='black', activebackground='grey', padx=20, pady=20, command=lambda: add_text('/'))
multiply_button = Button(window, text='*', fg='black', activebackground='grey', padx=20, pady=20, command=lambda: add_text('*'))
square_button = Button(window, text='^2', fg='black', activebackground='grey', padx=20, pady=20, command=lambda: add_text('^2'))
cube_button = Button(window, text='^3', fg='black', activebackground='grey', padx=20, pady=20, command=lambda: add_text('^3'))
equal_button = Button(window, text='=', fg='black', activebackground='grey', padx=20, pady=20, command=equal)
clear_button = Button(window, text='clear', fg='black', activebackground='grey', padx=20, pady=20, command=clear_text)

button1 = Button(window, text='1', fg='black', activebackground='grey', padx=20, pady=20, command=lambda: add_text('1'))
button2 = Button(window, text='2', fg='black', activebackground='grey', padx=20, pady=20, command=lambda: add_text('2'))
button3 = Button(window, text='3', fg='black', activebackground='grey', padx=20, pady=20, command=lambda: add_text('3'))
button4 = Button(window, text='4', fg='black', activebackground='grey', padx=20, pady=20, command=lambda: add_text('4'))
button5 = Button(window, text='5', fg='black', activebackground='grey', padx=20, pady=20, command=lambda: add_text('5'))
button6 = Button(window, text='6', fg='black', activebackground='grey', padx=20, pady=20, command=lambda: add_text('6'))
button7 = Button(window, text='7', fg='black', activebackground='grey', padx=20, pady=20, command=lambda: add_text('7'))
button8 = Button(window, text='8', fg='black', activebackground='grey', padx=20, pady=20, command=lambda: add_text('8'))
button9 = Button(window, text='9', fg='black', activebackground='grey', padx=20, pady=20, command=lambda: add_text('9'))
button0 = Button(window, text='0', fg='black', activebackground='grey', padx=20, pady=20, command=lambda: add_text('0'))

output_label.grid(row=0, columnspan=4)
add_button.grid(row=1, column=0)
subtract_button.grid(row=1, column=1)
divide_button.grid(row=1, column=2)
multiply_button.grid(row=1, column=3)
square_button.grid(row=2, column=3)
cube_button.grid(row=3, column=3)
equal_button.grid(row=4, column=3)
clear_button.grid(row=5, column=3)

button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)
button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button7.grid(row=4, column=0)
button8.grid(row=4, column=1)
button9.grid(row=4, column=2)
button0.grid(row=5, column=1)


window.mainloop()