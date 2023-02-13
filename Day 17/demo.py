class User:
    def __init__(self, id, username, followers=0):
    #initialise the user object with name and id
        self.name = username
        self.id = id
        self.followers = followers

    def printUser(self):
        print("User: " + self.name + " ID: " + self.id + " Followers: " + str(self.followers))

u1 = User('001', "Johnny")
u2 = User('002', "Sins", 100)

u1.printUser()
u2.printUser()