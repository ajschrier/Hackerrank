# Book is a placeholder class
# Real class was provided in the exercise


class Book:
    def __init__(self, title, author):
        pass


class MyBook(Book, object):
    def __init__(self, title, author, price):
        super(MyBook, self).__init__(title, author)
        self.price = price

    def display(self):
        print "Title: {}".format(self.title)
        print "Author: {}".format(self.author)
        print "Price: {}".format(self.price)
