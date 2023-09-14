class Calificaciones():
    def __init__(self, nota):
        self.nota = nota

    def calificacion(self):
        if self.nota > 9.0 :
            print("La calificacion es A")
        elif self.nota > 8.0 :
            print("La calificacion es B")
        elif self.nota >= 7.5 :
            print("La calificacion es C")
        else:
            print("La calificacion es R")



