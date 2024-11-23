class Recordatorio():
    def __init__(self, nombre, hora, cant, medida, desc="", finalizado=False):
        self.nombre = nombre # Nombre que se le quiera asignar al recordatorio.
        self.hora = hora # Hora(s) para tomar la medicina en un rango de 24 horas.
        self.cant = cant # Cantidad para la dosis.
        self.medida = medida # Medida para la dosis.
        self.desc = desc # Descripcion opcional: como instrucciones extra. Por defecto es una cadena vacia.
        self.finalizado = finalizado # Para eliminar al recordatorio de la lista.

    def checar_hora(self, hora_actual):
        # La hora actual tiene que ser en formato 24 horas.
        mensaje = self.imprimir_info() # TODO: No se si se le tenga que poner el self como argumento.

        if len(self.hora) == 1:
            if hora_actual == self.hora[0]:
                print(mensaje) ## TODO: En lugar de imprimir se tendra que retornar.
        else:
            if hora_actual in self.hora:
                print(mensaje)
            else:
                print("Todavia no es hora.")

    def imprimir_info(self):
        msj_c_formato = []
        msj_pedazo = []
        # Recortar la cadena en "subcadenas" de 16 caracteres para poder renderizar de mejor manera.
        msj = f"Es hora de {self.nombre}. {self.desc}. Tienes que tomar {self.cant} de {self.medida}."

        msj = msj.split()
            
            # Se van a eliminar los caracteres de la cadena msj y se pasaran a cadenitas que se agregaran a un arreglo.
        while len(msj) >= 0:
                espacios_vacios = 16
    
                while espacios_vacios <= 16:
                    if (espacios_vacios - len(msj[0])) > 0:
                        msj_pedazo.append(msj[0])
                        espacios_vacios -= len(msj[0]) 
                        msj.pop(0) 
                    else:
                        break
    
                msj_c_formato.append(msj_pedazo)
                msj_pedazo = []

    def marcar_completado(self):
        self.finalizado = True
