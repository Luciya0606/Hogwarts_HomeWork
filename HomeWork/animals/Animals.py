

class Animals:
    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def howl(self):
        print(f"{self.age}岁{self.color}{self.sex}{self.name}会叫")



    def running(self):
        print(f"{self.age}岁{self.color}{self.sex}{self.name}会跑")

if __name__ == '__main__':
    animals=Animals("狗狗", "黑色", 2, "母")
    animals.howl()
    animals.running()