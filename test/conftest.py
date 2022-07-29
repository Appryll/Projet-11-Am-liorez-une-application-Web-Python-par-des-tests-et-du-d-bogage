import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def club_fixture():
    data_club = {"name":"Simply Lift",
                "email":"john@simplylift.co",
                "points":"13"}
    return data_club

@pytest.fixture
def competition_fixture():
    data_competition = {"name": "Spring Festival",
                "date": "2020-03-27 10:00:00",
                "numberOfPlaces": "25"}
    return data_competition
