import tkinter as tk
ventana = tk.Tk()
ventana.title("CONTROL DE MOTOR")
ventana.geometry("600x400+450+200")
ventana.resizable(False, False)
diccionario_motor= {}

WELCOME_MESSAGE = """
     BIENVENIDO AL SISTEMA 'CONTROL DE MOTOR'

"""
TURN_SELECT_MESSSAGE = """
Para comenzar, debes seleccionar el sentido de giro del motor:
         1) CW para giro sentido horario.
         2) CCW para giro sentido antihorario.
         """

def seleccionar_giro_stop():
    global diccionario_motor
    diccionario_motor['sentido_giro']= 'STOP'
    diccionario_motor['velocidad']=0
    etiqueta.config(text=f"Sentido:{diccionario_motor['sentido_giro']}, Velocidad:{diccionario_motor['velocidad']}")
    print(diccionario_motor)
    boton1.pack_forget()
    boton2.pack_forget()
    boton3.pack_forget()
    
def sentido_seleccionado(sentido):
    global diccionario_motor
    diccionario_motor['sentido_giro']= sentido
    boton1.pack_forget()
    boton2.pack_forget()
    boton3.pack_forget()
    etiqueta.config(text="Ahora indique la velcidad deseada dentro de un rando de 0-255")
    etiqueta_entrada_velocidad = tk.Label(ventana, text='Ingrese velocidad')
    etiqueta_entrada_velocidad.pack()

    entrada_velocidad = tk.Entry(ventana)
    entrada_velocidad.pack()

    def aplicar_velocidad():
        valor_velocidad = entrada_velocidad.get()
        if valor_velocidad.isdigit():  
            velocidad = int(valor_velocidad)
            if 0 <= velocidad <= 255:
             diccionario_motor['velocidad']= velocidad
             etiqueta.config(text=f"Sentido: {diccionario_motor['sentido_giro']} , Velocidad: {diccionario_motor['velocidad']}")
             print(diccionario_motor)
             entrada_velocidad.pack_forget()
             etiqueta_entrada_velocidad.pack_forget()
             boton_aceptar_velocidad.pack_forget()
            else:
                 etiqueta.config(text=" Introduzca un valor numerico dentro del rango 0-255")
        else:
            etiqueta.config(text=" Introduzca un valor numerico valido")

    boton_aceptar_velocidad= tk.Button(ventana, text='ACEPTAR',command=aplicar_velocidad)
    boton_aceptar_velocidad.pack()
      
   
  
etiqueta1 = tk.Label(ventana, text=WELCOME_MESSAGE) 
etiqueta1.pack()

etiqueta = tk.Label(ventana, text=TURN_SELECT_MESSSAGE) 
etiqueta.pack()

boton1= tk.Button(ventana, text='CW',command=lambda:sentido_seleccionado('CW'),)
boton1.config(fg='white', bg='blue')
boton1.pack(side='left',padx=110)

boton2= tk.Button(ventana, text='CCW', command=lambda:sentido_seleccionado('CCW'))
boton2.config(fg='white', bg='blue')
boton2.pack(side='right', padx=110)

boton3= tk.Button(ventana, text= 'STOP', command=seleccionar_giro_stop)
boton3.config(fg='white', bg='red')
boton3.pack()


ventana.mainloop()


