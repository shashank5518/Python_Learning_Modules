from dataclasses import dataclass
import os
import logging

os.chdir("D:/Python/projects/")
logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


@dataclass
class Book:
    title: str
    author: str
    isbn: str
    copies_total: int
    copies_avail: int

    @property
    def is_available(self):
        return self.copies_avail > 0

    @property
    def borrowed_count(self):
        return self.copies_total - self.copies_avail

    def __post_init__(self):
        if (
            self.copies_avail < 0
            or self.copies_total < 0
            or self.copies_total < self.copies_avail
        ):
            raise ValueError


@dataclass
class Member:
    member_id: int
    name: str
    email: str
    borrowed_books: list = None

    def __post_init__(self):
        if "@" not in self.email or "." not in self.email:
            raise ValueError
        if self.borrowed_books is None:
            self.borrowed_books = []

    @property
    def num_of_books_borrowed(self):
        return len(self.borrowed_books)


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book: Book):
        if book.isbn not in self.books:
            self.books[book.isbn] = book
        else:
            existing_book = self.books[book.isbn]
            existing_book.copies_total += book.copies_total
            existing_book.copies_avail += book.copies_avail
        logging.info(f"Added New Book: {book.title}")

    def remove_book(self, isbn: str):
        try:
            book = self.books[isbn]
        except KeyError:
            logging.error(f"Book with {isbn} not found")
            raise KeyError
        else:
            if book.borrowed_count > 0:
                logging.error(
                    f"Could not remove {book.title} because copies are borrowed"
                )
                raise ValueError
            removed_book = self.books.pop(isbn)
            logging.info(f"Removed {removed_book.title}")

    def search_book(self, isbn: str) -> Book:
        if isbn not in self.books:
            logging.error(f"Book {isbn} does not exist")
            raise ValueError
        return self.books[isbn]

    def register_member(self, member: Member):
        if member.member_id not in self.members:
            self.members[member.member_id] = member
            logging.info(f"Added New Member: {member.name}, {member.member_id}")
        else:
            logging.error(f"Member {member.member_id} Already Exists")
            raise ValueError

    def remove_member(self, member_id: int):
        try:
            member = self.members[member_id]
        except KeyError:
            logging.error(f"Member {member_id} does not exist")
            raise KeyError
        if member.num_of_books_borrowed > 0:
            logging.error(f"Cannot remove {member_id} pending returns")
            raise ValueError
        removed_member = self.members.pop(member_id)
        logging.info(f"Removed Member {removed_member.name}")

    def search_member(self, member_id: int) -> Member:
        if member_id not in self.members:
            logging.error(f"Member {member_id} does not exist")
            raise ValueError
        return self.members[member_id]

    def borrow_book(self, member_id: int, isbn: str):
        member = self.search_member(member_id)
        book = self.search_book(isbn)

        if not book.is_available:
            logging.error(f"{book.title} is unavailable")
            raise ValueError
        if isbn in member.borrowed_books:
            logging.error(f"{isbn} already borrowed by {member_id}")
            raise ValueError
        book.copies_avail -= 1
        member.borrowed_books.append(isbn)
        logging.info(f"{book.title} borrowed by {member.name}")

    def return_book(self, member_id: int, isbn: str):
        member = self.search_member(member_id)
        book = self.search_book(isbn)

        if isbn not in member.borrowed_books:
            logging.error(f"{book.title} was never borrowed by {member.name}")
            raise ValueError
        book.copies_avail += 1
        member.borrowed_books.remove(isbn)
        logging.info(f"{book.title} was returned by {member.name}")

    def save(self):
        pass

    def load(self):
        pass


def main():
    book_1 = Book("Clean Code", "XYZ", "9182931273", 5, 3)
    member_1 = Member(101, "Shashank", "shashank@email.com")
    library = Library()

    library.add_book(book_1)
    library.register_member(member_1)
    library.search_member(member_1.member_id)

    print(library.members)
    print(library.books)


if __name__ == "__main__":
    main()
