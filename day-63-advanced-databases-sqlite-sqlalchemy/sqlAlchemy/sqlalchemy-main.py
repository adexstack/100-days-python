from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # getting current directory

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

# Creating the db table
# db.create_all()

# CREATE RECORD

# new_book_1 = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
# new_book_2 = Book(id=2, title="Dan Potter", author="J. K. Row", rating=7.3)
# new_book_3 = Book(id=3, title="Steve Potter", author="J. K. Steve", rating=5.3)
# new_book_4 = Book(id=4, title="Feyi Potter", author="J. K. Steve", rating=5.3)
## NOTE: When creating new records, the primary key fields is optional. you can also write:
# new_book_5 = Book(title="Dan Kan", author="Fret. Steve", rating=4.3)

# all_record = [new_book_4, new_book_5]
#
# for record in all_record:
#     try:
#         db.session.add(record)
#     except:
#         print("record was not written to db")

# db.session.add(new_book_1)
# db.session.add(new_book_2)
# db.session.add(new_book_3)
#db.session.add(new_book_4)

# committing session into db
# db.session.commit()

#Read All Records
# all_books = db.session.query(Book).all()
# print(all_books)

#Read A Particular Record By Query
# book = Book.query.filter_by(title="Harry Potter").first()
# print(book)

# Update A Particular Record By Query
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
#db.session.commit()


# Update A Record By PRIMARY KEY
book_id = 1
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Potter and the Goblet of Fire"
db.session.commit()


# Delete A Particular Record By PRIMARY KEY
book_id = 2
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()
#You can also delete by querying for a particular value e.g. by title or one of the other properties.
