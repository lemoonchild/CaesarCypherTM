# Simulador de Máquina de Turing para Cifrado César

Este proyecto implementa una Máquina de Turing en Python para simular el proceso de cifrado y descifrado de mensajes utilizando el Cifrado César. La interfaz de usuario está construida con Streamlit, proporcionando una experiencia visual amigable para los usuarios.

## Características

- Cifrado y descifrado de mensajes usando el Cifrado César.
- Visualización paso a paso del proceso de la Máquina de Turing.
- Interfaz de usuario intuitiva con Streamlit.
- Configuración flexible a través de archivos JSON.

## Estructura del Proyecto

El proyecto tiene la siguiente estructura:

```
CaesarCypherTM/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── src/
│   ├── Controller/
│   │   ├── decrypt_controller.py
│   │   └── encrypt_controller.py
│   └── Model/
│       ├── decrypt_model.py
│       └── encrypt_model.py
├── TuringMachines/
│   ├── Encrypt/
│   │   └── encrypt.json
│   └── Decrypt/
│       └── decrypt.json
```

## Instalación

Sigue estos pasos para instalar y ejecutar el proyecto localmente:

1. Clona el repositorio:
  ```sh
  git clone https://github.com/lemoonchild/CaesarCypherTM
  ```

2. Navega al directorio del proyecto:
  ```sh
  cd CaesarCypherTM
  ```

3. Crea un entorno virtual (recomendado):
  ```sh
  python -m venv venv
  source venv/bin/activate  # En MacOS/Linux
  venv\Scripts\activate     # En Windows
  ```

4. Instala las dependencias:
  ```sh
  pip install -r requirements.txt
  ```

## Ejecutar la Aplicación

Ejecuta la aplicación de Streamlit usando el siguiente comando:

```sh
streamlit run app.py
```

La aplicación se abrirá en tu navegador en la URL [http://localhost:8501](http://localhost:8501).

## Uso

1. Selecciona el modo: Encriptar o Desencriptar.
2. Ingresa la llave de desplazamiento (un número entre 1 y 25).
3. Escribe el mensaje que deseas cifrar o descifrar.
4. Haz clic en el botón Procesar para ver el resultado.
5. Explora el proceso paso a paso en la sección Ver pasos de la simulación.

## Ejemplo de Uso

### Ejemplo de Encriptación

**Entrada:**

- Llave: 3
- Mensaje: ROMA NO FUE CONSTRUIDA EN UN DIA

**Salida:**

- Mensaje Encriptado: URPD QR IXH FRQVWUXLGD HQ XQ GLD

### Ejemplo de Desencriptación

**Entrada:**

- Llave: 3
- Mensaje: URPD QR IXH FRQVWUXLGD HQ XQ GLD

**Salida:**

- Mensaje Desencriptado: ROMA NO FUE CONSTRUIDA EN UN DIA

## Archivos de Configuración

Los archivos de configuración JSON definen los estados y transiciones de la Máquina de Turing:

- `encrypt.json`: Configuración para el proceso de encriptación.
- `decrypt.json`: Configuración para el proceso de desencriptación.

### Ejemplo de Configuración (encrypt.json)

```json
{
  "Q": ["q0", "q_read_key", "q_encrypt", "q_accept"],
  "Sigma": ["#", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
  "Gamma": ["#", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_"],
  "q0": "q0",
  "F": ["q_accept"],
  "delta": [
   { "current_state": "q0", "read_symbol": "[0-9]", "next_state": "q_read_key", "write_symbol": "[0-9]", "movement": "R" },
   { "current_state": "q_read_key", "read_symbol": "#", "next_state": "q_encrypt", "write_symbol": "#", "movement": "R" },
   { "current_state": "q_encrypt", "read_symbol": "[A-Za-z]", "next_state": "q_encrypt", "write_symbol": "shift([A-Za-z], key)", "movement": "R" },
   { "current_state": "q_encrypt", "read_symbol": "_", "next_state": "q_accept", "write_symbol": "_", "movement": "S" }
  ]
}
```

## Requisitos del Proyecto

Consulta el archivo `requirements.txt` para ver todas las dependencias necesarias.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue estos pasos para contribuir:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Contacto

- **Autores:** Diego Valenzuela - Gerson Ramirez - Xavier Lopez - Nahomy Castro
