class Member():
    def __init__(self, m):
        self.name = m["name"]
        self.team = m["team"]
        self.position = m["pos"]
        self.board = m["board"]
        self.github = m["github"]
        self.email = m["email"]
    
    def writeToCSV(self, f):
        line = "{},{},{},{},{},{}".format(self.name, self.email, self.github, self.team, self.position, self.board)
        print(line, file=f)

    def mergeMembers(self, m):
        if self.name != m.name:
            self.name = m.name
        if self.team != m.team:
            self.team = m.team
        if self.position != m.position:
            self.position = m.position
        if self.github != m.github:
            self.github = m.github
        if self.email != m.email:
            self.email = m.email
        
        if m.board and self.board != m.board:
            self.board = m.board

def main():
    fallCSV = open('fall2017.csv', 'r')
    wCSV = open('w2018.csv', 'r')
    winterCSV = open('winter2018.csv', 'w')

    print("Name,Email,GitHub,Team,Position,Board", file=winterCSV)


    members = {}

    for line in fallCSV:
        line = line.rstrip().split(',')
        print(line)
        m = {}


        m["pos"] = line[0]
        m["name"] = line[1]
        m["email"] = line[2]
        m["team"] = line[3]
        m["board"] = line[4]
        m["github"] = line[5]

        member = Member(m)
        members[m["name"]] = member
    
    for line in wCSV:
        line = line.rstrip().split(',')
        m = {}

        m["name"] = line[0]
        m["jr"] = line[1]
        m["pos"] = line[2]
        m["team"] = line[3]
        m["github"] = line[4]
        m["email"] = line[5]
        m["board"] = ""

        if m["jr"] == "Yes":
            m["pos"] = m["pos"] + " (JR)"
        
        member = Member(m)
        if m["name"] in members:
            prev = members[m["name"]]
            prev.mergeMembers(member)
            members[m["name"]] = prev
        else:
            members[m["name"]] = member
    
    for name in members:
        member = members[name]
        member.writeToCSV(winterCSV)

    fallCSV.close()
    wCSV.close()
    winterCSV.close()



if __name__ == '__main__':
    main()