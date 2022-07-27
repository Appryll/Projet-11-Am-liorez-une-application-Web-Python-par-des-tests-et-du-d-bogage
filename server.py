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
        listOfCompetitionsEssai = json.load(comps)['competitions_essai']
        date_format = "%Y-%m-%d %H:%M:%S"
        for competitions_essai in listOfCompetitionsEssai:
            competitions_essai['date'] = datetime.datetime.strptime(competitions_essai["date"], date_format)
            if competitions_essai['date'] < datetime.datetime.now():
                competitions_essai['in_the_past'] = True
            else:
                competitions_essai['in_the_past'] = False              
        return listOfCompetitionsEssai
