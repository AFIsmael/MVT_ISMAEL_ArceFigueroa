# Instrucciones para ejecutar este proyecto

### Clonar el proyecto
```bash
git clone https://github.com/AFIsmael/MVT_ISMAEL_ArceFigueroa

cd MVT_ISMAEL_ArceFigueroa

```

### Crear y activar entorno virtual (Windows)
```bash
python -m venv venv
.\venv\Scripts\activate
```

### Crear y activar entorno virtual (Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```

### Instalar las dependencias del proyecto
```bash
pip install -r requirements.txt
```

### Activar entorno virtual
(Windows)
```bash
.\venv\Scripts\activate
```

(Linux)
```bash
source venv/bin/activate
```

### Instalar las dependencias del proyecto
```bash
pip install -r requirements.txt
```

### Navegar hacia la carpeta del proyecto `MVT`
```bash
cd MVT
```

### Se ejecuta la migración para crear la base de datos con la que trabajará nuestro proyecto de Django
```bash
python manage.py migrate
```

### Se levanta el servidor de Django que expone el servicio por el localhost en el puerto 8000 por defecto `http://127.0.0.1:8000/` 
```bash
python manage.py runserver
```

### Si queremos levantar el servidor de Django en otro puerto lo especificamos de la siguente manera. e.g. `http://127.0.0.1:8001/`
```bash
python manage.py runserver 8001
```


### Se crea el super usuario para nuestro proyecto de Django, **Solo si no se ha creado**
```bash
python manage.py createsuperuser
```
Ingrese `Username`, `Email address` y `Password` 


### Recordar que para que cargen de manera adecuada los templates deben actualizar su nombre de usuario en el path que está en el módulo `settings.py` ubicado en `MTV\MTV\settings.py`

```bash
        'DIRS': [
            " ***copiar el path de la carpeta templates*** (MVT_ISMAEL_ArceFigueroa/MTV/templates/) click derecho - Copy Path"
        ],
```



# Funcionalidades de la pagina

## Crear nuevo familiar

- navegar al endpoint create_family e insertar los datos solicitados de la siguiente manera.
```bash
http://127.0.0.1:8000/create_family/<str:name>/<str:last_name>/<int:dni>/<str:date_birth>
```
- el formato del entry en el dato (date_birth) es %Y-%m-%d


## visualizar la lista de familiares

- navegar al endpoint family/relatives.

```bash
http://127.0.0.1:8000/family/relatives
```
- o simplemente dar click en el Item Family en la esquina superior derecha del Home.

