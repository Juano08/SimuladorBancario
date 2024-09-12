__author__ = "Juan José Rueda Viveros"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "juan.ruedav@campusucc.edu.co"

class Fecha:
    # Aqui inicia la declaracion de mi clase
    #--------------------------------------#

    '''#-----------------------------------
    # Atributos
    -----------------------------------#'''
    
    dia= 0
    mes= 0
    anio= 0

    __method__ = "DarDia"
    __parameter__ = "ninguno"
    __returns__ = "dia"
    __description__ = "metodo que permite regresar el dia" 
    def DarDia(self):
        #Aqui va mi codigo
        return self.dia 

    __method__ = "DarMes"
    __parameter__= "ninguno"
    __returns__ = "mes"
    __description__ = "metodo que permite regresar el mes"
    def DarMes(self):
        # Aqui va mi codigo
        return self.mes

    __method__ = "DarAnio"
    __parameter__ = "ninguno"
    __returns__ = "anio"
    __description__ = "metodo que permite regresar el anio"
    def DarAnio(self):
        # Aqui va mi codigo
        return self.anio 

    __method__ = "DarFecha"
    __parameter__ = "ninguno"
    __returns__ = "fecha"
    __description__ = "metodo que regresa la fecha digitada por el usuario"
    def DarFecha(self):
        return self.dia+'/'+self.mes+'/'+self.anio

