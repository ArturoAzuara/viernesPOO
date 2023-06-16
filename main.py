from cosas import *

def main():
    per1 = Persona("Jose", 19)
    print(per1)
    print(Persona.descripcion)
    print("------herencia alumno-------")
    al1 = Alumno("Jose", 19, "232323322","ICO")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()
    print(al2)
    al2.nombre = "Juan"
    print(al2)
    al2.dormir()

    print("------herencia profe------")
    profe1 = Profesor("Jesus", 30 + 16,3535353,"Ingenieria de software")
    print(profe1)
    profe1.dormir()

    print("------herencia ayudante profe--------")
    ayudante = AyudanteProfesor("Adrián", 20,"23235","ICO",21323 , "Ing. de software", 4)
    print(ayudante)
    ayudante.dormir()
    ayudante.nombre = "Abraham"
    ayudante.dar_clase("POO")


main()