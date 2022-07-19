
from tkinter import *
import os


def ventanaInicio():
    global ventanaPrincipal
    ventanaPrincipal=Tk()
    ventanaPrincipal.geometry("300x250")
    ventanaPrincipal.title("Login de Afiliaccion de Salud")
    Label(text="Bienvenido a la Afiliacion de Salud", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Acceder al login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Registrarse un usuario y una contraseña", height="2", width="30", command=registro).pack()
    Label(text="").pack()
    ventanaPrincipal.mainloop()

def registro():
    global ventanaRegistro
    ventanaRegistro = Toplevel(ventanaPrincipal)
    ventanaRegistro.title("Registro")
    ventanaRegistro.geometry("300x250") 
    global nombre_usuario
    global clave
    global entrada_nombre
    global entrada_clave
    nombre_usuario = StringVar() 
    clave = StringVar() 
 
    Label(ventanaRegistro, text="Introduzca datos").pack()
    Label(ventanaRegistro, text="").pack()
    etiqueta_nombre = Label(ventanaRegistro, text="Nombre de usuario * ")
    etiqueta_nombre.pack()
    entrada_nombre = Entry(ventanaRegistro, textvariable=nombre_usuario) 
    entrada_nombre.pack()
    etiqueta_clave = Label(ventanaRegistro, text="Contraseña ")
    etiqueta_clave.pack()
    entrada_clave = Entry(ventanaRegistro, textvariable=clave, show='*') 
    entrada_clave.pack()
    Label(ventanaRegistro, text="").pack()
    Button(ventanaRegistro, text="Registrarse", width=10, height=1, command = registro_usuario).pack() 


def login():
    global ventana_login
    ventana_login = Toplevel(ventanaPrincipal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("300x250")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña").pack()
    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="Nombre usuario * ").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña * ").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login).pack()


def verifica_login():
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    entrada_login_usuario.delete(0, END) 
    entrada_login_clave.delete(0, END) 
 
    lista_archivos = os.listdir() 
    if usuario1 in lista_archivos:
        archivo1 = open(usuario1, "r") 
        verifica = archivo1.read().splitlines() 
        if clave1 in verifica:
            exito_login() 
        else:
            no_clave()
    else:
        no_usuario()


def exito_login():
    global ventana_exito
    ventana_exito = Toplevel(ventana_login)
    ventana_exito.title("Exito")
    ventana_exito.geometry("150x100")
    Label(ventana_exito, text="Login finalizado con exito").pack()
    Button(ventana_exito, text="OK", command=registroDatos).pack()
 
''' dara a conocer si la contraseña fue correcto''' 
 
def no_clave():
    global ventana_no_clave
    ventana_no_clave = Toplevel(ventana_login)
    ventana_no_clave.title("ERROR")
    ventana_no_clave.geometry("150x100")
    Label(ventana_no_clave, text="Contraseña incorrecta ").pack()
    Button(ventana_no_clave, text="OK", command=borrar_no_clave).pack() 
 

''' dara a conocer si el usuario no es correcto''' 
def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventana_login)
    ventana_no_usuario.title("ERROR")
    ventana_no_usuario.geometry("150x100")
    Label(ventana_no_usuario, text="Usuario no encontrado").pack()
    Button(ventana_no_usuario, text="OK", command=borrar_no_usuario).pack() 



def borrar_exito_login():
    ventana_exito.destroy()
 
 
def borrar_no_clave():
    ventana_no_clave.destroy()
 
 
def borrar_no_usuario():
    ventana_no_usuario.destroy()


 
def registro_usuario():
 
    usuario_info = nombre_usuario.get()
    clave_info = clave.get()
 
    file = open(usuario_info, "w") 
    file.write(usuario_info + "\n")
    file.write(clave_info)
    file.close()
 
    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)
 
    Label(ventanaRegistro, text="Registro completado con éxito", fg="green", font=("calibri", 11)).pack()
 
 


def registroDatos():
    
    raiz=Tk()
    raiz.title("Registro de Afiliaccion de Salud")
    miFrame=Frame(raiz,width=1200,height=600)
    miFrame.pack()
    '''creamos los cuadros de texto'''
    cuadroCedula=Entry(miFrame)
    cuadroCedula.grid(row=0,column=1, padx=10, pady=10)
    cuadroNombre=Entry(miFrame)
    cuadroNombre.grid(row=1,column=1, padx=10, pady=10)
    cuadroApellidos=Entry(miFrame)
    cuadroApellidos.grid(row=2,column=1, padx=10, pady=10)
    cuadroGenero=Entry(miFrame)
    cuadroGenero.grid(row=3,column=1, padx=10, pady=10)
    cuadroFechaNacimiento=Entry(miFrame)
    cuadroFechaNacimiento.grid(row=4,column=1, padx=10, pady=10)
    cuadroPais=Entry(miFrame)
    cuadroPais.grid(row=5,column=1, padx=10, pady=10)
    cuadroProvincias=Entry(miFrame)
    cuadroProvincias.grid(row=6,column=1, padx=10, pady=10)
    cuadroTrabajo=Entry(miFrame)
    cuadroTrabajo.grid(row=7,column=1, padx=10, pady=10)
    cuadroSalario=Entry(miFrame)
    cuadroSalario.grid(row=8,column=1, padx=10, pady=10)

    '''creamos los Label para el registro '''
    cedulaLabel=Label(miFrame,text="Cedula:")
    cedulaLabel.grid(row=0,column=0, sticky="e", padx=10, pady=10) 
    nombreLabel=Label(miFrame,text="Nombre:")
    nombreLabel.grid(row=1,column=0, sticky="e", padx=10, pady=10) 
    apellidoLabel=Label(miFrame,text="Apellido:")
    apellidoLabel.grid(row=2,column=0, sticky="e", padx=10, pady=10) 
    generoLabel=Label(miFrame,text="Genero:")
    generoLabel.grid(row=3,column=0, sticky="e", padx=10, pady=10)
    fechaLabel=Label(miFrame,text="Fecha de Nacimiento:")
    fechaLabel.grid(row=4,column=0, sticky="e", padx=10, pady=10)
    paisLabel=Label(miFrame,text="Pais:")
    paisLabel.grid(row=5,column=0, sticky="e", padx=10, pady=10)
    provinciaLabel=Label(miFrame,text="Provincia:")
    provinciaLabel.grid(row=6,column=0, sticky="e", padx=10, pady=10)
    trabajoLabel=Label(miFrame,text="Trabajo:")
    trabajoLabel.grid(row=7,column=0, sticky="e", padx=10, pady=10)
    salarioLabel=Label(miFrame,text="Salario:") 
    salarioLabel.grid(row=8,column=0, sticky="e", padx=10, pady=10)

    '''creamos el boton de ingresar'''
    botonRegistar=Button(raiz, text="Guardar")
    botonRegistar.pack()

    raiz.mainloop()


ventanaInicio()  
 
 