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

        for i in range(1, generated_password_length + 1):

            keys_in_dict = list(cases_copy.keys())

            roll_next_type = randint(0, len(keys_in_dict) - 1)

            key_rolled = list(cases_copy.keys())[roll_next_type]

            roll_item = randint(0, len(cases_copy[key_rolled]) - 1)
            next_value = cases_copy[key_rolled][roll_item]

            if key_rolled in ("symbols", "numbers"):
                cases_copy = cases.copy()
            elif key_rolled == "lc":
                cases_copy = cases_copy.pop("lc")
            elif key_rolled == "uc":
                cases_copy = cases_copy.pop("uc")

            generated_password.append(next_value)

        self.password = "".join(generated_password)

