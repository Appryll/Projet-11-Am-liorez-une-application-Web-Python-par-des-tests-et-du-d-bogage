# from test.conftest import client
# from flask import session, url_for, request

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
  
def test_showSummary_valid_mail(client):
    response = client.post("/showSummary", data={"email": "john@simplylift.co"})
    assert response.status_code == 200

def test_showSummary_invalid_mail(client):
    response = client.post("/showSummary", data={"email": "invalid@email.co"})
    assert response.status_code == 401

def test_showSummary_empty_email(client):
    response = client.post("/showSummary", data={"email": " "})
    assert response.status_code == 401

def test_logout_redirect(client):
    response = client.get("/logout", follow_redirects=True)
    assert response.request.path == "/"