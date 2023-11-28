import json, os

class PasswordManage():
    def __init__(self) -> None:
        self.path = 'C:/Users/allen/Music/Codequest/AWSCC-CodeQuest-Backend/backend/day-15/data.json'
        self.data = {}
        self.websites = []
        self.userChoice = ''
        self.openFile()
        pass

    def generateUI(self):
        print("Password Manager:\n1. Add Password\n2. View all Password\n3. Search for Website\n4. Delete Input\n5. Update a Password\n6. Quit")
        self.userChoice = input("Enter your Input: ")
        self.checkChoice(self.userChoice)
    
    def checkChoice(self, choice):
        if choice == '1':
            self.addPassword()
        elif choice == '2':
            self.viewPasswords()
        elif choice == '3':
            self.searchPasswords()
        elif choice == '4':
            self.deletePassword()
        elif choice == '5':
            self.updatePassword()
        elif choice == '6':
            print('\n Goodbyee !\n')
        else:
            print("\nEnter a Vaild Choice.\n")
            self.generateUI()

    def openFile(self):
        print('open file')
        if not os.path.exists('data.json'):
            with open('data.json', 'w') as f:
                json.dump({}, f)
        else:
            with open(self.path, 'r') as f:
                self.data = json.load(f)
                self.websites = list(self.data.keys())

    def saveFile(self):
        with open(self.path, 'w') as f:
            json.dump(self.data, f)
    
    def addPassword(self):
        print('\n Add Password \n')
        website = input("Enter website:")
        if website in self.data:
            print("Website Exits.\n")
            email = input("Enter Email: ")
            password = input("Enter Password: ")
            self.data[website].append({'email' : email, 'password' : password})
            pass
        else:
            email = input("Enter Email: ")
            password = input("Enter Password: ")
            self.data[website] = {'email' : email, 'password' : password}
        self.generateUI()
        pass

    def viewPasswords(self):
        print('\n View Password \n')
        print("Passwords:\n")
        for websites, credentials in self.data.items():
            print(f"----------------------\nWebsite: {websites}")
            for credential in credentials:
                print("Current:", credential)
                print(f"Email: {credential['email']}\n Password: {credential['password']}")
        self.generateUI()
    
    def searchPasswords(self):
        print('\n Search Password \n') 
        website = input("\nEnter Website to search: ") 
        if website in self.data:
            print(f"Website: {website}\n")
            for credential in self.data[website]:
                print(f"Email: {credential['email']}\n Password: {credential['password']}")
            print('\n')
        self.generateUI()
        pass

    def deletePassword(self):
        print('\n Delete Password \n')

        self.generateUI()
        pass

    def updatePassword(self):
        print('\n Update Password \n')
        self.generateUI()
        pass


app = PasswordManage()
app.generateUI()
