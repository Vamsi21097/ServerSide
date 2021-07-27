import os,csv,sys;
from flask import Flask
from register import *

app=Flask(__name__)


url = "postgresql://gzpzugqvthxgkl:ea358a4d34b4c30c51f6441bdfce62aa4d5f314443895dd899881e6083742072@ec2-52-21-252-142.compute-1.amazonaws.com:5432/d4q27kdo396jvi"

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