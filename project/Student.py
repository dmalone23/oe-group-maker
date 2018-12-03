class Student:
    def __init__(self, p, fn, ln):
        self.partner = ""
        self.preferences = []
        for x in p:
            self.preferences.append(x)

        self.first_name = fn
        self.last_name = ln

    def remove_preference_string(self, s):
        self.preferences.remove(s)

    def remove_preference_id(self, id):
        del self.preferences[id]
