
import random
import os


# the class for generation of name, password, user agent
class Generation:
    def __init__(self):
        with open(os.path.join('utils', 'Names.txt'), 'r') as filestream:
            self.list_of_names = filestream.read().split()

    def generate_fullname(self):
        fullname = []
        while True:
            rnd = random.randint(0, len(self.list_of_names) - 1)
            if rnd % 2 == 0:
                fullname.append(self.list_of_names[rnd])
                break
        while True:
            rnd = random.randint(0, len(self.list_of_names) - 1)
            if rnd % 2 != 0:
                fullname.append(self.list_of_names[rnd])
                break
        return fullname

    def generate_password(self):
        rnd = random.randint(0, len(self.list_of_names) - 1)
        return str(random.randint(200, 2000))+self.list_of_names[rnd]+'+'+str(random.randint(1, 200))

    @staticmethod
    def set_random_user_agent():
        with open(os.path.join('utils', 'user_agent.txt'), 'r') as filestream:
            list_of_ua = filestream.read().splitlines()
        return random.choice(list_of_ua)