class Publication():
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page):
        super().__init__(name)
        self.author = author
        self.page = page

    def print_info(self):
        print(f"{self.name} is written by {self.author}, and has {self.page} pages.")

class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor
    def print_info(self):
        print(f"Magazine name: {self.name}\nEditor: {self.editor}")

book1 = Book("Compartment No.6", "Rosa Liksom", 192)
magazine1 = Magazine("Donald Duck", "Aki Hyyppä")
book1.print_info()
magazine1.print_info()
