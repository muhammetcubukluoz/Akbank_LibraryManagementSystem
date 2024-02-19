class Library:
    def __init__(self, fName):
        self.fName=fName
    
    def fOpen(self):
        self.file=open(self.fName,"a+")
    
    # Reset the file
    def fClose(self):
        if self.file is not None:
            self.file.close()
            self.file=None

    def listBooks(self):
        try:
            file=open(self.fName,"r")
        except FileNotFoundError:
            print("file not exsist")
        else:
            with file:
                for row in file:
                    book=row.strip().split(",")
                    if len(book)>=2:
                        print("\nBook: ",book[0])
                        print("Author: ", book[1])

    def addBook(self):
        bookRow=[]
        bookRow.append(input("--Enter book title: "))
        bookRow.append(input("--Enter book author: "))
        bookRow.append(input("--Enter relase year: "))
        bookRow.append(input("--Enter number of pages: "))

        bookSave=",".join(bookRow)+"\n"

        try:
            with open(self.fName,"a")as file:
                file.write(bookSave)
            print(f"\nThe book('{bookRow[0]}') has been successfully added")
        except FileNotFoundError:
            print("\nThe file does not exsist.")
    
    def removeBook(self):
        title=input("--Enter the title of the book remove: ")
        found:False

        try:
            with open(self.fName,"r")as file:
                line=file.readlines()

            with open(self.fName,"w")as file:
                for row in line:
                    if not row.startswith(title+","):
                        file.write(row)
                    else:
                        found=True
                    
            if found:
                print(f"\nThe book('{title}') has been successfully remove")
            else:
                print(f"\nBook('{title}') not found.")
        except FileNotFoundError:
            print("\nThe file does not exsist.")

def menu():
    print("\n----------MENU----------")
    print("1- List Books")
    print("2- Add Book")
    print("3- Remove Book")
    print("4- Quit\n")

def main():

    lib=Library("books.txt")

    while True:
        menu()

        select=input("\n--Enter your select 1-4: ")

        if select=="1":
            print("\nList Books: ")
            lib.listBooks()
        elif select =="2":
            print("\nAdding Book: ")
            lib.addBook()
        elif select=="3":
            print("\nRemove Book: ")
            lib.removeBook()
        elif select=="4":
            print("\nExiting")
            break
        else:
            print("Please try again")

if __name__ == "__main__":
    main()





