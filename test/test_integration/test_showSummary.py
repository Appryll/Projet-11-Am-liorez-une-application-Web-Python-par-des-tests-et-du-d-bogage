from flask import session

def test_int_showSummary(client, club_fixture):
    response = client.post("/showSummary", data={"email": club_fixture["email"]})
    assert f'Welcome, {club_fixture["email"]}' in response.data.decode()
    assert f'Club points available : {club_fixture["points"]}'
