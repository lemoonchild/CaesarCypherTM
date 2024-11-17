import streamlit as st
from src.Controller.encrypt_controller import TuringController
from src.Controller.decrypt_controller import TuringDecryptController
import pandas as pd

def visualize_turing_machine(logs, tape):
    st.subheader("🔍 Proceso Detallado de la Simulación")

    # Mostrar la cinta con la posición del cabezal
    st.markdown("### Visualización de la Cinta")
    highlighted_tape = "".join(
        [f"**[{char}]**" if i == logs[-1]["head_position"] else char for i, char in enumerate(tape)]
    )
    st.write(f"`{highlighted_tape}`")

    # Crear un DataFrame para mostrar los pasos en forma de tabla
    steps_data = []
    for log in logs:
        step = {
            "Estado Actual": log["current_state"],
            "Posición del Cabezal": log["head_position"],
            "Carácter Actual": log["current_char"],
            "Transición Aplicada": log["transition"]
        }
        steps_data.append(step)

    # Mostrar la tabla con los pasos
    df_steps = pd.DataFrame(steps_data)
    st.dataframe(df_steps)

def main():
    st.set_page_config(page_title="Simulador de Máquina de Turing - Cifrado César", page_icon="🔐")

    st.title("🔐 Simulador de Máquina de Turing para Cifrado César")
    st.markdown("""
    Este simulador utiliza una máquina de Turing para **cifrar** y **descifrar** mensajes usando el Cifrado César.
    Ingresa la llave de desplazamiento y el mensaje para comenzar.
    """)

    mode = st.radio("Seleccione el modo:", ('Encriptar', 'Desencriptar'))
    key = st.number_input("Ingrese la llave de desplazamiento:", min_value=1, max_value=25, value=3, step=1)
    message = st.text_area("Ingrese el mensaje:", height=150)

    result = ""
    logs = []

    if st.button("Procesar"):
        if message.strip() == "":
            st.error("Por favor, ingrese un mensaje.")
        else:
            if mode == 'Encriptar':
                controller = TuringController('TuringMachines/Encrypt/encrypt.json')
                input_string = f"{key}#{message}"
                result, logs = controller.encrypt_message(input_string)
                st.success("Mensaje encriptado:")
                st.code(result, language="")
            else:
                controller = TuringDecryptController('TuringMachines/Decrypt/decrypt.json')
                input_string = f"{key}#{message}"
                result, logs = controller.decrypt_message(input_string)
                st.success("Mensaje desencriptado:")
                st.code(result, language="")

            # Mostrar la visualización gráfica del proceso
            tape = list(f"{key}#{message}")
            visualize_turing_machine(logs, tape)

if __name__ == "__main__":
    main()
