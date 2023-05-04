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
    tkinter.PhotoImage(file="NonRealTime/sakura.png"),
    tkinter.PhotoImage(file="NonRealTime/heart.png"),
    tkinter.PhotoImage(file="NonRealTime/jikan.png"),
    tkinter.PhotoImage(file="NonRealTime/mainkuma.png"),
    tkinter.PhotoImage(file="NonRealTime/nazo.png"),
]
photograph()
root.mainloop()