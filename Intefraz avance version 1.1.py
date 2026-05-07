from tkinter import*
from tkinter import messagebox

data={
    "Ing Software":{
              "IHC": "Lunes 07:00am - 8:30am / Martes: 15:00pm - 16:30pm / Sabado: 11:00am - 15:00pm / Grupos: Lunes S4, Martes: J, Sabado S",
               "Programacion":"Lunes: 09:30am - 12:00pm / Viernes: 7:00am - 9:30am / " 

            },
            "Ing Civil":{
        "Cálculo": "Miércoles 11:00 - 13:00 | Prof.",
        "Estructuras": "Jueves 07:00 - 09:00 | Prof.",        
        }
}
    
ventana=Tk()
ventana.geometry("500x300")
ventana.config(bg='gray')
ventana.title('Sistema UAEMEX')
ventana.resizable(width=False,height=False)

def mostrarhorario(materia,info):
    messagebox.showinfo(F"Detalles de {materia}",info)
def seleccioncarrera(nombrecarrera):
    subventana=Toplevel(ventana)
    subventana.title(f"Materia de {nombrecarrera}")
    subventana.geometry("300x250")
    
    Label(subventana,text=f"Materias disponibles:",font=("Arial",10,"bold")).pack(pady=10)
    materias=data.get(nombrecarrera,{})

    if not materias:
        Label(subventana, text="No hay materias registradas, ").pack()
    else:
        for materia,info in materias.items():
            Button(subventana, text=materia, width=25,
                   command=lambda m=materia, i=info:mostrarhorario(m,i)).pack(pady=5)

menu=Menu(ventana)
ventana.config(menu=menu)

Carreras=Menu(menu, tearoff=0)

Carreras.add_command(label="Ing Software",command=lambda: seleccioncarrera("Ing Software"))
Carreras.add_command(label="Ing Civil",command=lambda: seleccioncarrera("Ing Civil"))
Carreras.add_command(label="Ing Mecanica", command=lambda: seleccioncarrera("Ing Mecanica"))

menu.add_cascade(label="carreras",menu=Carreras)

menuarchivo=Menu(menu,tearoff=0)
menuarchivo.add_command(label="Salir",command=ventana.quit)
menu.add_cascade(label="Archivo",menu=menuarchivo)


try:
    banner_path=r'C:\Users\HP VICTUS\Desktop\images.png'
    imgbanner=PhotoImage(file=banner_path)
    mostbaner=Label(ventana,image=imgbanner,bg='gray')
    mostbaner.pack(side="top",padx=10,pady=5)
    
    ventana.imgbanner=imgbanner
except:
    Label(ventana,text="[Banner Universitario]",bg="darkgreen",fg="white",height=5,width=50).pack(pady=10)




ventana.mainloop()