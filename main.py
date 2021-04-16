# Expresiones regulares (regular expressions):
'''
El código anterior importa el paquete <re> y
compila un patrón de expresión
regular que puede coincidir
con al menos uno o más caracteres de espacio.
'''
# 1 y 2.

# importamos las "regular expressions":
import re   
regex = re.compile('\s+')


# 3.

# Importamos el .txt y lo convertimos a str con <with...>
with open('ejemplo.txt', 'r') as f:
  # con el replace quitamos el \n que aparece al importar el texto:
  ejemplo = f.read().replace('\n', ' ') # <- se deja el espacio para que no se sobrepongan valores


# dividir el texto en 1 o más caracteres de espacio:

'''
re.split ('\s+', texto)
el siguiente codigo me ahorra digitar mas codigo y mas entendible
para mi.
'''

resultado0 =regex.split(ejemplo)

# Imprimimos el resultado:
print(resultado0)

# 4.

'''
Supongamos que desea extraer todos los números del curso,
es decir, los números 101, 205, 189,.....
solo del texto anterior.
¿Como hacer eso?
'''
## 4.1

# Encontramos todos losnumeros dentro del texto:

'Explicado en el rm en el literal 4.1'
regex_num = re.compile('\d+')

# Listas de todos los digitos del str "ejemplo":
lista_num = regex_num.findall(ejemplo)

print(lista_num)

# 4.2

# compila la expresión regular y busca el patrón:
regex_num = re.compile('\d+')
busca_digitos = regex_num.search(ejemplo)

# Posición inicial en la que se encuentra el primer digito (Numero):
print('Posición Inicial: ', busca_digitos.start())

# Posición Final en la que se encuentra el primer digito (Numero):
print('Posición Final: ', busca_digitos.end())

# Imprime el primer numero encontrado:
print(ejemplo[busca_digitos.start():busca_digitos.end()])

# Alternativamente, puede obtener el mismo resultado utilizando el método group () del objeto de coincidencia:
print('Soy el mismo resultado -> ',busca_digitos.group())

# 5.

with open('Ejemplo1.txt', 'r') as f:
  # con el replace quitamos el \n que aparece al importar el texto:
  ejemplo1 = f.read().replace('\n', ' ') # <- se deja el espacio para que no se sobrepongan valores


# sustituir un texto por otro
'''
Del texto anterior, quiero igualar todos los espacios extra
y poner todas las palabras en una sola línea.

Para ello,
basta con utilizar regex.sub para sustituir el patrón '\s+'
por un solo espacio ' '.

# Ahorrando lineas con el codigo siguiente:
regex = re.compile('\s+')
print(regex.sub(' ', text))
'''
# Todo el texto que estaba por lienas diferentes ahora esta en una sola linea:
print(re.sub('\s+', ' ', ejemplo1))

# -> 1. extrae todos los nuemros de las materias:
all_num =re.findall('[0-9]+', ejemplo)
print(all_num)

# -> 2. extrae todos los codigos de las materias:
'NO enlista a las tildes'
all_cod = re.findall('[A-Z]{3}', ejemplo)
print(all_cod)

# ->  3. extrae todos los nombres de las materias:
'NO enlista a las tildes'
all_name = re.findall('[A-Za-z]{4,}', ejemplo)
print(all_name)

'''
Ahora tuve que escribir 3 líneas separadas para obtener los elementos individuales.
Pero hay una manera mejor. Regex Groups

Como todas las entradas tienen el mismo patrón,
puedes construir un patrón unificado para toda la entrada del curso
y poner las partes que quieres extraer dentro de un par de corchetes ().
'''
patron_materias = '([0-9]+)\s*([A-Z]{3})\s*([A-Za-z]{4,})'
# Mejor el zen en python:
print('--------------Mejora el zen de python--------------')
patron_materias_listas = re.findall(patron_materias, ejemplo)
print(patron_materias_listas)

