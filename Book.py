class Book:
    def __init__(self, book_id:str, title:str , author:str ,is_borrowed:bool) -> None:
        self.book_id=book_id
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed
    
    def borrow(self):
        if self.is_borrowed is True:
            self.is_borrowed= False
    def return_book(self):
        if self.is_borrowed is False:
            self.is_borrowed=True

class Member(Book):
    def __init__(self, book_id: str, 
                    title: str,
                    author: str, 
                    is_borrowed: bool ,
                    member_id:str , 
                    name:str ,
                    borrowed_books:list[Book]) -> None:
        super().__init__(book_id, title, author, is_borrowed)

        self.member_id=member_id
        self.name=name
        self.borrowed_books=borrowed_books


    def borrow_book(book):
        if book.is_borrowed == True:
            book.is_borrowed==False
    def return_book(book):
        if book.is_borrowed == False:
            book.is_borrowed==True

class Library:
    def __init__(self,books:dict[str,Book], members:dict[str,Member]) -> None:
        self.books=books
        self.members=members
    
    def add_book(book_book_id: str, title: str, author: str):
        pass
    def  register_member(member_id:str, name: str):
        pass
    def borrow_book(member_id: str, book_id: str):
        pass
    def return_book(member_id: str, book_id: str):
        pass
    def  get_borrowed_books(member_id):
        list[Book] 
        pass
