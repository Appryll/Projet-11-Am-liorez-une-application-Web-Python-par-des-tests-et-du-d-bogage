def test_int_showSummary(client, club_fixture):
    response = client.post("/showSummary", data={"email": club_fixture["email"]})
    assert f'Welcome, {club_fixture["email"]}' in response.data.decode()
    assert f'Club points available : {club_fixture["points"]}' in response.data.decode()

def test_int_showSummary(client, club_fixture, competition_fixture):
    response = client.get(f'/book/{competition_fixture["name"]}/{club_fixture["name"]}')
    assert f'Competitions places available : {competition_fixture["numberOfPlaces"]}' in response.data.decode()