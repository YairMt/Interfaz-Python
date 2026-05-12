from tkinter import *
from tkinter import messagebox

alumno = {
    "2211931": {"nombre": "Yair Manzanarez Torres", "carrera": "Ing Software"},
    "2142249": {"nombre": "Ithan", "carrera": "Ing Software"},
    "2115283": {"nombre": "Landa", "carrera": "Ing Software"}
}

data = {
    "Ing Software": {
        "IHC": "Lunes 07:00am - 8:30am / Martes: 15:00pm - 16:30pm / Sabado: 11:00am - 15:00pm",
        "Programacion": "Lunes: 09:30am - 12:00pm / Viernes: 7:00am - 9:30am" 
    },
    "Ing Civil": {
        "Cálculo": "Miércoles 11:00 - 13:00 | Prof.",
        "Estructuras": "Jueves 07:00 - 09:00 | Prof."
    }
}

ventana = Tk()
ventana.geometry("850x600")
ventana.config(bg='white')
ventana.title('Sistema UAEMEX')
ventana.resizable(width=False, height=False)


def materias(materia, info):
    messagebox.showinfo(materia, info)

def banner():
    
    try:
        ruta = r'C:\Users\HP VICTUS\Desktop\Carpetas de Escritorio\imm.png'
        original = PhotoImage(file=ruta)
        chica = original.subsample(2, 2)

        lbl_img = Label(main_content, image=chica, bg='white')
        lbl_img.image = chica 
        lbl_img.pack(side=TOP, fill=X, pady=(10, 0))
    except:
        Label(main_content, text="UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO", 
              font=("Arial", 12, "bold"), bg="#2d572c", fg="white", pady=15).pack(side=TOP, fill=X)

def perfil():
    user = entry_user.get()
    
    if user in alumno:
        nombreal = alumno[user]["nombre"]
        carrera_al = alumno[user]["carrera"]

        
        for widget in main_content.winfo_children():
            widget.destroy()

        
        banner()

        Label(main_content, text=f"Bienvenido: {nombreal}", 
              font=("Arial", 16, "bold"), bg="white", fg="#2d572c").pack(pady=(25, 5))
        
        Label(main_content, text=f"Plan de Estudios: {carrera_al}", 
              font=("Arial", 11), bg="white", fg="gray").pack(pady=(0, 20))

        if carrera_al in data:
            for materia, horarios in data[carrera_al].items():
                Button(main_content, text=f"▶ {materia}", font=("Arial", 10), anchor="w",
                       bg="#f0f0f0", relief="flat", width=60, padx=20, cursor="hand2",
                       command=lambda m=materia, t=horarios: materias(m, t)).pack(pady=5)
    else:
        messagebox.showerror("Error", "Usuario no Encontrado")


sidebar = Frame(ventana, bg="#2d572c", width=200)
sidebar.pack(side=LEFT, fill=Y)

opciones = ["Inicio", "Trayectoria", "Inscripción", "Calificaciones", "Cerrar"]
for opt in opciones:
    Button(sidebar, text=opt, bg="#2d572c", fg="white", relief="flat",
           font=("Arial", 10, "bold"), anchor="w", padx=20, height=2).pack(fill=X)


main_content = Frame(ventana, bg='white')
main_content.pack(side=RIGHT, expand=True, fill=BOTH)

banner()

login_frame = Frame(main_content, bg="white")
login_frame.pack(expand=True)

Label(login_frame, text="Sistema de Servicios Escolares", font=("Arial", 18, "bold"),
      bg="white", fg="#2d572c").pack(pady=20)

Label(login_frame, text="Usuario*", bg="white").pack(anchor="w")
entry_user = Entry(login_frame, font=("Arial", 12), bg="#e8f0fe", relief="flat", width=30)
entry_user.pack(pady=5)

Button(login_frame, text="FIRMÁRESE", bg="#d4af37", fg="white", relief="flat", 
       font=("Arial", 11, "bold"), height=2, command=perfil).pack(pady=30, fill=X)

ventana.mainloop()