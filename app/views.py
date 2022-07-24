from app import app
from server import loadClubs, loadCompetitions
from flask import render_template, redirect, flash, request, url_for, session

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')


# ERROR: Entering a unknown email crashes the app
# Code should be written to ensure that if something goes wrong (like the email isn't found), 
# the error is caught and handled. Display an error message like "Sorry, that email wasn't found." 
@app.route('/showSummary', methods=['POST'])
def showSummary():
    if request.method == 'POST':
        try:
            user= request.form['email']
            session["user"] = user
            club = [club for club in clubs if club['email'] == request.form['email']][0]
            return render_template('welcome.html', club=club, competitions=competitions, user=user)
        except:
            if request.form['email'] == '':
                flash('Please, enter your email address.')
            else:
                flash('Sorry, that email wasn\'t found. Please try again.')

            return render_template('index.html'), 401


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for('index'))
