import tkinter as tk

# dictionary with couples
btn_dict = {
    'inch' : 'inch to cm',
    'mile' : 'mile to km',
    'pound': 'pound to kg',
    'ounce': 'ounce to gram'
}

# reverse values dictionary
btn_reverse_dict = {
    'cm' : 'cm to inch',
    'km' : 'km to mile',
    'kg': 'kg to pound',
    'gram': 'gram to ounce'
}

lenght = len(btn_dict)    # used for columnspan geometry
couple = ''

def choose_couple():
    # returns the exchange value couple by clicking on the button
    global couple
    couple = choice.get()
    return couple

def click():
    # shows converted values
    global couple
    input_value = insert_value.get()
    output.delete(0.0, 'end')
    if couple in btn_dict.keys() or couple in btn_reverse_dict:
        try:
            if couple == 'inch':
                result = float(input_value) * 2.54
            elif couple == 'mile':
                result = float(input_value) * 1.609344
            elif couple == 'pound':
                result = float(input_value) * 0.45359237
            elif couple == 'ounce':
                result = float(input_value) * 28.3495231
            elif couple == 'cm':
                result = float(input_value) / 2.54    # reverse
            elif couple == 'km':
                result = float(input_value) / 1.609344    # reverse
            elif couple == 'kg':
                result = float(input_value) / 0.45359237    # reverse
            elif couple == 'gram':
                result = float(input_value) / 28.3495231    # reverse
        except:
            result = 'input must be a number'    # not yet raising error for negative numbers!!!
    else:
        result = 'no choice to convert'
    output.insert('end', result)

def close_window():
    window.destroy()
    exit()

window = tk.Tk()

window.title('Converter')
window.geometry('560x460')
window.configure(background='light yellow')

photo = tk.PhotoImage(file='converter.png')
lbl_photo = tk.Label(window, image=photo)
lbl_photo.grid(row=0, column=1, rowspan=lenght)

choice = tk.StringVar(window)

# two for loops for two columns
for (value, text) in btn_dict.items():
    tk.Radiobutton(window, text=text, value=value, variable=choice, width=20, background='light blue',
        indicator=0, command=choose_couple).grid(row=list(btn_dict.keys()).index(value), column=0, 
        padx=10, pady=10, sticky='w')

for (value, text) in btn_reverse_dict.items():
    tk.Radiobutton(window, text=text, value=value, variable=choice, width=20, background='light blue',
        indicator=0, command=choose_couple).grid(row=list(btn_reverse_dict.keys()).index(value), 
         padx=10, pady=10, column=2, sticky='e')

# text label
lbl_value = tk.Label(window, text='insert value you want to convert:', bg='light pink', font='Arial 10')
lbl_value.grid(row=lenght+1, column=1, padx=10, pady=10)

# insert value window
insert_value = tk.Entry(window, width=10, font='Arial 12 bold', bg='light grey')
insert_value.grid(row=lenght+2, column=1, padx=10, pady=10)

# submit button
submit_btn = tk.Button(window, text='CONVERT', font='Arial 12 bold', width=10, fg='red', command=click)
submit_btn.grid(row=lenght+3, column=1,padx=10, pady=10)

# output window
output = tk.Text(window, width=10, height=1.5, bg='light pink', font='Arial 17')
output.grid(row=lenght+4, column=1, padx=10, pady=20)

# exit button
btn_exit = tk.Button(window, text='exit', width=10, fg='dark grey', command=close_window)
btn_exit.grid(row=lenght+5, column=2, padx=0, pady=10)

window.mainloop()