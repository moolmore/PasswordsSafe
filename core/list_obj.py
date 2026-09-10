class PasswordsList:
    def __init__(self, p: list):
        self.passwords_list = p

def createListObject(passwords: list):
    global UserPasswordsList
    UserPasswordsList = PasswordsList(p=passwords)

