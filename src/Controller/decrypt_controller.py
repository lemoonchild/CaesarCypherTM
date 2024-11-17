from src.Model.decrypt_model import load_machine_config, simulate_turing_machine


class TuringDecryptController:
    def __init__(self, config_path):
        self.config = load_machine_config(config_path)

    def decrypt_message(self, input_string):
        decrypted_message = simulate_turing_machine(input_string, self.config)
        return decrypted_message
