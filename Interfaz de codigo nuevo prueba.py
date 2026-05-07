from tkinter import *
from tkinter import messagebox  

data = {
    "Ing Software": {
        "IHC": "Lunes 07:00 - 09:00 | Prof. Arriaga",
        "Programación": "Martes 09:00 - 11:00 | Prof. Sánchez",
    },
    "Ing Civil": {
        "Cálculo": "Miércoles 11:00 - 13:00 | Prof. Gómez",
        "Estructuras": "Jueves 07:00 - 09:00 | Prof. Ruiz",
    }
}

ventana = Tk()
ventana.geometry("500x350")
ventana.config(bg='gray')
ventana.title('SISTEMA UNIVERSITARIO')
ventana.resizable(width=False, height=False)



def mostrar_horario(materia, info):
   
    messagebox.showinfo(f"Detalles de {materia}", info)

def seleccionar_carrera(nombre_carrera):
   
    sub_ventana = Toplevel(ventana)
    sub_ventana.title(f"Materias de {nombre_carrera}")
    sub_ventana.geometry("300x250")
    
    Label(sub_ventana, text=f"Materias disponibles:", font=("Arial", 10, "bold")).pack(pady=10)
    

    materias = data.get(nombre_carrera, {})
    
    if not materias:
        Label(sub_ventana, text="No hay materias registradas.").pack()
    else:
       
        for materia, info in materias.items():
            Button(sub_ventana, text=materia, width=25, 
                   command=lambda m=materia, i=info: mostrar_horario(m, i)).pack(pady=5)



menu_barra = Menu(ventana)
ventana.config(menu=menu_barra)


menu_carreras = Menu(menu_barra, tearoff=0)

menu_carreras.add_command(label="Ing Software", command=lambda: seleccionar_carrera("Ing Software"))
menu_carreras.add_command(label="Ing Civil", command=lambda: seleccionar_carrera("Ing Civil"))
menu_carreras.add_command(label="Ing Mecanica", command=lambda: seleccionar_carrera("Ing Mecanica"))

menu_barra.add_cascade(label="Carreras", menu=menu_carreras)


menu_archivo = Menu(menu_barra, tearoff=0)
menu_archivo.add_command(label="Salir", command=ventana.quit)
menu_barra.add_cascade(label="Archivo", menu=menu_archivo)


try:
    banner_path = r'C:\Users\HP VICTUS\Desktop\images.png'
    imgbanner = PhotoImage(file=banner_path) 
    mostbaner = Label(ventana, image=imgbanner, bg='gray')
    mostbaner.pack(side="top", padx=10, pady=5)
    
    ventana.imgbanner = imgbanner 
except:
    Label(ventana, text="[Banner Universitario]", bg="darkgreen", fg="white", height=5, width=50).pack(pady=10)

ventana.mainloop()


