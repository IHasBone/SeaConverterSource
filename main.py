import tkinter as tk

root = tk.Tk()
root.title("Sea Converter")
root.iconbitmap('./clock.ico')


canvas = tk.Canvas(root, height=700, width=700, bg="white")
canvas.pack()

text1 = tk.Label(root, text="Knots", bg="white")
text1.place(relwidth=0.1, relheight=0.05, relx=0.1, rely=0.05)

speed = tk.Entry(root, bg="yellow")
speed.place(relwidth=0.1, relheight=0.05, relx=0.1, rely=0.1)

text2 = tk.Label(root, text="Nautical Miles", bg="white", font=('TkDefaultFont', 8))
text2.place(relwidth=0.1, relheight=0.05, relx=0.8, rely=0.05)

distance = tk.Entry(root, bg="yellow")
distance.place(relwidth=0.1, relheight=0.05, relx=0.8, rely=0.1)

text3 = tk.Label(root, text="Hours", bg="white")
text3.place(relwidth=0.1, relheight=0.05, relx=0.45, rely=0.75)

time = tk.Entry(root, bg="yellow")
time.place(relwidth=0.1, relheight=0.05, relx=0.45, rely=0.8)


def clear_numbers():
    time.delete(0, len(time.get()))
    distance.delete(0, len(distance.get()))
    speed.delete(0, len(speed.get()))


def convert():
    if speed.get() != "" and distance.get() != "" and time.get() == "":
        answer = float(distance.get()) / float(speed.get())
        time.insert(0, answer)
    elif speed.get() == "" and distance.get() != "" and time.get() != "":
        answer = float(distance.get()) / float(time.get())
        speed.insert(0, answer)
    elif speed.get() != "" and distance.get() == "" and time.get() != "":
        answer = float(speed.get()) * float(time.get())
        distance.insert(0, answer)


convert = tk.Button(root, text="Convert", padx=10, pady=5, fg="white", bg="#263D42", command=convert, activebackground="#263D42", activeforeground="white")
convert.pack()

clear_all = tk.Button(root, text="Clear all numbers", padx=10, pady=5, fg="white", bg="#263D42", command=clear_numbers, activebackground="#263D42", activeforeground="white")
clear_all.pack()

root.mainloop()
