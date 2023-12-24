
class library:
    def __init__(self):
        self.total_book = 0
        self.booklist = []

    def add(self, name):
        self.booklist.append(name)
        self.total_book = len(self.booklist)

    def show(self):
        print(f"The number of books in the library is {self.total_book} and the books are:") 
        for i in self.booklist:
            print(i)
        

a = library()
a.add("Wings of fire")
a.add("Harry Potter and the half blood price")
a.add("Looking for alaska")
a.add("Thousand splendid sun")
a.show()