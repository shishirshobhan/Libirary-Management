import datetime
import list  # Using Modularity
class LMS:  # Creating Class LMS
    def __init__(self):  # Creating init function
        self.BookName = []  # List to store name of the Book
        self.author = []  # List to store name of the author name
        self.quantity = []  # List to store quantity of the book
        self.cost = []  # List to store Cost of the book
    def addd(self):  # Creating addd function
        booknames = input("Enter the name of the book you want to add: ")  # Asking user to input book name
        author = input("Enter the name of the author: ")  # Asking user to input author name
        quantity = int(input("Enter the total quantity of the book: "))  # Asking user to input available quantity of the book
        cost = input("Enter the price for the book to borrow: ")  # Asking user the cost of book to borrow
        with open("book_list.txt", "a") as adding:
            adding.write("\n")
            adding.write(f"{booknames},{author},{str(quantity)},{cost}")  # Adding book in book list.

            print("You have successfully added book on the book list.")  # Showing message to the user.

    def ask(self): # Creating function name ask consisting menu prompt
        print("Welcome To Libirary Management System")
        # Creating menu prompt options
        menu_prompt = """Please choose one of the following options." 

        -Type 'a' to add a book in Book List
        -Type 'b' to borrow books 
        -Type 'r' to return borrowed books
        -Type 'l' to list the books available in library.
        -Type 'q' to quit the program
         what would you like to do : """

        selected_option = input(menu_prompt).strip().lower()
        while selected_option != "q":
            if selected_option == "a":  # If user input a then addd function will be working
                self.addd()
            elif selected_option == "l":  # If user input l then the list of available books will be displayed
                list.show_books()
            elif selected_option == "b":  # If user input b then function borrow will be working
                self.borrow()
            elif selected_option == "r":  # If user input r then the function returnBook will be working
                self.returnBook()
            else:
                print(f"Sorry, '{selected_option}' is a invalid option, please choose a valid option")  # Showing message

            selected_option = input(menu_prompt).strip().lower() # changing uppercase to lowercase

    def book_divide(self):  # Creating book_divide functions
        with open("book_list.txt", "r") as f:
            lines = f.readlines()
            lines = [x.strip('\n') for x in lines]
            for i in range(len(lines)):
                end = 0
                for a in lines[i].split(','):
                    if (end == 0):
                        self.BookName.append(a)  # append book name in first position
                    elif (end == 1):
                        self.author.append(a)  # append author name second position
                    elif (end == 2):
                        self.quantity.append(a)  # append quantity of the book third position
                    elif (end == 3):
                        self.cost.append(a.strip("Rs."))  # append cost of the book fourth position
                    end += 1

    def getDate(self):  # Creating getDate function to get current date
        now = datetime.datetime.now
        return str(now().date())

    def getTime(self):  # Creating getTime function to get current time
        now = datetime.datetime.now
        return str(now().time())

    def borrow(self):  # Creating borrow function
        self.book_divide()
        taken = False
        Date = datetime.date.today()  # display current date
        delaydate = datetime.timedelta(days=10)  # display date after 10 days
        X = str(Date + delaydate)  # display date and delay date
        while (True):
            firstName = input("Enter the first name of the borrower: ")  # Asking user to input first name
            if firstName.isalpha():  # If user input other than alphabet in their name
                break
            print("please input alphabet from A-Z")  # display message
        while (True):  # If user input genuine name
            lastName = input("Enter the last name of the borrower: ")  # Asking user to input last name
            if lastName.isalpha():  # If user input other than alphabet in their name
                break
            print("please input alphabet from A-Z")  # display message

        while taken == False:
            for i in range(len(self.BookName)):
                print(i, " number for ", self.BookName[i])  # Shows book number in book list
            try:
                self.book = int(input("enter book number: "))  # Asking user to input book number
                t = "Borrow-" + firstName + ".txt"  # stores borrower information in text file
                with open(t, "w+") as f:  # Display borrow bill
                    f.write("               Library Management System  \n")
                    f.write("                   Borrowed By: " + firstName + " " + lastName + "\n")
                    f.write(
                        f"   Borrowed Date:   {self.getDate()}             Time :    {self.getTime()}      Returning Date : {X}\n\n")
                    f.write("S.N. \t\t Bookname \t      Authorname \n")
                try:
                    if (int(self.quantity[self.book]) > 0):  # Checks book quantity
                        print("Book you want to borrow is available for you. ")  # shows message
                        with open(t, "a")as f:
                            f.write("1. \t\t" + self.BookName[self.book] + "\t\t  " + self.author[self.book] + "\n")
                        print("Please return the book within " + str(X))
                        self.quantity[self.book] = int(self.quantity[self.book]) - 1   # Decreases quantity from book list
                        with open("book_list.txt", "w") as f:  # Display book list
                            for i in range(len(self.BookName)):
                                f.write(
                                    f"{self.BookName[i]},{self.author[i]},{str(self.quantity[i])},{self.cost[i]}\n")

                        loop = True
                        count = 1
                        while loop == True:  # creating loop
                            choice = str(input(
                                "Do you want to borrow another book? Remember you cannot borrow the same book again until you returned it. Press y for yes and n for no."))
                            if (choice.upper() == "Y"):
                                count = count + 1
                                print("Please select an option below:")  # Asking user to select option
                                for i in range(len(self.BookName)):  # shows book number
                                    print("Enter", i, "to borrow book", self.BookName[i])
                                self.book = int(input("Enter the book number you want to borrow: ")) # Asking user to input book number
                                if (int(self.quantity[self.book]) > 0):  # Checks book quantity
                                    print("Book you want to borrow is available for you.")  # displaying message
                                    with open(t, "a") as f:
                                        f.write(str(count) + ". \t\t" + self.BookName[self.book] + "\t\t  " +
                                                self.author[self.book] + "\n")
                                    self.quantity[self.book] = int(self.quantity[self.book]) - 1  # Decrease quantity of the book by -1 when borrowed
                                    with open("book_list.txt", "w") as f:
                                        for i in range(len(self.BookName)):  # Display book number and details
                                            f.write(
                                                f"{self.BookName[i]},{self.author[i]},{str(self.quantity[i])},{self.cost[i]}\n")
                                            taken = False
                                else:
                                    loop = False
                                    break
                            elif (choice.upper() == "N"):  # When borrower don't want to borrow again
                                print("You have successfully borrowed the books you want! Thank you for choosing our Libirary. ")  # Display message
                                print("")
                                loop = False
                                taken = True
                            else:
                                print("Please enter the command as instructed")  # When user input other than option provided

                    else:
                        print("Sorry !Book is not available, please wait for some days.")  # When book is out odf stock
                        taken = False
                except IndexError:
                    print("")
                    print("Please choose book according to the number provided.")  # When user invalid book number
            except ValueError:
                print("")
                print("Please choose as suggested to borrow books you want.")  # Guidance for user

    def returnBook(self):  # Creating returnBook function
        self.book_divide()  # Calling book_divide function
        name = input("Enter the name of borrower: ")  # Asking user to input borrower name
        a = "Borrow-" + name + ".txt"  # Checks borrower name in text file
        try:
            with open(a, "r") as f:  # when user input valid name
                lines = f.readlines()
                lines = [a.strip("$") for a in lines]
            with open(a, "r") as f:
                data = f.read()
                print(data)
        except:  # Show message when borrower name is invalid
            print("The name of the borrower you entered is incorrect. Please, make sure you entered correctly.")
            self.returnBook()  # calling returnBook Function

        b = "Return-" + name + ".txt"
        with open(b, "w+")as f:  # Display borrower details
            f.write("                Library Management System \n")
            f.write("    Date: " + self.getDate() + "    Time:" + self.getTime() + "\n\n")
            f.write("S.N.\t\tBookname\t\tCost\n")

        total = 0.0  # calculating total price of borrowed books
        for i in range(len(self.BookName)):
            if self.BookName[i] in data:
                with open(b, "a") as f:
                    f.write(str(i + 1) + "\t\t" + self.BookName[i] + "\t\t" + "$" + self.cost[i] + "\n")
                    self.quantity[i] = int(self.quantity[i]) + 1
                total += int(self.cost[i])

        print("\t\t\t\t\t\t\t" + "$" + str(total))
        print("Check whether the book return date is expired or not.")  # Asking user to check date
        print("Press Y for Yes and N for No")  # Asking user to input either Y or N
        stat = input()
        if (stat.upper() == "Y"):  # When user input Y
            print("Enter the number of delayed days to return book.")  # Asking user to enter total number of delayed days
            day = int(input())
            fine = 2 * day  # Calculating fine
            with open(b, "a")as f:
                f.write("\t\t\t\t\tFine: $" + str(fine) + "\n")
            total = total + fine  # Calculating total price along with fine

        print("Final Total: " + "$" + str(total))
        with open(b, "a")as f:
            f.write(f"\t\t\t\t\t Total:  ${str(total)}")  # Storing details

        with open("book_list.txt", "w") as f:
            for i in range(len(self.BookName)):
                f.write(f"{self.BookName[i]},{self.author[i]},{str(self.quantity[i])},{self.cost[i]}\n")
def main():  # creating main function
    Library1 = LMS()
    Library1.ask()
main()
