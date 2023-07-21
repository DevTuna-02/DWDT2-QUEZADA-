from alumnos import alumnos
print('Bienvenidos al registro de Notas.')
Alumnos=[]

terminar=False
while terminar==False:
    comando=input('Ingrese comando:').upper()
    if comando=='R':
        Nombre=input('Ingrese Nombre del Alumno:')
        Apellido=input('Ingrese Apellido del Alumno:')
        Edad=input('Ingrese Edad del Alumno:')
        Nacionalidad=input('Ingrese Nacionalidad del Alumno:')
        Alumnos.append(alumnos(Nombre,Apellido,Edad,'',Nacionalidad))


    elif comando=='C':
        for alumno in Alumnos:
            nota=None
            while nota is None:
                nota=input(f"Alumno <{alumno.nombre} {alumno.apellido}, ingrese nota:")
                try:
                    nota=float(nota)
                except ValueError:
                    print('La nota debe ser un numero entre 0 y 20')
                if nota>=0.0 and nota<=20.0:
                    alumno.registrarNota(nota)
                else:
                    print('La nota debe ser un numero entre 0 y 20')

    elif comando=='P':
        suma=0
        for alumno in Alumnos:
            suma=suma+alumno.nota
        promedio=suma/len(Alumnos)
        print(f'El promedio de notas para <{len(Alumnos)}>es: {promedio}')

    elif comando=='S':
        suma=0
        for alumno in Alumnos:
            suma=suma+alumno.nota
        print(f'La suma de notas para <{len(Alumnos)}>es: {suma}')
    elif comando=='X':
        terminar =True
    else:
        print('Ingrese un comando valido...')

