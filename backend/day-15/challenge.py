import json, os

class PasswordManage():
    def __init__(self) -> None:
        self.path = './backend/day-15/data.json'
        self.data = {}
        self.userChoice = ''
        self.openFile()

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
            except json.decoder.JSONDecodeError:
                print("Error decoding JSON. File might be empty or not in valid JSON format.")
                self.data = {}

    def saveFile(self):
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=4)
    
    def addPassword(self):
        os.system('cls')
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

    def viewPasswords(self):
        os.system('cls')
        print('\n View Password \n')
        print("Passwords:\n")
        for websites, credentials in self.data.items():
            for credential in credentials:
                print(f" Website: {websites}\n Id: {credential['id']}\n Email: {credential['email']}\n Password: {credential['password']}\n")
    
    def searchPasswords(self):
        os.system('cls')
        print('\n Search Password \n') 
        website = input("\nEnter Website to search: ") 
        if website in self.data:
            print(f"Website: {website}\n")
            for credential in self.data[website]:
                print(f"ID: {credential['id']}\n Email: {credential['email']}\n Password: {credential['password']}\n")
        else:
            print("Website does not exist.\n")


    def deletePassword(self):
        os.system('cls')
        print('\n Delete Password \n')
        website = input("Enter website: ")
        results = self.getWebsite(website, True)
        if results:
            id_to_rmove, credentials = results
            updatedCreds = []
            for credential in credentials:
                if id_to_rmove != credential['id']:
                    updatedCreds.append(credential)
            self.data[website] = updatedCreds
            self.saveFile()
                
    def updatePassword(self):
        os.system('cls')
        print('\n Update Password \n')
        website = input("Enter Website: ")
        result = self.getWebsite(website, True)
        if result:
            id_to_update, credentials = result
            for credential in credentials:
                if credential['id'] == id_to_update:
                    new_email = input("Enter new Email (leave blank to keep the current one): ")
                    new_password = input("Enter new Password (leave blank to keep the current one): ")
                if new_email:
                    credential['email'] = new_email
                if new_password:
                    credential['password'] = new_password
            print("Password updated successfully!\n")
            self.saveFile()

    def getWebsite(self, website, needID):
        if website in self.data:
            credentials = self.data[website]
            for credential in credentials:
                print(f"Website: {website}\nID: {credential['id']}\nEmail: {credential['email']}\nPassword: {credential['password']}\n")
                if needID:
                    while True:
                        try:
                            id_to_update = int(input("Enter ID:"))
                            break
                        except:
                            print("Enter Valid Value.")
                    return id_to_update, credentials
        else:
            print('Website does not exist.\n')

app = PasswordManage()
while True:
    app.generateUI()
    if app.userChoice == '6':
        break