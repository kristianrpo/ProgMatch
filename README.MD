### Explicación estructura del proyecto
Basados en el principio de la arquitectura limpia y la convergencia de la misma con la arquitectura que nos proporciona el framework de Django, obtenemos:
- **Carpeta 'components'**: Aquí se encuentran todas las aplicaciones/componentes creados del proyecto.
- **Carpeta 'config'**: Aquí se encuentra la configuración del proyecto como tal, sus urls iniciales, etc. la carpeta 'settings' dentro de esta, parte la configuración del proyecto en dos:
    - **'base.py'**: Se encuentra la configuración que no cambia para ningun integrante del equipo de desarrollo, aquí se encuentran dependencias fijas y necesarias para el correcto funcionamiento del proyecto.
    - **'local.py'**: Se encuentra la configuración cambiante, si es el caso,  para cada integrante del equipo de desarrollo, ya que por ejemplo, para casos como lo son la base de datos, probablemente desde el local de cada computador de los desarrolladores existirá una conexión diferente a la base de datos (si se utiliza una distinta a sqlite).
- **'data'**: Es la "capa" o la carpeta donde se almacena todos los datos del negocio, en este caso, unicamente la base de datos.
- **'domain'**: Es el corazón de la aplicación y está aislado de cualquier dependencia ajena a la logica o los datos del negocio. En su interior, se encuentran dos carpetas:
    - **'entities'**: Aquí se define la estructura de la base de datos, es decir, las tablas correspondientes que van a almacenar la información necesaria para el correcto funcionamiento de la aplicación. Para esto, utilizamos unica y exclusivamente el ORM de Django que permite traducir nuestro codigo en python a los distintos lenguajes de base de datos. Basicamente, se define lo que normalmente en el framework definiriamos en el archivo "models.py" de cada componente. Pero ahora, los definiremos dentro de esta carpeta, y luego se instanceará al archivo "models.py" de cada componente.
    - **'useCases'**: Aquí se define la parte logica de la aplicación. Es lo que en el framework definiriamos en el archivo "views.py" de cada componente. Pero ahora, los definiremos dentro de esta carpeta, y luego se instanceará al archivo "views.py" de cada componente.
- **'presentation'**: Es la capa que interactua con el usuario. Dentro de esta, se encuentran la carpeta:
    - **'UI'**: Es todo lo que ve el usuario de la aplicación, esta carpeta a su vez, contiene:
        - **'staticFiles'**: Aquí se guardara todos los archivos estáticos tales como los CSS, JS e imagenes de cada uno de los componentes. Son archivos que se definen inicialmente y no cambian durante la ejecución de la aplicación.
        - **'templates'**: Se encuentran todos las plantillas HTML que se presentan al usuario en cada una de las secciones de la aplicación
### Generalidades a tener en cuenta
- Se hará uso del "lowerCamelCase" para la escritura de todo el proyecto.
- Se documentará el proyecto con el formato "Docstring", donde en general, se busca tener en cuenta las siguientes aspectos (informese más en el siguiente link: https://pywombat.com/articles/docstring-python):
        - Para poder documentar nuestro código vamos a colocar, en la primera línea del cuerpo de la función, un comentario con triple comillas simples, o tiple comillas dobles. Por convención será triple comillas dobles.
        - Este comentario deberá cumplir con los siguientes puntos.
            - La primera línea debe poseer una breve descripción del funcionamiento del código.
            - Las descripciones deben comenzar con mayúscula y finalizar con punto.
            - Si existen más líneas, la segunda deberá ser un espacio en blanco, de tal forma que sea fácil distinguir entre la descripción y el resto del comentario.
            - Las siguientes líneas deben ser uno o más párrafos que describan las convenciones de llamada del objeto.
            - A este de comentario los conoceremos como docstring (documentation string) Un comentario con triple comillas dobles, o simples, en la primera línea del bloque del objeto.
- Como generalidad, y aplicando los conceptos de codigo limpio, se recomienda utilizar **clases genericas de django**, las cuales nos permiten obtener un codigo mas organizado y haciendo uso de la programación orientada objetos que nos brinda el framework (siempre que exista la posibilidad de utilizarlas en la parte logica de la aplicación). Además, permite mantener el codigo simple y entendible para el equipo de desarrollo.
- Reutilizar codigo siempre en la medida de lo posible, aplicando el principio DRY.
- Cada uno cree su propio entorno virtual, activenlo y descarguen las dependencias, de la siguiente forma:
    ```python -m venv venv```
    ```./venv/Scripts/activate```
    ```pip install -r requirements.txt```
- A la hora de crear una aplicación/componente en Django por algún motivo, en el archivo 'base' en config/settings, en 'INSTALLED_APPS', agregar 'components.nombre_nueva_aplicación', y además, dentro de la aplicación creada, en el archivo "apps.py", modificar la variable "name" por name = 'components.nombre_nueva_aplicación'.