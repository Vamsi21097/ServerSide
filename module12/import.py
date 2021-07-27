import os,csv,sys;
from flask import Flask
from register import *

app=Flask(__name__)


url = "postgresql://jdqkilhlauiwgk:d97be59aa9bc5dc534fd3820935adf8c7cc6d06f20758ffb6cf72cc73dd52dbc@ec2-34-206-8-52.compute-1.amazonaws.com:5432/d1dt17jclf7qfq"

app.config["SQLALCHEMY_DATABASE_URI"] = url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    with app.app_context():
        db.create_all()
        f=open("books.csv")
        reader=csv.reader(f)
        for isbn, title, author, year in reader:
            print(isbn,title,author,year)
            book=Books(isbn=isbn, title=title, author=author, year=year)
            db.session.add(book)
            db.session.commit()
        print("Success", file=sys.stdout)

if __name__ == "__main__":
    main()