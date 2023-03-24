import string
from random import randint


class Password:
    length: int
    password: str

    def __init__(self, length=12):
        self.length = length

    def create_random_password(self) -> None:

        generated_password = list()
        generated_password_length = self.length

        cases = {
            "symbols": ['!', '$', '%', '&', '*', '+', '-', '?', '@', '_'],
            "lower_case": list(string.ascii_letters[:26]),
            "upper_case": list(string.ascii_letters[26:]),
            "numbers": list(string.digits),
        }

        cases_copy = cases.copy()

        next_value = None

        for i in range(0, generated_password_length):

            list_of_dict_keys = list(cases_copy.keys())

            roll_for_key = randint(0, len(list_of_dict_keys) - 1)

            key_rolled = list_of_dict_keys[roll_for_key]

            rolled_key_values = cases_copy[key_rolled]
            roll_for_value_index = randint(0, len(rolled_key_values) - 1)

            selected_value = cases_copy[key_rolled][roll_for_value_index]

            if key_rolled in ("symbols", "numbers"):
                cases_copy = cases.copy()
            elif key_rolled == "lower_case":
                cases_copy["lower_case"].pop(roll_for_value_index)
            elif key_rolled == "upper_case":
                cases_copy["upper_case"].pop(roll_for_value_index)

            generated_password.append(selected_value)

        self.password = "".join(generated_password)

