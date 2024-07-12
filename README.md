# TP-Testing
Trabajo Practico Obligatorio Testing

## Getting Started

Las siguientes instrucciones premiten obtener una copia del proyecto, setear el entorno y poder correrlo localmente para desarollo de nuevas funcionalidades o testing.

### Prerequisitos

> #### Python 
>
> - Ingresar a la sección Descargas de [Python](https://www.python.org/downloads/).
> - Descargar la última versión o >= to 3.8.0.
> - Instalar Python y setear las variables de entorno.
> - Verificar que se haya instalado correctamenete con *python --version* desde cualquier consola/terminal (PowerShell, CMD, bash).
> ```
> PS C:\Users\you_user> python --version
> Python 3.8.0
> ```

> #### Entorno virtual de Python
>
> Los entornos virtuales de Python son útiles para evitar conflictos entre distintos proyectos que pueden utilizar distintas versiones de librerías.
> - Ubicado desde una consola en la raíz del proyecto, ejecutar el siguiente comando:
> ```
> python -m venv .venv
> ```
> - Al finalizar, se debería haber creado una carpeta con nombre " v" la raíz del proyecto.
> - Para acitvar el entorno virtual, ejecutar el siguiente comando:
> -- En Linux bash/zsh -> ``` $ source .venv/bin/activate ```
> -- En Windows cmd.exe -> ``` .\.venv\Scripts\activate.bat ```
> -- En Windows PowerShell -> ``` .\.venv\Scripts\Activate.ps1 ```
> - Para indagar más sobre el tema, ingresar a la siguiente url [venv](https://docs.python.org/3/library/venv.html).


### Instalación

>
> #### Python Libs
> - Es necesario instalar en el proyecto los módulos/librerías que se usan como dependencias desde el archivo *requirements.txt*, luego de activar el virtual enviroment vas a ejecutar el siguiente comando:
> ```
> (.venv) PS C:\Users\you_user\you_workspace\TP-Testing> pip install -r requirements.txt
> ```
> - Finalizada la instalación, se puede verificar la instalación de los módulos con el comando *pip freeze* y se debe observar lo siguente:
> ```
> (.venv) PS C:\Users\you_user\you_workspace\TP-Testing> pip freeze
> ...
> allure-pytest-bdd==2.8.22
> allure-python-commons==2.8.13
> pytest==5.4.1
> selenium==3.141.0
> ...
>```

### Ejecucion

>
> #### Python Libs
> - Desde la terminal: Activar el venv y ejecutar el siguiente comando 
> ```
> (.venv) PS C:\Users\you_user\you_workspace\TP-Testing> python -m pytest .\tests_demo_blaze.py
> ```
> - Desde pycharm: Botón derecho sobre el archivo tests_demo_blaze.py y elegir la opción "Run"
