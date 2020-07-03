class ContactInfo:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return "Name: " + str(self.name) + "\n" + "Phone: " + str(self.phone) + "\n" + "Email: " + str(self.email)

    def getName():
        return self.name

    def getPhoneNumber():
        return self.phone

    def getEmailAddress():
        return self.email
