class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        print(f'Title: {self.title}')

    def get_author(self):
        print(f'Author: {self.author}')

PP = Book('Orgulho e Preconceito', 'Jane Austen')
PP.get_title()
PP.get_author()
print('------------------------------')
H = Book('Hamelet', 'William Shakespeare')
H.get_title()
H.get_author()
print('------------------------------')
WP = Book('War and Peace', 'Leo Tolstoy')
WP.get_title()
WP.get_author()