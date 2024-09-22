# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 13:36:04 2024

@author: namita
"""
class Book_Detail:
    def __init__(self, nw_bk_nam, nw_bk_aut, nw_bk_gnr, nw_bk_pblktn):
        # Initialize attributes
        self.bk_nam = nw_bk_nam
        self.bk_aut = nw_bk_aut
        self.bk_gnr = nw_bk_gnr
        self.bk_pblktn = nw_bk_pblktn

        # Dictionary to store book details
        self.bk_dic = {
            "BookName": self.bk_nam,
            "BookAuthor": self.bk_aut,
            "BookGenere": self.bk_gnr,
            "BookPublication": self.bk_pblktn  # Correcting the key name to 'BookPublication'
        }

    # Method to add book details to a list
    def add_bk_dtl(self, empty_list):
        empty_list.append(self.bk_dic)

    # Method to print the book details
    def print_bk_dtl(self, book_list):
        for book in book_list:
            print(book)
       

# Create an empty list to store book details
empty_list = []

# Create a Book_Detail object and add book details to the list
book = Book_Detail('BBB', 'Nam', 'Bio', 'pub')

# Append the book details to the list
book.add_bk_dtl(empty_list)

# Print the book details
book.print_bk_dtl(empty_list)