### Introducción al lenguaje Python
Universidad ICESI  
Curso: Sistemas Operativos  
Docente: Daniel Barragán C.  
Tema: Estructura para proyectos con Flask  
Correo: daniel.barragan at correo.icesi.edu.co

### Objetivos
* Conocer y emplear una estructura propuesta para la implementación de proyectos con Flask

### Introducción
La adecuada estructura de un proyecto es importante para garantizar la escalabilidad del mismo cuando sus modulos se tornan mas complejos

### Instalación

En esta guía se asume que cuenta con una máquina virtual con el sistema operativos CentOS 7.x instalado. Las versiones de CentOS incluyen Python por defecto. Se debe realizar la instalación y configuración de MySQL junto con las librerías de desarrollo.

### Desarrollo

#### Base de datos

En el directorio scripts, encontrara los scripts para la creación de los esquemas en la base de datos. Desde el directorio raíz del repositorio ejecute el siguiente comando:

```
# ./database_cli.sh
```

#### Proyecto de Flask

En este repositorio encontrará un ejemplo modificado del presentado en el blog y repositorio de github:   

```
http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/  
https://github.com/postrational/rest_api_demo
```

Para la ejecución de la aplicación dígite los siguientes comandos desde el directorio raíz del repositorio:

```
$ export PYTHONPATH=.:$PYTHONPATH
$ python rest_api_demo/app.py
```

Abra un navegador en la dirección **http://localhost:8888/api**, podrá visualizar la documentación para los endpoints implementados. Cancele la ejecución del script presionando la combinación de teclas **CTRL+C**.

### Actividades
1. Realice las modificaciones necesarias para adicionar la fecha actual automaticámente al crear un usuario.
2. Realice las modificaciones necesarias para adicionar el campo identificación a los usuarios.
3. Adicione un endpoint al proyecto tomando como base el repositorio original de michal karzynski
