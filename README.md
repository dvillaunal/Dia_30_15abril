# Regular Expressions:
[Texto estudiado, en el cual es sacada toda la información](https://docs.python.org/3/library/re.html)

## 1. Introducción a las expresiones regulares:

Las expresiones regulares, también llamadas ___regex___, se implementan en prácticamente todos los lenguajes informáticos. En Python, se implementa en el módulo estándar `re`.

* Nota:
  Se usa ampliamente en el procesamiento del lenguaje natural, aplicaciones web que requieren validar la entrada de cadenas (como la dirección de correo electrónico) y casi la mayoría de los proyectos de ciencia de datos que involucran la minería de texto.

## 2. ¿Qué es un patrón de expresiones regulares y cómo compilar uno?

Un patrón de expresiones regulares es un lenguaje especial que se usa para representar texto, números o símbolos genéricos, por lo que se puede usar para extraer textos que se ajustan a ese patrón.
Un ejemplo básico es `'\s+'.`

Aquí `'\s'` coincide con cualquier carácter de espacio en blanco. Al agregar una `'+'` notación al final, el patrón coincidirá con al menos 1 o más espacios. Por lo tanto, este patrón también coincidirá con los `'\t'` caracteres de tabulación pares .

## 3. ¿Cómo dividir una cadena separada por una expresión regular?

Tengo tres elementos del curso en el `ejemplo0.txt`:
 > N° de la curso | Código del curso | Nombre del curso. 
 
Los espacios entre las palabras no son iguales.

Quiero dividir estos tres elementos del curso en unidades individuales de números y palabras. ¿Como hacer eso?

Esto se puede dividir de dos formas:
1. Mediante el método `re.split`.
2. Llamando al método `.split` del objeto `regex`.

## 4. Encontrar coincidencias de patrones usando findall, search y match:

### 4.1 ¿Qué hace re.findall ():

En el código anterior, el carácter especial `'\d'` es una expresión regular que coincide con cualquier dígito.

Agregar un `'+'` símbolo obliga a la presencia de al menos 1 dígito para poder ser encontrado.

** =>Resultado del `r.compile('\d+')` :**
  ~~~
  > print(lista_num)
  ['101', '205', '189', '201', '653', '234', '934', '236']
  ~~~

*  Nota:
  Similar a `'+'` , hay un `'*'` símbolo que requiere 0 o más     dígitos para ser encontrado. Prácticamente hace que la    presencia de un dígito sea opcional para hacer una        coincidencia.

  Finalmente, el método findall extrae todas las apariciones de 1 o más dígitos del texto y las devuelve en una lista.

### 4.2 re.search() vs re.match():

Como su nombre indica, `regex.search()` busca el patrón en un texto dado.

Pero a diferencia de `.findall()`, que devuelve las partes coincidentes del texto como una lista, `regex.search()` devuelve un objeto coincidente particular que contiene las posiciones inicial y final de la primera ocurrencia del patrón.

Del mismo modo, `regex.match()` también devuelve un objeto coincidente. Pero la diferencia es que requiere que el patrón esté presente al principio del propio texto.

## 5. ¿Cómo sustituir un texto por otro usando expresiones regulares?:

Para reemplazar textos, use el `.regex.sub()` :

**-> Nota:** Texto extraido de [Generador de Textos](https://www.blindtextgenerator.com/es)

Del texto anterior, quiero igualar todos los espacios extra y poner todas las palabras en una sola línea.

Para ello, basta con utilizar `regex.sub` para sustituir el patrón `'\s+'` por un solo espacio ' '.

## 6. Grupos de expresiones regulares:

Los grupos de expresiones regulares son una función muy útil que permite extraer los objetos de coincidencia deseados como elementos individuales.
Supongamos que quiero extraer el número de curso, el código y el nombre como elementos separados.

* Explicación  `lines 99-109`:
 Compilé 3 expresiones regulares separadas, una para el número de materia, el código y el nombre:

 1. Para el número de las materias, el patrón ``[0-9]+`` indica que debe coincidir con todos los números del 0 al 9. Añadiendo el símbolo ``+`` al final se busca al menos una ocurrencia de los números 0-9. Si sabe que el número del curso tendrá seguramente exactamente 3 dígitos, el patrón podría haber sido ``[0-9]{3}`` en su lugar.
 
 2. Para el código de la materia, puede adivinar que ``'[A-Z]+'`` coincidirá exactamente con n apariciones consecutivas de los alfabetos de la A a la Z (MAYUSCULAS).

 3. Para el nombre del curso, ``'[A-Za-z]{4,}'`` buscará los alfabetos mayúsculos y minúsculos a-z, suponiendo que todos los nombres de las materias tendrán al menos 4 o más caracteres.


