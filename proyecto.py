
import collections
import string

operadores = {
    '+': 'Suma',
    '=': 'igual',
    '-': 'Resta',
    '*': 'Multiplicación',
    '/': 'División',
    '%': 'Módulo',
    '==': 'Igual a',
    '!=': 'Diferente de',
    '<': 'Menor que',
    '>': 'Mayor que',
    '<=': 'Menor o igual que',
    '>=': 'Mayor o igual que',
    '|': 'OR ',
    '<<': 'Desplazamiento izquierdo',
    '>>': 'Desplazamiento derecho'
}
tipos_de_datos = {'int':'Entero', 'float':'flotante', 'string':'cadena', 'void':'void'}
palabras_reservadas = {
    'if': 'if',
    'while': 'bucle while',
}

operadores_llave=operadores.keys()
tipos_de_datos_llave=tipos_de_datos.keys()
palabras_reservadas_llave=palabras_reservadas.keys()



class Tabla_Simbolos:
    def __init__(self):
        self.simbolos = {}
        self.funciones = {}

#------ Métodos para variables------------------------------------------------------
    def agregar_simbolo(self, nombre, tipo, valor=None):
        self.simbolos[nombre] = {'tipo': tipo, 'valor': valor}

    def buscar_simbolo(self, nombre):
        return self.simbolos.get(nombre, {'tipo': None, 'valor': None})

    def obtener_nombres(self):
        return list(self.simbolos.keys())

    def obtener_simbolos(self):
        return [(nombre, simbolo['tipo'], simbolo['valor']) for nombre, simbolo in self.simbolos.items()]

    def obtener_tipo(self, nombre):
        simbolo = self.buscar_simbolo(nombre)
        return simbolo['tipo'] if simbolo else None

    def obtener_valor(self, nombre):
        simbolo = self.buscar_simbolo(nombre)
        return simbolo['valor'] if simbolo else None



#----------------------- Métodos para funciones--------------------------------------------------------
    def agregar_funcion(self, nombre, tipo_retorno):
        self.funciones[nombre] = {'tipo_retorno': tipo_retorno}

    def buscar_funcion(self, nombre):
        return self.funciones.get(nombre, {'tipo_retorno': None})

    def obtener_nombres_funciones(self):
        return list(self.funciones.keys())

    def obtener_funciones(self):
        return [(nombre, funcion['tipo_retorno']) for nombre, funcion in self.funciones.items()]

    def obtener_tipo_retorno_funcion(self, nombre):
        funcion = self.buscar_funcion(nombre)
        return funcion['tipo_retorno'] if funcion else None






def es_numero(palabra):
    try:
        float(palabra)
        return True
    except ValueError:
        return False   

  



import re  

#def corte_palabras(fuente):
 #   coincidencias = re.split(r'(\W+)', fuente)
  #  coincidencias = [coincidencia for coincidencia in coincidencias if coincidencia.strip()]  # Filtramos espacios en blanco
   # return coincidencias


#def corte_palabras(oracion):
 #   palabras_y_simbolos = re.findall(r'\b\w+\b|\W', oracion)
  #  return palabras_y_simbolos

def corte_palabras(oracion):
    palabras_y_simbolos = re.findall(r'\b\w+\b|\S', oracion)
    return palabras_y_simbolos

class AnalizadorSemantico:
    def __init__(self):
        self.tabla_de_simbolos = Tabla_Simbolos()  # Asumo que TablaDeSimbolos es la clase que estás utilizando

    def leer_archivo_texto(self, nombre_archivo):
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
            return contenido
        except FileNotFoundError:
            print(f"Error: El archivo '{nombre_archivo}' no se encuentra.")
            return None
        except Exception as e:
            print(f"Error inesperado al leer el archivo: {str(e)}")
            return None

    def analizar_codigo(self, codigo):
     
        lineas = codigo.split('\n')

        for numero_linea, linea in enumerate(lineas, start=1):
        

            self.analizar_linea(linea, numero_linea)


    def analizar_linea(self, linea, numero_linea):
        
        palabras = corte_palabras(linea.strip())
        conta = len(palabras)
         
        for posicion in range(conta):
         
            palabra_actual = palabras[posicion].strip()


            if palabra_actual in tipos_de_datos_llave and "=" in palabras:
                
                if posicion+1<conta and posicion+2<conta:
                    if palabras[posicion+2]=="=" :
                        k= palabras[posicion+3]


                     
                        if palabra_actual == "int" and es_numero(k):
                               self.tabla_de_simbolos.agregar_simbolo(palabras[posicion+1],palabras[posicion],palabras[posicion+3])
                             

                        elif palabra_actual == "string" and  es_numero(k)==False  and k!="":
                                    self.tabla_de_simbolos.agregar_simbolo(palabras[1],palabras[0],palabras[4])
                                    print ( self.tabla_de_simbolos.obtener_simbolos())

                        elif palabra_actual == "float" and  es_numero(k) :
                                    self.tabla_de_simbolos.agregar_simbolo(palabras[1],palabras[0],palabras[3])

                        else:
                            #elif palabra_actual == "void" and  es_numero(k)==False  and k!="" or es_numero(k)==True and '(' is not palabras:
                                    print(f"Error - Línea {numero_linea}: tipo de dato '{palabras[posicion].strip()}'  incorrecta")
                                    
                    



               # print(self.tabla_de_simbolos.obtener_simbolos())

            elif  palabra_actual in self.tabla_de_simbolos.obtener_nombres() and "=" in palabras :  # buscar si la palabra se encuentra en el dicionario
                     
         

                if posicion+1<conta and posicion+2<conta: # valorar si la busqueda es correcta
                    if palabras[posicion+1]=="=" :
                        k= palabras[posicion+2]
                            
                        if self.tabla_de_simbolos.obtener_tipo(palabra_actual) == "int" or  self.tabla_de_simbolos.obtener_tipo(palabra_actual) == "float" and k=='"' :
                                print(f"Error - Línea {numero_linea}: Variable '{palabras[posicion].strip()}' asignacion incorrecta")
                                 
                             
                        elif self.tabla_de_simbolos.obtener_tipo(palabra_actual) == "string" and  es_numero(k)==True: 
                            print(f"Error - Línea {numero_linea}: Variable '{palabras[posicion].strip()}' asignacion incorrecta")
                             
        

            elif  palabra_actual!= "" and  "=" in palabras and palabra_actual not in self.tabla_de_simbolos.obtener_nombres() and palabra_actual not in palabras_reservadas_llave and "(" not in palabras :
                
                if posicion+1<conta:
                    if palabras[posicion+1]=="=" :
                        print(f"Error - Línea {numero_linea}: Variable '{palabras[posicion].strip()}' NO ESTA DECLARADO") 



# ----------------------------esto if es de la declaracion de metodos--------------------------------------------

            elif   "(" in palabras and ")" in palabras  :
                
                if palabra_actual in tipos_de_datos_llave: 

                    if palabra_actual == "int" and  palabras[ posicion+2]== "(": 
                            self.tabla_de_simbolos.agregar_funcion(palabras[1],palabras[0])
                            
       
                    elif palabra_actual == "string" and  palabras[ posicion+2]=="(" :    
                            self.tabla_de_simbolos.agregar_funcion(palabras[1],palabras[0])
                           


                    elif palabra_actual == "float" and  palabras[ posicion+2] =="(": 
                            self.tabla_de_simbolos.agregar_funcion(palabras[1],palabras[0])
                            

                  
                    elif palabra_actual == "void" and  palabras[ posicion+2] =="(": 
                            self.tabla_de_simbolos.agregar_funcion(palabras[1],palabras[0])
                            
            #--------------------------------------------------------------------------------------------- 
                    k= palabras[posicion+2]# asignar en la tabla varaiable que esta en una funcion
 
                    if palabra_actual == "float" and  (k=="," or k==")"):
                            self.tabla_de_simbolos.agregar_simbolo(palabras[posicion+1],palabra_actual,)
                    
                    
                    if palabra_actual == "int" and (k=="," or k==")"):
                            self.tabla_de_simbolos.agregar_simbolo(palabras[posicion+1],palabra_actual,)
                            
                    
                    if palabra_actual == "string" and (k=="," or k==")"):
                            self.tabla_de_simbolos.agregar_simbolo(palabras[posicion+1],palabra_actual,)
                    
                    if palabra_actual == "void" and (k=="," or k==")"):  
                          print(f"Error - Línea {numero_linea}: asignacion {palabra_actual}  invalida")
          
            if palabra_actual in palabras_reservadas_llave and "(" in palabras and ")" in palabras  :
                 k= palabras[posicion+2]
                 j=palabras[posicion+4]
                
                # if  self.tabla_de_simbolos.buscar_simbolo(j) and k in self.tabla_de_simbolos.obtener_simbolos:
                 if es_numero(k) and es_numero(j):

                    if "=" in palabras :
                      print(f"Error - Línea {numero_linea}:  aignacion invalida")   
                   
                     
                 elif es_numero(k)==False and es_numero(j)==False:
                     
                     if self.tabla_de_simbolos.obtener_tipo(k) and  self.tabla_de_simbolos.obtener_tipo(j) :
                         print(self.tabla_de_simbolos.obtener_tipo(k))
                         print(self.tabla_de_simbolos.obtener_tipo(j))
                     
                     else:
                         print(f"Error - Línea {numero_linea}:  diferencia de variable")   
                
                 elif  es_numero(k)==False and  es_numero(j)==True:
                    

                    if self.tabla_de_simbolos.obtener_tipo(k)=="string" or self.tabla_de_simbolos.obtener_tipo(k)==None:   
                            print(f"Error - Línea {numero_linea}:  DIFERENCIAS EN LA DECLARACION DE VARIABLES") 
                    
                

                    
                 elif  es_numero(k)==True and  es_numero(j)==False:
                    if self.tabla_de_simbolos.obtener_tipo(j) !="int" :
                        print(f"Error - Línea {numero_linea}:  DIFERENCIAS EN LA DECLARACION DE VARIABLES") 
            
            if palabra_actual == "return" :
                 if conta>1:
                     nombre=self.tabla_de_simbolos.obtener_nombres_funciones()
                     if len(nombre)>0: 

                        if self.tabla_de_simbolos.buscar_funcion(nombre[0])!=None:
                       
                           tipo_funcion=self.tabla_de_simbolos.obtener_tipo_retorno_funcion(nombre[0]) 
                           nombre_retorno=self.tabla_de_simbolos.obtener_tipo(palabras[1])

                           if tipo_funcion !=None and nombre_retorno !=None:
                                
                                if(nombre_retorno!=tipo_funcion): # si son diferentes  el retorno es error
                                    print(f"Error - Línea {numero_linea}:  valor de retorno no coincide con la declaración de funcion")
                          
                           elif  (tipo_funcion=="int" or tipo_funcion=="float") and palabras[1]=='"':
                                print(f"Error - Línea {numero_linea}:  valor de retorno no coincide con la declaración de funcion")
                                                                 
                           elif  tipo_funcion=="String"  and  es_numero(palabras[1]):
                                    print(f"Error - Línea {numero_linea}:  valor de retorno no coincide con la declaración de funcion")

                           elif  tipo_funcion=="void":
                                    print(f"Error - Línea {numero_linea}:  valor de retorno no coincide con la declaración de funcion")


                        else:
                            print(f"Error - Línea {numero_linea}:  valor de retorno no coincide con la declaración de funcion") 
                        
                       
         #-----------------------------------con los while y if -------------------------------------------------

     
         
         # self.tabla_de_simbolos.agregar_simbolo(palabras[])

 


if __name__ == "__main__":
    a = AnalizadorSemantico()

   
    nombre_archivo = "m.txt"

    contenido_codigo = a.leer_archivo_texto(nombre_archivo)

    if contenido_codigo:
        a.analizar_codigo(contenido_codigo)
    else:
        print("No se pudo analizar el código debido a errores en la lectura del archivo.")

    



   