import tkinter

pnum = 0
def photograph():
    global pnum
    canvas.delete("PH")
    canvas.create_image(400,300, image=photo[pnum], tag="PH")
    pnum += 1
    if pnum >= len(photo):
        pnum = 0
    root.after(3000, photograph)
    
root = tkinter.Tk()
root.title("Degital PhotoFlame")
canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()
photo = [
    tkinter.PhotoImage(file="imgs/01.png"),
    tkinter.PhotoImage(file="imgs/02.png"),
    tkinter.PhotoImage(file="imgs/03.png"),
    tkinter.PhotoImage(file="imgs/04.png"),
    tkinter.PhotoImage(file="imgs/05.png"),
    tkinter.PhotoImage(file="imgs/06.png"),
    tkinter.PhotoImage(file="imgs/07.png"),
    tkinter.PhotoImage(file="imgs/08.png"),
    tkinter.PhotoImage(file="imgs/09.png"),
    tkinter.PhotoImage(file="imgs/10.png"),
    tkinter.PhotoImage(file="imgs/11.png"),
    tkinter.PhotoImage(file="imgs/12.png"),
    tkinter.PhotoImage(file="imgs/13.png"),
    tkinter.PhotoImage(file="imgs/14.png"),
    tkinter.PhotoImage(file="imgs/15.png"),
    tkinter.PhotoImage(file="imgs/16.png"),
    tkinter.PhotoImage(file="imgs/rabit.png"),
]
photograph()
root.mainloop()