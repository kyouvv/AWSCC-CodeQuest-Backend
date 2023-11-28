import json, os

class PasswordManage():
    def __init__(self) -> None:
        self.path = 'C:/Users/allen/Music/Codequest/AWSCC-CodeQuest-Backend/backend/day-15/data.json'
        self.data = {}
        self.websites = []
        self.userChoice = ''
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
            try:
                with open(self.path, 'r') as f:
                    self.data = json.load(f)
                    self.websites = list(self.data.keys())
            except json.decoder.JSONDecodeError:
                print("Error decoding JSON. File might be empty or not in valid JSON format.")
                self.data = {}

    def saveFile(self):
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=4)
    
    def addPassword(self):
        print('\n Add Password \n')
        website = input("Enter website:")
        id = 1
        if website in self.data:
            print("Website Exits.\n")
            email = input("Enter Email: ")
            password = input("Enter Password: ")
            id = len(self.data[website]) + 1
            self.data[website].append({'id' : id, 'email' : email, 'password' : password})
            pass
        else:
            email = input("Enter Email: ")
            password = input("Enter Password: ")
            self.data[website] = [{'id' : id, 'email' : email, 'password' : password}]
        self.saveFile()
        self.generateUI()
        pass

    def viewPasswords(self):
        self.openFile()
        print('\n View Password \n')
        print("Passwords:\n")
        for websites, credentials in self.data.items():
            for credential in credentials:
                print(f" Website: {websites}\n Id: {credential['id']}\n Email: {credential['email']}\n Password: {credential['password']}\n")
        self.generateUI()
    
    def searchPasswords(self):
        self.openFile()
        print('\n Search Password \n') 
        website = input("\nEnter Website to search: ") 
        if website in self.data:
            print(f"Website: {website}\n")
            for credential in self.data[website]:
                print(f"ID: {credential['id']}\n Email: {credential['email']}\n Password: {credential['password']}\n")
            print('\n')
        self.generateUI()
        pass

    def deletePassword(self):
        print('\n Delete Password \n')
        website = input("Enter website: ")
        if website in self.data:
            if len(self.data[website]) > 1:
                pass
            else:
                pass
                
        self.generateUI()
        pass

    def updatePassword(self):
        print('\n Update Password \n')
        self.generateUI()
        pass


app = PasswordManage()
app.generateUI()
