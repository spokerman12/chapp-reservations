# chapp-reservations

Este programa es una prueba de código solicitada por Chapp Solutions.

## Para ejecutar el programa:

Puedes visitar [https://chapp-reservations.herokuapp.com](https://chapp-reservations.herokuapp.com)

Si prefieres ejecutarlo localmente:

1. Clona este repo
2. Crea y activa un [entorno virtual de Python](https://virtualenv.pypa.io/en/latest/) (opcional, recomendado). Debes usar  Python >= 3.7.12
3. `pip install -r requirements.txt`
4. `python manage.py runserver`
5. Abre [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en tu navegador.

Las credenciales de administrador fueron hechas llegar por correo.

Puedes ejecutar las pruebas con `python manage.py test`.
También se ha habilitado CI/CD en Github.

## Argumentos:

- Suelo tomar en cuenta la escalabilidad en el diseño del código. Sin embargo, también valoro la visión de producto. Por ello esta es una aplicación que no utiliza una API entre los template y el backend, lo que es el deber ser si se quiere trabajar seriamente en este programa.
- Usé Django 3.2 porque tiene LTS
- Apunté a entregar algo completo y que funcione. Aún así, considero que hay muchas mejoras posibles, como por ejemplo:
    - Refactorizaciones
    - Implementación de una REST API de verdad
    - Manejo de errores y agregar más validaciones en los templates y en el backend
    - Verificación de tipado (typing) para Python
    - Más pruebas unitarias
- El trabajo en Git de inteŕes yace en los primeros commit. En los últimos ya avanzaba más rápido mientras tomaba decisiones de diseño, por lo cual la historia de commit no es tan granular como debería en un entorno de trabajo regular.
- El algoritmo de búsqueda de reservas puede ser mejor. Como hay pocas habitaciones, no es mayor problema. Además, en un entorno de producción hay más variantes que considerar (concurrencia) y se pueden definir estructuras de datos para reflejar la lógica de negocio, más allá de simples modelos de Django.
- Cambié "Cuádruple" por "Familiar", me parece que sonaba mejor.
- Inicialmente programé todo en inglés, pero luego reescribí los templates en español viendo que los precios estaban en Euros.

## Requerimientos:

```
    Una reserva consiste de:
    ● fecha entrada
    ● fecha salida
    ● tipo de habitación
    ● no huéspedes
    ● datos de contacto (nombre, email, teléfono)
    ● precio total de la reserva
    ● localizador
    ● no de habitación (opcional)

    Habrá un botón para crear una reserva nueva. Este botón llevará a una pantalla que debe
    permitir introducir 2 fechas (entrada y salida), el número de huéspedes. Al buscar entre 2
    fechas le mostrará como mínimo la siguiente información:
    ● Tipo de habitación
    ● No de habitaciones disponibles para este rango de fechas
    ● Precio total de la estancia
    ● Un botón para seleccionar esa habitación

    Tras seleccionar la habitación deseada, le llevará a un formulario donde tendrá que introducir
    los datos de contacto para la reserva (nombre, email, teléfono). Al finalizar el formulario se
    creará la reserva (con un localizador alfanumérico único) y le llevará a la pantalla con el listado
    de reservas.

    Algunos detalles a tener en cuenta:
    ● Habrá 4 tipos de habitaciones: 10 individuales, 5 dobles, 4 triples, 6 cuádruples.
    ● El precio diario de cada tipo de habitación es: individual=20€/día, doble=30€/día,
    triple=40€/día, cuádruple=50€/día
    ● En una habitación individual sólo cabe 1 persona (huésped). En una doble caben 1 o 2
    personas. En una Triple caben 1, 2, o 3 personas. En una cuádruple caben 1, 2, 3 o 4
    personas.

    Por lo tanto si el usuario hace una búsqueda para 3 personas, solo deberá
    mostrar habitaciones triples y cuádruples (siempre y cuando estén disponibles para
    esas fechas) .
    ● A medida que se vayan creando reservas, debe descontarse del número de
    habitaciones disponibles de ese tipo para ese rango de fechas. Solo se podrán crear
    reservas desde la fecha actual hasta el 31/12/2020.

    Cualquier cambio o añadido sobre lo aquí explicado que suponga una mejora en la aplicación
    será bienvenida y tenida en cuenta. Queremos ver cómo eres capaz de pensar por ti mismo/a
    añadiendo mejoras sobre lo requerido. También queremos ver que tu código es limpio y
    eficiente.

    Para entregar la prueba se debe subir a una cuenta de github y facilitarnos el enlace. La prueba
    se entregará con 2 reservas ya creadas. Se usará una base de datos SQLite que estará
    incluida en el repositorio git.
    Es necesario facilitar una url a la prueba funcionando. Antes de revisar el código
    comprobaremos la funcionalidad de la prueba en esa url. Puedes utilizar cualquier servicio
    gratuito como pythonanywhere, heroku, etc.
```
