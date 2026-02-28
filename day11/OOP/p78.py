class BTSMember:
    def __init__(self, name, role, age):
        self.name = name
        self.role = role
        self.age = age

    def introduce(self):
        print(f"Hi! I'm {self.name}, I'm a {self.role} and I'm {self.age} years old!")

    def perform(self):
        print(f"{self.name} is performing! 🎤")

jk = BTSMember("Jungkook", "singer", 25)
v = BTSMember("V", "vocalist", 27)

jk.introduce()   # Hi! I'm Jungkook, I'm a singer and I'm 25 years old!
v.perform()      # V is performing! 🎤