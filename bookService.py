from repository import Repository


class BookService():
    def get_bookList(self):
        return Repository.book

    def listar(self):
        print("\n     Listando")
        for key in self.Repository.book:
            print("-> %s" % (self.repository.book[key]))

    def add_book(self, book):
        print("\n     Agregando")
        lastKey = -1
        for i in Repository.booksList:
            lastKey = i
        bookkey = lastKey + 1
        Repository.booksList[bookkey] = book.__dict__
        return bookkey

    def update_book(self, key, book):
        Repository.book[key]['_name'] = book.name
        Repository.book[key]['_surname'] = book.surname
        Repository.book[key]['_age'] = book.age

    def delete_book(self, key):
        del Repository.book[key]

    def assign_book(self, book_id, member_legajo):
        pass
