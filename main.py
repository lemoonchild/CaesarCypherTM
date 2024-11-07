from src.Controller.encrypt_controller import TuringController


def main():
    controller = TuringController('TuringMachines/Encrypt/encrypt.json')
    input_string = input(
        "Ingrese la llave seguida del mensaje a cifrar (ejemplo: 3#ROMA NO FUE CONSTRUIDA EN UN DIA): ")
    encrypted_message = controller.encrypt_message(input_string)
    print("Mensaje encriptado:", encrypted_message)


if __name__ == "__main__":
    main()
