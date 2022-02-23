class Student:
    def __init__(self, fname, lname, id):
        self.fname = fname
        self.lname = lname
        self.id = id

    def __str__(self):
        return f"{self.lname}, {self.fname}\tID: {self.id}"

    def __len__(self):
        return len(self.fname) + len(self.lname)
