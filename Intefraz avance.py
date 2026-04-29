from tkinter import*

ventana=Tk()
ventana.geometry("500x300")
ventana.config(bg='gray')
ventana.title('VENTANA PRINCIPAL')
ventana.resizable(width=False,height=False)
ventana.iconbitmap(r'C:\Users\HP VICTUS\Desktop\Carpetas de Escritorio\Trabajos python IHC\Comprimidos.ico')

try:
    imagen_original = Image.open(r'')
    imagen_redimensionada = imagen_original.resize((500, 120), Image.LANCZOS)
    render = ImageTk.PhotoImage(imagen_redimensionada)
    banner = Label(ventana, image=render, bg='gray')
    banner.image = render
    banner.pack(side="top", fill="x")
    except Exception as e:
    print(f"No se pudo cargar la imagen: {'e'}")


menu=Menu(ventana)
ventana.config(menu=menu)


Carreras=Menu(menu,tearoff=0)
Carreras.add_command (label="Ing Software")
Carreras.add_command (label="Ing Civil")
Carreras.add_command (label="Ing Mecanica")
Carreras.add_command (label="Ing")
Carreras.add_command (label="Ing")
Carreras.add_command (label="Ing")



Materias=Menu(menu,tearoff=0)

Materias.add_command(label="Interaccion Humano Computadora (IHC)")
Materias.add_command(label="Programación")
Materias.add_command (label="Calculo Dif/Int")
Materias.add_command(label="Algebra")
Materias.add_separator()
Materias.add_command(label="Exit")

Horarios=Menu (menu,tearoff=0)

Horarios.add_command (label="Algebra")
Horarios.add_command(label="Interaccion Humano Computadora")
Horarios.add_command(label="Dias")

Help=Menu (menu,tearoff=0)

Help.add_command (label="Help")
Help.add_separator
Help.add_command(label="About")


menu.add_cascade(label="Carrera",menu=Carreras)
menu.add_cascade(label="Materias",menu=Materias)
menu.add_cascade(label="Horarios",menu=Horarios)
menu.add_cascade(label="Help",menu=Help)



ventana.mainloop()

