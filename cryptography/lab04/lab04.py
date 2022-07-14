import tkinter as tk
from random import choice
from bitarray import bitarray
import tkinter.messagebox as msg

rejestr1 = []
rejestr2 = []
rejestr3 = []
output = []


def wyswietl():
    w = ''
    for i in range(len(output)):
        if output[i] == True:
            w += "1"
        else:
            w += "0"

    print(w)


def generate(dlugoscBita=None):
    try:
        output.clear()
        if dlugoscBita is None:
            dlugoscBita = int(out_length_entry.get())
        if (dlugoscBita <= 0):
            msg.showerror("Błąd", "Długosc musi byc wieksza niz 0")
        funkcja1 = bitarray(lfsr1func.get())
        freeterm1 = bitarray(lfsr1free.get())
        funkcja2 = bitarray(lfsr2func.get())
        freeterm2 = bitarray(lfsr2free.get())
        funkcja3 = bitarray(lfsr3func.get())
        freeterm3 = bitarray(lfsr3free.get())
        rejestr1 = bitarray(lfsr1register.get())
        rejestr2 = bitarray(lfsr2register.get())
        rejestr3 = bitarray(lfsr3register.get())

        if (len(funkcja1) == int(lfsr1length.get()) and len(funkcja2) == int(lfsr2length.get()) and len(
                funkcja3) == int(lfsr3length.get())):
            print("")
        else:
            msg.showerror("Error", "Zla dlugosc funkcji")
            pass

        if (len(rejestr1) == len(funkcja1) and len(rejestr2) == len(funkcja2) and len(rejestr3) == len(funkcja3)):
            print("")
        else:
            msg.showerror("Błąd", "Zła dlugosc")
            pass

        if typGeneratora.curselection()[0] == 0:
            for i in range(0, dlugoscBita):
                a1 = (freeterm1[0])
                a2 = (freeterm2[0])
                a3 = (freeterm3[0])
                for j in range(0, len(funkcja1)):
                    if funkcja1[j]:
                        a1 = a1 ^ rejestr1[j]

                for k in range(0, len(funkcja2)):
                    if funkcja2[k]:
                        a2 = a2 ^ rejestr2[k]

                for l in range(0, len(funkcja3)):
                    if funkcja3[l]:
                        a3 = a3 ^ rejestr3[l]

                x1 = rejestr1.pop()
                x2 = rejestr2.pop()
                x3 = rejestr3.pop()

                rejestr1.insert(0, (a1))
                rejestr2.insert(0, (a2))
                rejestr3.insert(0, (a3))

                output.append((bool(x1) and bool(x2)) ^ (not bool(x2) and bool(x3)))

                x1 = rejestr1.pop()
                rejestr1.insert(0, (a1))

                x2 = rejestr2.pop()
                rejestr2.insert(0, (a2))

                if x1:
                    output.append(bool((x2)))

        wyswietl()

    except Exception:
        msg.showerror("Błąd", "Błąd")
        return




def ustaw1():
    length = int(lfsr1length.get())
    lfsr1func.delete(0, 'end')
    lfsr1register.delete(0, 'end')
    lfsr1func.insert(0, losowanie(length))
    lfsr1register.insert(0, losowanie(length))


def ustaw2():
    length = int(lfsr2length.get())
    lfsr2func.delete(0, 'end')
    lfsr2register.delete(0, 'end')
    lfsr2func.insert(0, losowanie(length))
    lfsr2register.insert(0, losowanie(length))


def ustaw3():
    length = int(lfsr3length.get())
    lfsr3func.delete(0, 'end')
    lfsr3register.delete(0, 'end')
    lfsr3func.insert(0, losowanie(length))
    lfsr3register.insert(0, losowanie(length))


def losowanie(length):
    mozliwe = ["0", "1"]
    temp = ''
    for i in range(int(length)):
        temp += choice(mozliwe)

    return temp


master = tk.Tk()
master = master
master.minsize(600, 400)
master.title("Generator liczb")
label1 = tk.Label(master, text="Dlugosc  funkcji/rejestru:")
label2 = tk.Label(master, text="Wyraz wolny funkcja:")
label3 = tk.Label(master, text="Zawartosc rejestru:")
label1.place(x=25, y=5)
label2.place(x=225, y=5)
label3.place(x=425, y=5)

lfsr1label = tk.Label(master, text="LFSR1")
lfsr1label.place(x=25, y=55)
lfsr1length = tk.Entry(master)
lfsr1length.insert(0, "10")
lfsr1length.place(x=75, y=55, width=35, height=25)
lfsr1set = tk.Button(master=master, text="Ustaw", command=ustaw1)  # dodaj command
lfsr1set.place(x=120, y=55, width=50, height=25)
lfsr1fxlabel = tk.Label(master, text="f(x1)")
lfsr1fxlabel.place(x=200, y=55)
lfsr1free = tk.Entry(master)
lfsr1free.insert(0, "0")
lfsr1free.place(x=235, y=55, width=15, height=25)
lfsr1func = tk.Entry(master)

lfsr1func.insert(0, losowanie(lfsr1length.get()))
lfsr1func.place(x=260, y=55, width=140, height=25)
lfsr1register = tk.Entry(master)

lfsr1register.insert(0, losowanie(lfsr1length.get()))
lfsr1register.place(x=425, y=55, width=140, height=25)

lfsr2label = tk.Label(master, text="LFSR2")
lfsr2label.place(x=25, y=100)
lfsr2length = tk.Entry(master)
lfsr2length.insert(0, "10")
lfsr2length.place(x=75, y=100, width=35, height=25)
lfsr2set = tk.Button(master=master, text="Ustaw", command=ustaw2)  # dodaj command
lfsr2set.place(x=120, y=100, width=50, height=25)
lfsr2fxlabel = tk.Label(master, text="f(x2)")
lfsr2fxlabel.place(x=200, y=100)
lfsr2free = tk.Entry(master)
lfsr2free.insert(0, "0")
lfsr2free.place(x=235, y=100, width=15, height=25)
lfsr2func = tk.Entry(master)
lfsr2func.insert(0, losowanie(lfsr2length.get()))
lfsr2func.place(x=260, y=100, width=140, height=25)
lfsr2register = tk.Entry(master)
lfsr2register.insert(0, losowanie(lfsr2length.get()))
lfsr2register.place(x=425, y=100, width=140, height=25)
# lfsr3
lfsr3label = tk.Label(master, text="LFSR3")
lfsr3label.place(x=25, y=145)
lfsr3length = tk.Entry(master)
lfsr3length.insert(0, "10")
lfsr3length.place(x=75, y=145, width=35, height=25)
lfsr3set = tk.Button(master=master, text="Ustaw", command=ustaw3)  # dodaj command
lfsr3set.place(x=120, y=145, width=50, height=25)
lfsr3fxlabel = tk.Label(master, text="f(x3)")
lfsr3fxlabel.place(x=200, y=145)
lfsr3free = tk.Entry(master)
lfsr3free.insert(0, "0")
lfsr3free.place(x=235, y=145, width=15, height=25)
lfsr3func = tk.Entry(master)
lfsr3func.insert(0, losowanie(lfsr3length.get()))
lfsr3func.place(x=260, y=145, width=140, height=25)
lfsr3register = tk.Entry(master)
lfsr3register.insert(0, losowanie(lfsr3length.get()))
lfsr3register.place(x=425, y=145, width=140, height=25)
# select boxes
generator_label = tk.Label(master, text="Typ Generatora:")
generator_label.place(x=40, y=200)
generator_scrollbar = tk.Scrollbar(master, orient=tk.VERTICAL)
typGeneratora = tk.Listbox(master, selectmode=tk.SINGLE, yscrollcommand=generator_scrollbar.set,
                           exportselection=0)

generator_scrollbar.place(x=150, y=225, height=150)
typGeneratora.place(x=40, y=225, height=150, width=350)
typGeneratora.insert(0, "Geffe generator")
typGeneratora.configure(font=30)

out_length_label = tk.Label(master, text="Dlugosc bitów:")
out_length_label.place(x=400, y=200)
out_length_entry = tk.Entry(master)
out_length_entry.place(x=400, y=225, width=150, height=25)
out_length_entry.insert(0, "20000")
generate_button = tk.Button(master, text="Generate", command=generate)
generate_button.place(x=400, y=300, width=60, height=25)

master.mainloop()
