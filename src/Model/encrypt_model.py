import json


def load_machine_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def get_shifted_char(char, key, alphabet):
    if char.isupper():
        # Letras mayúsculas
        uppercase_letters = [c for c in alphabet if c.isupper()]
        index = uppercase_letters.index(char)
        shifted_index = (index + key) % len(uppercase_letters)
        return uppercase_letters[shifted_index]
    elif char.islower():
        # Letras minúsculas
        lowercase_letters = [c for c in alphabet if c.islower()]
        index = lowercase_letters.index(char)
        shifted_index = (index + key) % len(lowercase_letters)
        return lowercase_letters[shifted_index]
    else:
        # Caracteres no alfabéticos se dejan igual
        return char


def simulate_turing_machine(input_string, config):
    tape = list(input_string)
    current_state = config['q0']
    head_position = 0
    key_chars = []
    alphabet = config['Gamma']

    key = None  # Inicializamos la clave como None

    while current_state != 'q_accept' and head_position < len(tape):
        current_char = tape[head_position]
        transition_applied = False

        # Debug: Mostrar el estado actual, posición del cabezal y carácter actual
        print(f"Estado actual: {current_state}, Posición: {head_position}, Carácter: '{current_char}'")

        for transition in config['delta']:
            if transition['current_state'] == current_state:
                read_symbol = transition['read_symbol']
                write_symbol = transition['write_symbol']
                movement = transition['movement']
                next_state = transition['next_state']

                # Verificar si el símbolo leído coincide con el patrón
                symbol_matches = False
                if read_symbol == current_char:
                    symbol_matches = True
                elif read_symbol == '[A-Za-z]' and current_char.isalpha():
                    symbol_matches = True
                elif read_symbol == '[0-9]' and current_char.isdigit():
                    symbol_matches = True
                elif read_symbol == ' ' and current_char == ' ':
                    symbol_matches = True
                elif read_symbol == '#' and current_char == '#':
                    symbol_matches = True
                elif read_symbol == '_' and current_char == '_':
                    symbol_matches = True

                if symbol_matches:
                    # Debug: Mostrar la transición aplicada
                    print(f"Aplicando transición: {transition}")

                    # Aplicar el símbolo de escritura
                    if write_symbol == "shift([A-Za-z], key)":
                        if key is None:
                            # Convertir la clave a entero
                            key = int(''.join(key_chars))
                        shifted_char = get_shifted_char(current_char, key, alphabet)
                        tape[head_position] = shifted_char
                    elif write_symbol in ['[0-9]', '[A-Za-z]']:
                        tape[head_position] = current_char  # Mantener el mismo carácter
                    else:
                        tape[head_position] = write_symbol

                    # Mover el cabezal
                    if movement == 'R':
                        head_position += 1
                    elif movement == 'L':
                        head_position -= 1
                    # Si es 'S', no hacemos nada

                    # Actualizar el estado
                    current_state = next_state
                    transition_applied = True

                    # Si estamos leyendo la clave, agregar los dígitos
                    if current_state == 'q_read_key' and current_char.isdigit():
                        key_chars.append(current_char)

                    break  # Salir del bucle de transiciones

        if not transition_applied:
            # Debug: Mostrar mensaje si no se aplicó una transición
            print(f"No se encontró una transición válida para el estado '{current_state}' y símbolo '{current_char}'. La máquina se detiene.")
            break

    # Después de la simulación, unir la cinta completa
    full_tape = ''.join(tape)

    # Encontrar la posición del separador '#'
    separator_index = full_tape.find('#')

    if separator_index != -1:
        # Extraer el mensaje encriptado después del '#'
        encrypted_message = full_tape[separator_index + 1:]
    else:
        # Si no se encuentra el separador, retornar toda la cinta (o manejar el error)
        encrypted_message = full_tape

    return encrypted_message

