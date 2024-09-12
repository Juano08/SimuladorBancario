__author__ = "Juan"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "juan.ruedav@campusucc.edu.co"

from Fecha import Fecha 

class Empleado: 
    # Aqui inicia la declaracion de la clase

    '''#-------------------------------------
    # Atributos
    -----------------------------------------#'''

    nombre = ''
    apeliido = ''
    salario = 0

    '''#------------------------------------
    # 1 Masculino, 2 = Femenino
    ----------------------------------------#'''

    sexo = 0 

    '''#---------------------------------------------
    Asociacion
    ------------------------------------------------#'''

    fechaIngreso = Fecha()
    fechaNacimiento = Fecha() 

    '''#---------------------------------------------
    # Metodos
    ---------------------------------------------#'''

    def DarNombre(self):
        # Aqui va mi codigo
        return self.nombre

    
    __method__ = "CambiarSalario"
    __parameter__ = "nuevoSalario"
    __returns__ = "Salario"
    __Description__ = "metodo que actualiza el salario del empleado"
    def CambiarSalario(self, nuevoSalario):
        # Aqui va mi codigo 
        self.salario = nuevoSalario


    # Retorna el salario del empleado
    def DarSalario(self):
        # Aqui va mi codigo
        return self.salario
    

    __method__ = "ConsutarFechaIngreso"
    __parameter__ = "Ninguno"
    __returns__ = "fecha de ingreso"
    __Description__ = "metodo que muestra la fecha de ingreso del empleado"
    def ConsultarFechaIngreso(self):
        # Aqui va mi codigo
        return self.fechaIngreso.DarFecha() 
    
    __method__ = "CalcularSalarioAnual"
    __parameter__= "ninguno"
    __returns__ = "SalariAnual"
    __Description__ = "muestra el salario anual del empleado"
    def CalcularSalarioAnual(self):
        # Aqui va mi codigo
        # Forma 1
        # total = self.salario*12
        # return total
        # Forma 2
        return self.salario*12
    
    __method__ = "CalcularImpuestoSalarioAnual"
    __parameter__ = "Ninguno"
    __returns__ = "Impuesto de salario anual"
    __Description__ = "Muestra el impuesto del salario anual del empleado"
    def CalcularImpuestoSalarioAnual (self):
        # Aqui inicia mi codigo
        # Forma 1       
        # salrioAnual=self.CalcularSalarioAnual()
        # impuestoAnual=salarioAnual*0.19
        # return impuestoAnual
        # Forma 2
        return self.CalcularSalarioAnual()*0.19
    

#############################################################################
    #__method__ = "CalcularSalarioMensual"
    #__parameter__ = "Ninguno"
    #__returns__ = "Salario Mensual"
    #__Description__ = "metodo que muestra el salario mensual del empleado"
    #def CalcularSalarioMensual(self):
        return self.salario
#############################################################################

    __method__ = "CalcularImpuestoSalarioMensual"
    __parameter__= "ninguno"
    __returns__ = "Impuesto salario mensual"
    __Description__ = "metodo que permite calcular el impuesto del salario mensual"
    def CalcularImpuestoSalarioMensual(self):
        # Aqui inicia mi codigo
        return self.DarSalario()*0.19