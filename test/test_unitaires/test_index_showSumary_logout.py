expected_flash_invalid_mail_message = 'Sorry, that email is not valid. Please try again.'
expected_flash_empty_mail_message = 'Please, enter your email address.'

def test_index(client, club_fixture):
    response = client.get('/')
    data = response.data.decode()
    assert club_fixture["name"] in data
    assert club_fixture["points"] in data
    assert response.status_code == 200

def test_showSumary(client):
    response = client.get("/showSummary")
    assert response.status_code == 405
  
def test_showSummary_valid_mail(client, club_fixture):
    response = client.post("/showSummary", data={"email": club_fixture["email"]})
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