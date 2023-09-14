from logica.Calificaciones import Calificaciones

if __name__ == '__main__':
    notaInicial = float(input("Igrese su nota: "))
    calificaciones = Calificaciones(notaInicial)
    calificaciones.calificacion()


