import tkinter

def place_symbole(row, colum) :
    print(f"{row}/{colum}")

def drow_grile() :
    for row in range(3) :
        for colum in range(3) :
            button = tkinter.Button(
                root, font=("Arial", 50),
                width=4, height=2,
                command=lambda r=row, c=colum: place_symbole(r, c)
                )
            button.grid(row=row,column=colum)

# creations de la fenetre
root = tkinter.Tk()

# personalisations de la fenetre
root.title("tictacto")
root.minsize(250, 250)

# apele de la fonctions pour desiner la grille
drow_grile()

root.mainloop()