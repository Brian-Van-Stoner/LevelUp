class Phonebook():
    pass

    def __init__(self):
        self.user_details = dict()

    def add(self, name, tel):
        self.user_details[name] = tel
    
    def search(self, name):
        for k,v in self.user_details.items():
            if name == k:
                return True