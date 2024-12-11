# Build your Free Al Agent

Este proyecto es una aplicación web interactiva creada con Streamlit y modelos de lenguaje integrados a través de llama_index. Su finalidad es ofrecer una interfaz de chat para interactuar con diferentes modelos LLM.

## Estructura del proyecto

La estructura principal del proyecto es la siguiente:

```
build-your-free-Alagent/
├─ app/
│  ├─ app.py
│  ├─ config.yaml
├─ .env
├─ .gitignore
├─ Dockerfile
├─ install.bat
├─ LICENSE
├─ README.md
├─ requirements.txt
├─ run.bat
└─ start-demo.sh
```

- **app/app.py**: Archivo principal de la aplicación Streamlit. Aquí se define la lógica de interacción con los modelos LLM y la interfaz de usuario.
- **app/config.yaml**: Archivo de configuración adicional (si es requerido) donde pueden definirse parámetros específicos para la aplicación.
- **.env**: Archivo de entorno (opcional) para almacenar variables de entorno sensibles, como tokens de acceso o credenciales (no está incluido en el repositorio por razones de seguridad).
- **requirements.txt**: Archivo que contiene la lista de dependencias necesarias para el proyecto.
- **install.bat**: Script para instalar las dependencias del proyecto en entornos Windows.
- **run.bat**: Script para ejecutar la aplicación en entornos Windows utilizando Streamlit.
- **start-demo.sh**: Script de ejemplo para entornos Unix o Docker (opcional, si se quiere ejecutar en Linux/MacOS o dentro de un contenedor Docker).
- **Dockerfile**: Archivo que permite la construcción de una imagen Docker para la aplicación.

## Dependencias y Requerimientos

Antes de ejecutar la aplicación, es necesario contar con:

- **Python 3.9 o superior** (recomendado)
- **pip** (gestor de paquetes de Python)
- **Streamlit** y las librerías listadas en `requirements.txt`
- **llama_index** y su compatibilidad con el modelo Ollama o los modelos seleccionados (por ejemplo: llama3.2:1b, phi3, mistral). Esto puede requerir tener instalados los modelos a nivel local o acceso a ellos.
- Conexión a internet si los modelos dependen de un endpoint remoto (esto dependerá de la configuración).

Asegúrate de que `pip` esté en el PATH y que puedas ejecutar `streamlit` desde la línea de comandos.

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/build-your-free-Alagent.git
cd build-your-free-Alagent
```

Instala las dependencias (Windows):

Ejecuta el script `install.bat`:

```bash
install.bat
```

Esto ejecutará `pip install -r requirements.txt`.

En otros sistemas operativos (Linux/MacOS), puedes hacerlo manualmente:

```bash
pip install -r requirements.txt
```

## Ejecución de la Aplicación

### En Windows:
Usa el script `run.bat`:

```bash
run.bat
```

Este script ejecutará:

```bash
streamlit run app/app.py
```

Una vez ejecutado, se abrirá automáticamente el navegador por defecto con la interfaz de la aplicación, generalmente en [http://localhost:8501](http://localhost:8501).

### En Linux/MacOS:

Ejecuta el comando de forma manual:

```bash
streamlit run app/app.py
```

O utiliza `start-demo.sh` si está configurado correctamente (no olvides darle permisos de ejecución con `chmod +x start-demo.sh`).

## Uso de la Aplicación

1. La aplicación mostrará en la interfaz un cuadro de chat.
2. En el panel lateral (*sidebar*) podrás seleccionar el modelo a utilizar, por ejemplo: llama3.2:1b, phi3, o mistral.
3. Ingresa tu pregunta o mensaje en el campo designado y presiona *Enter*.
4. La aplicación generará una respuesta basada en el modelo seleccionado. El tiempo de respuesta se mostrará junto al mensaje.

## Customización

- Puedes cambiar la lógica de la aplicación editando `app/app.py`.
- Ajusta el archivo `config.yaml` (si es requerido por tu entorno) para personalizar la configuración.
- Si usas Docker, modifica el `Dockerfile` para personalizar el contenedor.

## Notas adicionales

- Asegúrate de que las variables de entorno sensibles (API keys, credenciales, etc.) estén definidas en `.env` o configuradas de forma segura en tu entorno.
- Revisa `requirements.txt` para ver todas las librerías utilizadas. Puedes agregar, eliminar o actualizar las librerías según tus necesidades.

## Licencia

Este proyecto está bajo la licencia MIT.