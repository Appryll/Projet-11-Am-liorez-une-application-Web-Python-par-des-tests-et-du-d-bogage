from locust import HttpUser, task

class ProjectPerfTest(HttpUser):
    
    @task
    def index(self):
        self.client.get('')

    @task 
    def showSummary(self):
        self.client.post("showSummary", {"email": "john@simplylift.co"})
    
    @task
    def book(self):
        club = "Simply Lift"
        competition = "Fall Classic"
        self.client.get(f'book/{competition}/{club}')

    @task
    def purchasePlaces(self):
        data = {
            'club': "Simply Lift",
            'competition': "Fall Classic",
            'places': 1
        }
        self.client.post("purchasePlaces", data)

    @task
    def logout(self):
        self.client.get("logout")