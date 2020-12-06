class person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello, my name is", self.name)
        print("I am", self.age, "years old")

pl = person("Poorni", "12")
pl.myfunc()