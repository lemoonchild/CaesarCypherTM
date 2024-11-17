from src.Controller.encrypt_controller import TuringController
from src.Controller.decrypt_controller import TuringDecryptController


def main():
    mode = input("Seleccione el modo ('encrypt' para encriptar, 'decrypt' para decriptar): ").strip().lower()

    if mode == 'encrypt':
        controller = TuringController('TuringMachines/Encrypt/encrypt.json')
        input_string = input(
            "Ingrese la llave seguida del mensaje a cifrar (ejemplo: 3#ROMA NO FUE CONSTRUIDA EN UN DIA): ")
        encrypted_message = controller.encrypt_message(input_string)
        print("Mensaje encriptado:", encrypted_message)
    elif mode == 'decrypt':
        controller = TuringDecryptController('TuringMachines/Decrypt/decrypt.json')
        input_string = input(
            "Ingrese la llave seguida del mensaje a descifrar (ejemplo: 3#URPD QR IXH FRQVWUXLGD HQ XQ GLD): ")
        decrypted_message = controller.decrypt_message(input_string)
        print("Mensaje descifrado:", decrypted_message)
    else:
        print("Modo inválido. Por favor, elija 'encrypt' o 'decrypt'.")


if __name__ == "__main__":
    main()
