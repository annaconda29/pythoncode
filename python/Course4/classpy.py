class Fish:
    x = "Tiger"
    y = "Lion"
    def fish(self):
        self.x = self.x + "fish"
        self.y = self.y + "fish"
        print("Fishes are:", self.x, ",", self.y)
a = Fish()
a.fish()
print(a)
print("Type:", type(a))
print("Dir:", dir(a))