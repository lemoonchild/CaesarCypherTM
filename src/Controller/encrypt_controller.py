from src.Model.encrypt_model import load_machine_config, simulate_turing_machine


class TuringController:
    def __init__(self, config_path):
        self.config = load_machine_config(config_path)

    def encrypt_message(self, input_string):
        encrypted_message = simulate_turing_machine(input_string, self.config)
        return encrypted_message
