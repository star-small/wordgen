from tkinter import *
from words_gen import *
import words_gen

def gen():
    try:
        text['fg'] = 'white'


        if b_var.get() == 0:
            x = int(num.get())
            ending = form.get()
            word = consonant(x, ending)
            print(word)
            text["text"] = word.upper()
        elif b_var.get() == 1:
            x = int(num.get())
            ending = form.get()
            word = vowel(x, ending)
            print(word)
            text["text"] = word.upper()

    except ValueError:
        text["text"] = 'Введите числово!'
        text["fg"] = 'red'

def update():
    words_gen.list_consonant = arr1_form.get().split(' ')
    words_gen.list_vowel = arr2_form.get().split(' ')
    print(words_gen.list_consonant)
    print(words_gen.list_vowel)
root = Tk()



root.title("Word generator")
root.configure(padx=3, pady=3)
root.minsize(width=500, height=300)
root.maxsize(width=900, height=300)
root.configure(background='#242424')

root.columnconfigure(0, weight=1)
text = Label(root, highlightthickness=3, highlightbackground="#141414",  font='Ubuntu 45', text='Generator', borderwidth=2, relief='ridge', bg="#1c1c1c", fg="white")
text.grid(row=0, column=0, columnspan=3)
text_count = Label(root, bg="#242424", fg="white", text="choose length: ").grid(row=1, column=0, sticky=E)
num = Spinbox(root, highlightthickness=2, highlightbackground="#141414",  width=7, from_=1, to=10, bg="#242424", fg="white")
num.grid(row=1, column=1, sticky=W)

last_word = Label(root, bg="#242424", fg="white", text="Enter last word").grid(row=2, column=0, sticky=E)
form = Entry(root, highlightthickness=2, highlightbackground="#141414", bg="#242424", fg="white")
form.grid(row=2, column=1, sticky=W)

arr1 = Label(root, bg="#242424", fg="white", text="variant 1").grid(row=2, column=0, sticky=W)
arr1_form = Entry(root, highlightthickness=2, highlightbackground="#141414", bg="#242424", fg="white")
arr1_form.grid(row=3, column=0, sticky=W)


arr2 = Label(root, bg="#242424", fg="white", text="variant 2").grid(row=4, column=0, sticky=W)
arr2_form = Entry(root, highlightthickness=2, highlightbackground="#141414", bg="#242424", fg="white")
arr2_form.grid(row=5, column=0, sticky=W)
btn_update = Button(root, highlightthickness=2, highlightbackground="#141414", bg="#242424", fg="white", text='Update', command=update)
btn_update.grid(row=6, column=0, sticky=W)


b_var = IntVar()
b_var.set(0)

r1 = Radiobutton(root, highlightthickness=1, highlightbackground="#141414", text="variant 1", variable=b_var, value=0)
r2 = Radiobutton(root, highlightthickness=1, highlightbackground="#141414", text='variant 2', variable=b_var, value=1)
r1.grid(row=3, column=1, sticky=E)
r2.grid(row=3, column=2, sticky=W)
btn = Button(root, highlightthickness=2, highlightbackground="#141414", bg="#242424", fg="white", text='Generate!', command=gen).grid(row=3, column=0, columnspan=3)
text["fg"] = 'white'
root.mainloop()