class alumnos:
    def __init__(self,nombre,apellido,edad,nota,nacionalidad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.nota=nota
        self.nacionalidad=nacionalidad

    def leerNota(self):
        print(self.nota)
    def registrarNota(self,notaAlumno):
        self.nota=notaAlumno
        print(self.nota)


