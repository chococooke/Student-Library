
# My first python project
class CentralLibrary:
    def __init__(self, bookList):
        self.bookList = bookList;
        
    def listAllBooks(self):
        for index, book in enumerate(booklist):
            print(f"{index + 1}. {book}")
    
    def issueBook(self, bookName):
        if bookName in self.bookList:
            print(f"The book {bookName} has been successfully issued to you.\nKeep it safe consider if returning within 30 days.\nThank you!\n")
            self.bookList.remove(bookName)
        else:
            print("The book is not currently available.\n")
            
    def returnBook(self, bookName):
        self.bookList.append(bookName)
        print(f"The book has been returned to the Library successfully. Thank you for choosing central Library.\n")
        
            

class Student:
    def issueBook():
        bookName = input("Enter the book you want to issue : ")
        centralLibrary.issueBook(bookName=bookName)
        
    def returnBook():
        bookName = input("Enter the name of the book : ")
        centralLibrary.returnBook(bookName=bookName)
        
        

if __name__ == "__main__":
    booklist = ["Harry Potter", "LOTR", "Linux Fundamentals", "Desi Boyz"]
    centralLibrary = CentralLibrary(bookList=booklist)
    
    welcomeMessage = '''
    [=== Welcome to Central Library ===]
    Options:
    \t1. List available books
    \t2. Issue A book
    \t3. Return A book
    \t-----------------
    \tPress 'q' to quit.
    [==================================]
    '''
    while(True):
        print(welcomeMessage)
        a = input("Enter you choice : ")
        
        if(a == '1'):
            centralLibrary.listAllBooks()
        elif(a == '2'):
            Student.issueBook()
        elif(a == '3'):
            Student.returnBook()
        elif(a == 'q'):
            print("Thank you for using Central Library. Visit again!")
            exit()
        else:
            print("[x] Invalid Input!")
            
    