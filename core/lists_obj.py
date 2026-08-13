class PasswordsList:
    def __init__(self, p: dict):
        self.passwords_list = p

def createListObject(passwords: dict):
    global UserPasswordsList
    UserPasswordsList = PasswordsList(p=passwords)

