### How to execute

Development
```
00_path_params> ./scripts/deploy.sh
```

Production
```
export PRODUCTION=true
00_path_params> ./scripts/deploy.sh
```

Testing
```
tox -e pytest
```

### Generación de Artefactos

Instalar el paquete rpm si es necesario
```
sudo apt install rpm -y
```

Realizar una primera generación de un artefacto
```
python3 setup.py bdist --formats=rpm
```

Observe el contenido del archivo de especificación empleado para crear el artefacto
```
cat build/bdist.linux-armv7l/rpm/SPECS/gm_analytics.spec
```

Observe los archivos que han sido comprimidos dentro del artefacto
```
tar xfz dist/gm_analytics-0.1.0.dev20181009.tar.gz
ls dist/gm_analytics-0.1.0.dev20181009
```

A continuación se realizaran modificaciones para adicionar dependencias previas
a la instalación del artefacto, y acciones posteriores a la instalación

Cree nuevamente el artefacto, pero esta vez adicione un script posterior a la instalación del artefacto
```
python3 setup.py bdist_rpm --post-install="scripts/post_install_py3.sh"
```

Observe el contenido del archivo de especificación empleado para crear el artefacto. Note las diferencias en el archivo
con respecto a la primera generación del artefacto
```
cat build/bdist.linux-armv7l/rpm/SPECS/gm_analytics.spec
```

Cree nuevamente el artefacto, pero esta vez adicione dependencias previas a la instalación del artefacto
```
python3 setup.py bdist_rpm --requires="python3 python3-pip"
```

**Nota**: Puede adicionar la opción __--spec-only__ al comando anterior para generar unicamente el archivo de especificación sin la construcción del
artefacto. El archivo de especificación sera almacenado para este caso en el directorio **dist**

Observe el contenido del archivo de especificación empleado para crear el artefacto. Note las diferencias en el archivo
con respecto a la primera generación del artefacto
```
cat build/bdist.linux-armv7l/rpm/SPECS/gm_analytics.spec
```

Hasta este momento se han generado dos tipos de artefactos por separado, uno con una acción previa a la instalación y otro con una acción posterior.
Por medio del siguiente comando podrá obtener las dos funcionalidades en un solo artefacto.
```
python3 setup.py bdist_rpm --post-install="scripts/post_install_py3.sh" --requires "python3 python3-pip"
```

Es posible indicar el ejecutable de python a emplear para la construcción del artefacto como se muestra
a continuación
```
python3.6 setup.py bdist_rpm --post-install="scripts/post_install_py3.sh" --python="/usr/bin/python3.6"
```

Puede añadir mas opciones consultando las parametros para el argumento bdist_rpm, o también puede editar el archivo de especificación manualmente y
realizar la creación del artefacto a partir de él.
```
python3 setup.py bdist_rpm -h
```

### Actividad
Determine si es necesario adicionar un parametro a la construcción del artefacto para la instalación de las dependencias del servicio de python implementado