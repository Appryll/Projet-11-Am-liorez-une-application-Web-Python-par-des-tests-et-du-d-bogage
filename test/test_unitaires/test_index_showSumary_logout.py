# from test.conftest import client
from flask import session, url_for, request

expected_flash_invalid_mail_message = '<h5>Sorry, that email is not valid. Please try again.</h5>'
expected_flash_empty_mail_message = '<h5>Please, enter your email address.</h5>'

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
  
def test_showSummary_valid_mail(client):
    response = client.post("/showSummary", data={"email": "john@simplylift.co"})
    assert response.status_code == 200

def test_showSummary_invalid_mail(client):
    response = client.post("/showSummary", data={"email": "invalid@email.co"})
    assert response.status_code == 401
    data = response.data.decode()
    assert expected_flash_invalid_mail_message in data

def test_showSummary_empty_email(client):
    response = client.post("/showSummary", data={"email": " "})
    assert response.status_code == 401
    data = response.data.decode()
    assert expected_flash_invalid_mail_message in data

def test_logout_redirect(client):
    response = client.get("/logout", follow_redirects=True)
    assert response.request.path == "/"