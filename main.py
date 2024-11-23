import serial
import time
from datetime import datetime
from recordatorio import Recordatorio

# Crea un objeto Serial llamado que representa la conexión serial al Arduino. 
# (puerto, velocidad)
ard = serial.Serial('COM1', 9600)  # Asegúrate de usar el puerto correcto

def send_msg_to_display(msg):
    '''
    Envia una cadena msg a traves de la comunicacion serial.
    Primero convierte la cadena en una sentencia de bytes mediante la codificacion UTF-8 para poder ser transmitido al monitor serial.
    El caracter \n indica un salto de linea y como se puede observar en el otro fragmento de codigo es el caracter que se usa para identificar el cierre de un mensaje.
    '''
    ard.write(msg.encode('utf-8'))
    ard.write(b'\n')

def create_recordatorio():
    '''
    Solicita los datos del recordatorio al usuario y crea un objeto Recordatorio.
    '''
    nombre = input("Nombre del recordatorio: ")
    hora = input("Hora del recordatorio (HH:MM): ")
    cant = input("Cantidad: ")
    medida = input("Medida: ")
    desc = input("Descripción: ")
    return Recordatorio(nombre, [hora], cant, medida, desc)

def main():
    '''
    Crea un recordatorio cuando se presiona el botón y envía el mensaje al display a la hora especificada.
    '''
    try:
        recordatorio = None
        while True:
            if ard.in_waiting > 0:
                button_state = ard.readline().decode('utf-8').strip()
                if button_state == "BUTTON_PRESSED":
                    recordatorio = create_recordatorio()
                    print("Recordatorio creado.")
            
            if recordatorio:
                hora_actual = datetime.now().strftime("%H:%M")
                mensaje = recordatorio.checar_hora(hora_actual)
                if mensaje and mensaje != "Todavia no es hora.":
                    send_msg_to_display(mensaje)
                    time.sleep(60)  # Espera un minuto antes de volver a checar la hora
    finally:
        ard.close()

if __name__ == '__main__':
    main()
    