import re  

velocidad = re.compile(r"^-?\d+(\.\d+)?$")  
WELCOME_MESSAGE = """
     BIENVENIDO AL SISTEMA 'CONTROL DE MOTOR'
       Para detener el motor en cuaquier momento del sistema, escribe STOP o stop
"""

TURNING_DDIRECTION_MESSAGE = """
        Introduzca el sentido de giro del motor:
         1) CW o cw para giro sentido horario.
         2) CCW occw para giro sentido antihorario.
        
""" 

print(WELCOME_MESSAGE)

while True:
    turning_direction = input(TURNING_DDIRECTION_MESSAGE) 
    if turning_direction.lower() == 'cw' or turning_direction.lower() == 'ccw' or turning_direction.lower()=='stop':
        break
    else:
        print('Intruduzca un sentido de giro valido') 
        

while True:
    if turning_direction.lower() == 'stop':
        
        user_velocity = 0
        break
      
    user_velocity = input("Introduce una velocidad válida [-255, 254]: ")

    if user_velocity.lower() =='stop':
        turning_direction= 'stop'
        user_velocity = 0
        break


    if velocidad.match(user_velocity):  
        user_velocity = float(user_velocity) 

        if 0 <= user_velocity <= 254:
            break  
        else:
            print("Error: La velocidad no está dentro del rango permitido.")
    else:
        print("Error: Debes ingresar un número entero o decimal válido.")

activation_commands_motor ={

  'direction': turning_direction.lower() , 'velocity': user_velocity

}

print(activation_commands_motor)

print(user_velocity, turning_direction)
