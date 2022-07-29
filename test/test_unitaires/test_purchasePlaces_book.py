from app.views import MAX_POINTS

expected_flash_great_booking = "Great-booking complete!."
expected_flash_points_negative = "Error! You cannot reserve null or negative places."
expected_flash_points_sup_club_inf_competition = "Error! You try to use more places than you have available."

def test_purchase_places(client):
    response = client.get("/purchasePlaces")
    assert response.status_code == 405

def test_purchase_places_great(client, club_fixture, competition_fixture):
    places = 1
    response = client.post("/purchasePlaces", data={"competition": competition_fixture["name"], "club": club_fixture["name"], "places": places })
    data = response.data.decode()
    assert response.status_code == 200
    assert expected_flash_great_booking in data

def test_purchase_places_negative(client, club_fixture, competition_fixture):
    places_negative = -1
    response_error_negative = client.post("/purchasePlaces", data={"competition": competition_fixture["name"], "club": club_fixture["name"], "places": places_negative })
    data_negative = response_error_negative.data.decode()
    assert expected_flash_points_negative in data_negative
    assert response_error_negative.status_code == 200

def test_purchase_places_sup_club_inf_competition(client, club_fixture, competition_fixture):
    places = int(club_fixture["points"] ) + 1
    response = client.post("/purchasePlaces", data={"competition": competition_fixture["name"], "club": club_fixture["name"], "places": places })
    data = response.data.decode()
    assert expected_flash_points_sup_club_inf_competition in data
    assert response.status_code == 200

def test_purchase_places_sup_max_points(client, club_fixture, competition_fixture):
    places = MAX_POINTS + 1
    response = client.post("/purchasePlaces", data={"competition": competition_fixture["name"], "club": club_fixture["name"], "places": places })
    assert response.status_code == 200
    data = response.data.decode()
    #assert "Sorry! It is only possible to reserve between 0 and {MAX_POINTS} places in each competition." in data

def test_purchase_places_sup_competition(client, club_fixture, competition_fixture):
    places = int(competition_fixture["numberOfPlaces"]) + 1
    response = client.post("/purchasePlaces", data={"competition": competition_fixture["name"], "club": club_fixture["name"], "places": places })
    assert response.status_code == 200
    data = response.data.decode()
    assert "Error! you try to reserve more places than are available for this competition." in data

def test_book_url_ok(client, club_fixture, competition_fixture):
    club = club_fixture["name"]
    competition = competition_fixture["name"]
    response = client.get(f'/book/{competition}/{club}')
    assert response.status_code == 200

# def test_book_url_ok(client, club_fixture, competition_fixture_error):
#     response = client.get(f'/book/{competition_fixture_error["name"]}/{club_fixture["name"]}', follow_redirects=True)
#     data = response.data.decode()
#     assert response.status_code == 404
#     assert "Something went wrong-please try again" in data  
    