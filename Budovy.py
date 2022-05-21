import tkinter
c = tkinter.Canvas(width = 800, height = 600, bg = 'white')
c.pack()

subor = open('vystavba.txt')
hranica = int(subor.readline().strip())
udaje = []
for riadok in subor:
    udaje.append(riadok.strip().split())

subor.close()

rozmery = []
for udaj in udaje:
    rozmery.append([int(udaj[0]),int(udaj[1])])

pocet = len(rozmery)
a1, a2 = 100, 400
for i in range(pocet):
    sirka = rozmery[i][0]
    vyska = rozmery[i][1]
    b1, b2 = a1 + sirka, a2 - vyska
    if vyska == 0:
        c.create_line(a1, a2, b1, b2, fill='lightgreen',width=2)
    else:
        c.create_rectangle(a1, a2, b1, b2, fill='lightgrey')
    
    predvyska = rozmery[i-1][1]
    #print(predvyska)
    if abs(predvyska-vyska) >= hranica and vyska != 0 and predvyska !=0:
        c.create_line(a1,a2 - predvyska,a1,a2 - vyska,fill = "red")
    a1 += sirka
    
    


c.mainloop()

