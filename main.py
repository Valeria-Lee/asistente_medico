import serial

'''
Crea un objeto Serial llamado que representa la conexión serial al Arduino. 
(puerto, velocidad)
'''
ard = serial.Serial('/dev/ttyUSB0', 9600)

def send_msg_to_display(msg):
    '''
    Envia una cadena msg a traves de la comunicacion serial.
    Primero convierte la cadena en una sentencia de bytes mediante la codificacion UTF-8 para poder ser transmitido al monitor serial.
    El caracter \n indica un salto de linea y como se puede observar en el otro fragmento de codigo es el caracter que se usa para identificar el cierre de un mensaje.
    '''
    ard.write(msg.encode('utf-8'))
    ard.write(b'\n')

def main():
    '''
    Enviar el mensaje introducido por el usuario a traves de la funcion send_msg_to_display()
    Finaliza con cerrar la comunicacion.
    '''
    try:
        # TODO: aqui enviariamos los mensajes del asistente
        msg_to_send = input("ingresa mensaje: ")
        send_msg_to_display(msg_to_send)
    finally:
        ard.close()

if __name__ == '__main__':
    main()
