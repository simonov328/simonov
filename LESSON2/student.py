class Student:

    def __init__(self, name: str, age: float, group:str):
         self.Name = name
         self.Age = float
         self.Group = group

    def __str__(self):
        return (f'Name - {self.Name}\n'
                f'Age - {self.Age}\n'
                f'Group - {self.Group}')
