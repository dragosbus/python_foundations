class Parent():
    def __init__(self,last_name,eye_color):
        self.last_name = last_name
        self.eye_color = eye_color
        
class Child(Parent):
    def __init__(self, last_name, eye_color, toys):
        Parent.__init__(self, last_name, eye_color)
        self.toys = toys
        
d = Parent("busuioc","blue")
print(d.last_name)
    