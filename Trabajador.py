from Persona import Persona

class Trabajador(Persona):
    def __init__(self, identificacion, nombre, apellido1, apellido2, fechaNacimiento, genero, activo, idRol):
        super().__init__(identificacion, nombre, apellido1, apellido2, fechaNacimiento, genero, activo)
        self.idRol=idRol
    
    def capturaDatos(self):
         # Validación de identificación
        while True:
            self.identificacion = input("Digite el número de identificación del trabajador: ").strip()
            if self.identificacion:
                break
            else:
                print("El número de identificación no puede estar vacío o contener solo espacios.")
        # Validación del nombre
        while True:
            self.nombre = input("Digite el nombre del trabajador: ").strip()
            if self.nombre:
                break
            else:
                print("El nombre no puede estar vacío o contener solo espacios.")
        # Validación del primer apellido
        while True:
            self.apellido1 = input("Digite el primer apellido del trabajador: ").strip()
            if self.apellido1:
                break
            else:
                print("El primer apellido no puede estar vacío o contener solo espacios.")
        # Validación del segundo apellido
        while True:
            self.apellido2 = input("Digite el segundo apellido del trabajador: ").strip()
            if self.apellido2:
                break
            else:
                print("El segundo apellido no puede estar vacío o contener solo espacios.")
        # Validación de la fecha de nacimiento en formato yyyy-MM-dd
        while True:
            try:
                anhoNacimiento = int(input("Digite el año de nacimiento del pasajero: ").strip())
                if anhoNacimiento > 0:
                    self.fechaNacimiento = anhoNacimiento
                    break
                else:
                    print("El año de nacimiento debe de ser una numero positivo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")   
        # Validación del género
        while True:
            gen = input("""
            Seleccione el género:
            F - Femenino
            M - Masculino
            """).strip().upper()
            if gen in ["F", "M"]:
                self.genero = gen
                break
            else:
                print("Opción no válida. Ingrese 'F' para Femenino o 'M' para Masculino.")
        #Valida que sea un dato entero        
        # NOTA: SE BEDE AGREGAR LA LOGICA PARA AGREGAR EL ID ROL
        objTrabajador = Trabajador(self.identificacion, self.nombre, self.apellido1, self.apellido2,
                                   self.fechaNacimiento, self.genero, activo=True, idRol=self.idRol)

    def modificar(self):
        pass

    def listar(self):
        pass

    def desactivar(self):
        pass