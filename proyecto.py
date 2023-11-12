
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
                self.tabla_de_simbolos.agregar_simbolo(palabras[1],palabras[0],palabras[3])
               # print(self.tabla_de_simbolos.obtener_simbolos())

         elif  palabra_actual in self.tabla_de_simbolos.obtener_nombres() and "=" in palabras:
                     
                   # print("palabra :["+palabra_actual +" ]se encuente en el toque")# hacer una segregacion de informacion
               
                    if posicion+1<conta and posicion+2<conta:
                        if palabras[posicion+1]=="=" :
                            k= palabras[posicion+2]
                            
                            if self.tabla_de_simbolos.obtener_tipo(palabra_actual) == "int" and k=='"' :
                                 print(f"Error - Línea {numero_linea}: Variable '{palabras[posicion].strip()}' asignacion incorrecta")
                                 
                             
                             
                  


          
         elif  palabra_actual!= "" and  "=" in palabras and palabra_actual not in self.tabla_de_simbolos.obtener_nombres():
                
             if posicion+1<conta:
                if palabras[posicion+1]=="=" :
                    print(f"Error - Línea {numero_linea}: Variable '{palabras[posicion].strip()}' NO ESTA DECLARADO") 


                
               

         # self.tabla_de_simbolos.agregar_simbolo(palabras[])

 


if __name__ == "__main__":
    a = AnalizadorSemantico()

   
    nombre_archivo = "m.txt"

    contenido_codigo = a.leer_archivo_texto(nombre_archivo)

    if contenido_codigo:
        a.analizar_codigo(contenido_codigo)
    else:
        print("No se pudo analizar el código debido a errores en la lectura del archivo.")

    



   