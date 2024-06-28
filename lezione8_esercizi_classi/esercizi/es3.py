class Book:
   
    def __init__(self , title:str , author:str , isbn) -> None:
        self.title=title
        self.author=author
        self.isbn=isbn

    def __str__(self) -> str:
        return f"title = {self.title}, author = {self.author}, isbn = {self.isbn}"
        
    @classmethod
    def from_string(cls , book_str :str):
        title , author , isbn = book_str.split(",")
        return cls(title, author , isbn)
    

class Member:
    def __init__(self , name:str , member_id:str , borrowed_books:bool) -> None:
        self.name=name
        self.member_id=member_id
        self.borrowed_books=borrowed_books
        

a=Book("tempo","pippo",21313)
print(a)
book :str= "La Divina Commedia, D. Alighieri, 999000666"
libro : Book= Book.from_string(book)
print(libro)