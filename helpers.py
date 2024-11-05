import random
import string


class DataGenerate():
    name_list = [
        'John', 'Tom', 'Anna', 'Mia', 'Diana', 'Otto', 'Amanda', 'Ivan', 'Alexander', 'Elena', 'Lina', 'Lui', 'Michael']

    def generate_random_name(self):
        random_name = random.choice(self.name_list)
        return random_name

    def generate_random_email(self, length=3):
        characters = string.digits
        digits = ''.join(random.choice(characters) for _ in range(length))
        return f"alina_kuptsova_15_{digits}@ya.ru"

    def generate_random_password(self, length=6):
        characters = string.ascii_letters + string.digits
        random_password = ''.join(random.choice(characters) for _ in range(length))
        return random_password


data_generate = DataGenerate()

