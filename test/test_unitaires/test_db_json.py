from server import loadClubs, loadCompetitions, loadCompetitionsEssai

def loadCompetitionsEssai(self):
    compet_essai = loadCompetitionsEssai('competitions_essai.json')
    expected = [{
                "competitions_essai": [
                {
                    "name": "Spring Festival",
                    "date": "2020-03-27 10:00:00",
                    "numberOfPlaces": "25"
                },
                {
                    "name": "Fall Classic",
                    "date": "2020-10-22 13:30:00",
                    "numberOfPlaces": "13"
                },
                {
                    "name": "Jeux Olympiques d'hiver Maisons Laffitte",
                    "date": "2024-05-09 10:00:00",
                    "numberOfPlaces": "40"
                },
                {
                    "name": "Jumping Maisons Laffitte",
                    "date": "2023-03-08 10:00:00",
                    "numberOfPlaces": "50"
                }
                                        ]
                }]
    assert compet_essai == expected

def loadCompetitions(self):   
    compet = loadCompetitions('competitions.json')
    expected = [{
                "competitions": [
                    {
                        "name": "Spring Festival",
                        "date": "2020-03-27 10:00:00",
                        "numberOfPlaces": "25"
                    },
                    {
                        "name": "Fall Classic",
                        "date": "2020-10-22 13:30:00",
                        "numberOfPlaces": "13"
                    }
                                ]
                }]
    assert compet == expected

def loadClubs(self):   
    clubs = loadClubs('clubs.json')
    expected = [{"clubs":[
                    {
                        "name":"Simply Lift",
                        "email":"john@simplylift.co",
                        "points":"13"
                    },
                    {
                        "name":"Iron Temple",
                        "email": "admin@irontemple.com",
                        "points":"4"
                    },
                    {   "name":"She Lifts",
                        "email": "kate@shelifts.co.uk",
                        "points":"12"
                    }
                        ]
                }]
    assert clubs == expected
    