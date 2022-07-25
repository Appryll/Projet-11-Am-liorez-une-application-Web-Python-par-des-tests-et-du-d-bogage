from app import app
from server import loadClubs, loadCompetitions
from flask import render_template, redirect, flash, request, url_for, session

competitions = loadCompetitions()
clubs = loadClubs()
MAX_POINTS = 12

@app.route('/')
def index():
    return render_template('index.html')
    

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
                flash('Please, enter your email address.', 'warning')
            else:
                flash('Sorry, that email is not valid. Please try again.', 'danger')
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


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places'])
    places_available = int(competition['numberOfPlaces'])

    # Places required greater than those available by the club and less than or equal to the places for the competition
    if places_required > int(club['points']) and places_required <= places_available:
        flash('Error! You try to use more places than you have available', 'danger')
        return render_template('booking.html',club=club, competition=competition)
    # Required places greater than those available for the competition
    elif places_required > places_available:
        flash(f'Error! you try to reserve more places than are available for this competition. {places_available} vacancies remain.', 'danger')
        return render_template('booking.html', club=club, competition=competition)
    # Places greater than 12 because the maximum per club is 12
    elif places_required > MAX_POINTS:
        flash(f'Sorry! It is only possible to reserve between 0 and {MAX_POINTS} places in each competition', 'warning')
        return render_template('booking.html', club=club, competition=competition)
    # Reserve 0 places or negative
    elif places_required <= 0:
        flash('Error! You cannot reserve null or negative places', 'danger')
        return render_template('booking.html', club=club, competition=competition)
    else:
        flash('Great-booking complete!', 'info')
        club['points'] = int(club['points']) - places_required
        competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
        return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display
@app.route('/pointsAvailable', methods=['GET'])
def pointsAvailable():
    return render_template('points_available_club.html', clubs=clubs)


@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for('index'))
