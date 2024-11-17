import json

def load_machine_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_shifted_char(char, key, alphabet):
    if char.isupper():
        uppercase_letters = [c for c in alphabet if c.isupper()]
        index = uppercase_letters.index(char)
        shifted_index = (index - key) % len(uppercase_letters)
        return uppercase_letters[shifted_index]
    elif char.islower():
        lowercase_letters = [c for c in alphabet if c.islower()]
        index = lowercase_letters.index(char)
        shifted_index = (index - key) % len(lowercase_letters)
        return lowercase_letters[shifted_index]
    else:
        return char

def format_transition(transition):
    current_state = transition['current_state']
    read_symbol = transition['read_symbol']
    next_state = transition['next_state']
    write_symbol = transition['write_symbol']
    movement = transition['movement']
    return f"Estado: {current_state} → {next_state} | Leer: {read_symbol} | Escribir: {write_symbol} | Movimiento: {movement}"

def simulate_turing_machine(input_string, config):
    tape = list(input_string)
    current_state = config['q0']
    head_position = 0
    key_chars = []
    alphabet = config['Gamma']

    key = None
    logs = []

    while current_state != 'q_accept' and head_position < len(tape):
        current_char = tape[head_position]
        transition_applied = False
        log_entry = {
            "current_state": current_state,
            "head_position": head_position,
            "current_char": current_char,
            "transition": ""
        }

        for transition in config['delta']:
            if transition['current_state'] == current_state:
                read_symbol = transition['read_symbol']
                write_symbol = transition['write_symbol']
                movement = transition['movement']
                next_state = transition['next_state']

                symbol_matches = (
                    read_symbol == current_char or
                    (read_symbol == '[A-Za-z]' and current_char.isalpha()) or
                    (read_symbol == '[0-9]' and current_char.isdigit()) or
                    (read_symbol == ' ' and current_char == ' ') or
                    (read_symbol == '#' and current_char == '#') or
                    (read_symbol == '_' and current_char == '_')
                )

                if symbol_matches:
                    log_entry["transition"] = format_transition(transition)

                    if write_symbol == "shift([A-Za-z], key)":
                        if key is None:
                            key = int(''.join(key_chars))
                        shifted_char = get_shifted_char(current_char, key, alphabet)
                        tape[head_position] = shifted_char
                    elif write_symbol in ['[0-9]', '[A-Za-z]']:
                        tape[head_position] = current_char
                    else:
                        tape[head_position] = write_symbol

                    if movement == 'R':
                        head_position += 1
                    elif movement == 'L':
                        head_position -= 1

                    current_state = next_state
                    transition_applied = True

                    if current_state == 'q_read_key' and current_char.isdigit():
                        key_chars.append(current_char)

                    break

        logs.append(log_entry)

        if not transition_applied:
            log_entry["transition"] = "No se encontró una transición válida"
            logs.append(log_entry)
            break

    full_tape = ''.join(tape)
    separator_index = full_tape.find('#')
    decrypted_message = full_tape[separator_index + 1:] if separator_index != -1 else full_tape

    return decrypted_message, logs
