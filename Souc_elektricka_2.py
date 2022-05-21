import tkinter
canvas = tkinter.Canvas(width = 500, height = 100, bg = "black")
canvas.pack()



subor = open("zastavky.txt", encoding="utf8")

zastavky = []

for riadok in subor:
    zastavky.append(riadok.strip())

dlzka = len(zastavky)

i = 0

def tlacidlo(event):
    global i
    canvas.delete("all")
    
    if i < dlzka - 1: 
        canvas.create_text(250,50, text = zastavky[i], fill = "red", font = ("Arial",40), tags = "ciara")
        
    else:
        canvas.create_text(250,50, text = zastavky[i] + "  " + "PROSIM VYSTUPTE", fill = "red", font =("Arial", 20), tags = "ciara")
    
    i += 1
    
def posuvaj():
    global xCiara
    canvas.move('ciara',-5,0)
    xCiara -= 5
    if xCiara < 0:
        canvas.move('ciara',1000,0)
        xCiara +=1000
    canvas.after(20,posuvaj)

xCiara = 700


posuvaj()

canvas.bind_all("<KeyPress>",tlacidlo)

canvas.mainloop()


