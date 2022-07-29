import json, datetime

def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs
         
def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions

def loadCompetitionsEssai():
    with open('competitions_essai.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        date_format = "%Y-%m-%d %H:%M:%S"
        for competitions in listOfCompetitions:
            competitions['date'] = datetime.datetime.strptime(competitions["date"], date_format)
            if competitions['date'] < datetime.datetime.now():
                competitions['in_the_past'] = True
            else:
                competitions['in_the_past'] = False              
        return listOfCompetitions