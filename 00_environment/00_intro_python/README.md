### Introducción al lenguaje Python
Universidad ICESI  
Curso: Sistemas Operativos  
Docente: Daniel Barragán C.  
Tema: Introducción a Python  
Correo: daniel.barragan at correo.icesi.edu.co

### Objetivos
* Emplear algunas instrucciones del lenguaje Python
* Ejecutar comanos de consola desde Python

### Introducción
Python es un lenguaje de programación multiparadigma, que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional. Es un lenguaje interpretado, usa tipado dinámico y es multiplataforma.

### Instalación

En esta guía se asume que cuenta con una máquina virtual con el sistema operativos CentOS 6.x instalado. Las versiones de CentOS incluyen Python por defecto.

### Desarrollo

#### Crear un usuario

Cree un usuario con nombre python_user

```
# adduser python_user
# passwd python_user
```

#### Verificar Python

Verifique la instalación de Python

```
# su python_user
$ python -V
```

#### Consola interactiva

Abra la consola intectiva y practique algunos comandos.

```
$ python
print "hello world"
exit()
```

#### Scripts con Python

Cree un archivo de nombre greeting.py

```python
import sys
print "hi " + sys.argv[1]
print "salut %s" % (sys.argv[1])
```

```
$ python greeting.py "daniel"
```

#### Funciones en Python

Cree un archivo de nombre operations.py

```python
def sub(val_a=0, val_b=0):
    res = val_a - val_b
    return res

def sum(*ops):
    res = 0
    for op in ops:
        res += op
    return res

def show(**cons):
    for key, value in cons.iteritems():
        print "%s == %s" % (key, value)

def filter(*ops):
    list = [x ** 2 for x in ops if x % 2 == 0]
    return list

val_a = 1
val_b = 2
val_c = 3
cons_pi = 3.14
cons_e = 2.71
ans = sub(val_a=1, val_b=2)
print "result =" + str(ans)
ans = sum(val_a, val_b, val_c)
print "result = " + str(ans)
ans = filter(val_a, val_b, val_c)
print "result = " + str(ans)
show(cons_pi=3.14, cons_e=2.71)
```

**Nota:** Puede encontrar mas información sobre el uso de * y ** en python buscando como *args y **kargs

#### Obteniendo el espacio usado por /home

Cree un archivo de nombre disk_space.py

```python
from subprocess import Popen, PIPE
df_process = Popen(["df","-h","/home"], stdout=PIPE, stderr=PIPE)
tail_process = Popen(["tail","-1"], stdin=df_process.stdout, stdout=PIPE, stderr=PIPE)
awk_process = Popen(["awk","{print $4}"], stdin=tail_process.stdout, stdout=PIPE, stderr=PIPE)
print awk_process.communicate()[0]
```

```
$ python disk_space.py
```

#### Conversiones en Python

Cree un archivo de nombre convert.py

```python
number_as_text = ["1"]
number_as_int = int(number_as_text[0])
numer_output = number_as_int + 1
print numer_output
```

```
$ python convert.py
```

#### Ciclos en Python

Cree un archivo de nombre iterate.py

```python
number_list = []      
threshold = 3      

for i in range(8):
  number_list.append(i)

for value in number_list:
  if value > threshold:
    print value
```

```
$ python iterate.py
```

#### Leer archivo en Python

Cree los siguientes archivos con nombre ip_addresses.txt y scan.py

```
127.0.0.1
127.0.0.1
```

```python
from subprocess import Popen, PIPE

with open('ip_addresses.txt', 'r') as f:
    data = f.readlines()

    for ip_address in data:
      ping_process = Popen(["ping","-c","1",ip_address.rstrip()], stdout=PIPE, stderr=PIPE)
      print ping_process.communicate()[0]
```

```
$ python scan.py
```

#### Escribir en un archivo en Python

Cree el siguiente archivo con nombre status.py

```python
with open("status.txt", "w") as f:
	f.write("All checks Running")
```

```
$ python status.py
```

### Actividades

#### Ejecutando cualquier comando en consola
Realice un script en python que reciba como parametro una cadena de texto con un comando (el comando debe tener argumentos de entrada) y lo ejecute en la consola. Debe usar subprocess.

