import json


f2017 = open('fall2017.json', 'r')
f = open('w2018.csv', 'r')
w2018 = open('winter2018.json', 'w')

fall = json.load(f2017)

winter = {
    "schema": 2,
    "data": {
        "teams": fall["data"]["teams"],
        "members": fall["data"]["members"]
    }
}

teams = set()

for team in fall["data"]["teams"]:
    teams.add(team["name"])

already = set()

for member in fall["data"]["members"]:
    if member["github"].lower() in already:
        continue
    else:
        already.add(member["github"].lower())

for line in f:
    line = line.rstrip()
    cols = line.split(',')
    name = cols[0]
    pos = cols[2]
    team = cols[3]
    github = cols[4].lower()

    if github in already:
        continue

    if team not in teams:
        winter["data"]["teams"].append({
            "name": team,
            "description": "replace this.",
            "image": "/assets/projects/"
        })
        teams.add(team)

    if pos == 'PM':
        pos = 'Product Manager'
    elif pos == 'Designer':
        pos = 'Designer'
    else:
        pos = 'Developer'

        if cols[1] == 'Yes':
            pos = 'Jr. Developer'
        

    image = "assets/profiles/" + name.lower().replace(' ', '_').replace('-', '_') + '.jpg'

    member = {
        "name": name,
        "github": github,
        "team": team,
        "title": pos,
        "image": image
    }

    winter["data"]["members"].append(member)

json.dump(winter, w2018)

f2017.close()
f.close()
w2018.close()


