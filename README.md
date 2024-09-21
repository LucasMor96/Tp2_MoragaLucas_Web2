# Tablero de Mensajes

Una aplicación web desarrollada como parte de un trabajo práctico II para la materia "Programación Web 2". Esta aplicación, creada con Django 4.2 y Python 3.10, simula un sistema de mensajería interno donde los usuarios pueden enviar, recibir, buscar, y organizar mensajes, brindando una experiencia intuitiva y fácil de usar.

## Tecnologías Utilizadas

La aplicación está construida sobre las siguientes tecnologías:

- **Django** para la gestión del backend y la lógica de negocio.
- **Python 3.10** como lenguaje de programación principal.
- **SQLite** como base de datos para almacenar los mensajes.
- **HTML**, **CSS**, y **Bootstrap** para el diseño del frontend, proporcionando una interfaz amigable y adaptable.

## Funcionalidades Principales

- **Enviar Mensajes**: Facilita la comunicación entre usuarios mediante el envío de mensajes.
- **Listar Mensajes**: Muestra una vista completa de todos los mensajes, incluyendo enviados, recibidos, eliminados (en papelera) y favoritos.
- **Filtrar Mensajes**: Organiza los mensajes según su tipo: enviados, recibidos, eliminados, o favoritos.
- **Buscar Mensajes**: Permite buscar mensajes específicos por remitente o destinatario.
- **Marcar como Favorito**: Da la opción de destacar mensajes importantes marcándolos como favoritos.
- **Eliminar Mensajes**: Permite mover mensajes a la papelera o eliminarlos permanentemente.

## Cómo Empezar

Para poner en funcionamiento la aplicación, sigue estos pasos:

1. Clonar este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/LucasMor96/Tp1_web2_2024.git
    ```

2. Instalar las dependencias necesarias:

    ```bash
    pip install -r requirements.txt
    ```

3. Realiza las migraciones de la base de datos:

    ```bash
    python manage.py migrate
    ```

4. Ejecuta el servidor de desarrollo de Django:

    ```bash
    python manage.py runserver
    ```

## Cómo Usar la Aplicación

1. Abre tu navegador y dirígete a [http://localhost:8000/](http://localhost:8000/).
2. Explora las diferentes pestañas para enviar mensajes, buscar, filtrar, y gestionar tus mensajes.
3. Utiliza la barra de búsqueda para encontrar mensajes específicos de manera rápida.
