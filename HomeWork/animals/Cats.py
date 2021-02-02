from Animals import Animals


class Cats(Animals):
    def __init__(self, name, color, age, sex):
        self.pelage="短毛"
        super().__init__(name, color, age, sex)


    def catching(self):
        print(f"{self.age}岁{self.color}{self.pelage}{self.sex}{self.name}会抓老鼠")


    def howl(self):
        print(f"{self.age}岁{self.color}{self.pelage}{self.sex}{self.name}会喵喵叫")

    def main(self):
        if self.age<3:
            self.howl()
            print("--调用父类方法--")
            self.running()
        else:
            self.catching()

if __name__ == '__main__':
    age = int(input("请输入年龄"))
    cats=Cats("猫咪", "白色", age, "公")
    cats.main()



