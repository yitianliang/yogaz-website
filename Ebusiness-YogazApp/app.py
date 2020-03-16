from flask import Flask, flash, redirect, escape, request, render_template, send_from_directory, session, abort
import sqlite3
from flask import g
from flask_login import LoginManager
import os

app = Flask(__name__)
login_manager = LoginManager(app)
login_manager.init_app(app)
app.secret_key = os.urandom(12)

DATABASE = 'yogaz.db'

# DB config and functions


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('yogaz.db')
    return db


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Session Control


def NoActiveSession():
    return not session or not session['logged_in']

# Getting User Info


def GetUserInfo(username, password):
    con = get_db()
    cur = con.cursor()
    cur.execute(
        "SELECT * FROM user WHERE username = ? and password = ? limit 1;", (username, password))
    userdata = cur.fetchall()
    return userdata


def GetBookingInfo(userId):
    con = get_db()
    cur = con.cursor()
    cur.execute(
        "SELECT classSchedule.datetime, classSchedule.description, classSchedule.classScheduleId from classSchedule join booking on classSchedule.classScheduleId = booking.classScheduleId WHERE booking.userID = ?;", [userId])
    bookingdata = cur.fetchall()
    return bookingdata


def GetClassSchedule():
    con = get_db()
    cur = con.cursor()
    cur.execute("select * from classSchedule;")
    rows = cur.fetchall()
    return rows

# main page always GET
@app.route('/')
def indexpage():
    if NoActiveSession():
        return render_template('index.html')
    else:
        return render_template('indexlogin.html', result=session['userdata'])

# login manager
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# Routes to static content
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)


@app.route('/pic/<path:path>')
def send_pic(path):
    return send_from_directory('static/pic', path)


@app.route('/json/<path:path>')
def send_json(path):
    return send_from_directory('templates/json', path)


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static/pic', path)

# Sub pages
@app.route('/signup.html')
def signup():
    if NoActiveSession():
        return render_template('signup.html')
    else:
        return indexpage()


@app.route('/result.html', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        con = get_db()
        cur = con.cursor()
        cur.execute("INSERT INTO user (firstName, lastName, username, password, email, address, address2, country, state, zip) VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (result['firstName'], result['lastName'], result['username'], result['password'], result['email'], result['address'], result['address2'], result['country'], result['state'], result['zip']))
        con.commit()
        con.close()
        return render_template("result.html", result=result)
    else:
        return render_template("index.html")


@app.route('/aboutUs.html')
def aboutUs():
    return render_template('aboutUs.html')


@app.route('/classSchedule.html')
def classSchedule():
    rows = GetClassSchedule()
    return render_template('classSchedule.html', rows=rows)


@app.route('/contactUs.html')
def contactUs():
    return render_template('contactUs.html')


@app.route('/index.html')
def indexPage():
    return indexpage()


@app.route('/profile.html', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        result = request.form
        if 'username' in result.keys():  # Login through index page
            userdata = GetUserInfo(result['username'], result['password'])
            if not userdata:
                flash('Authentication Error, please try again')
                session['logged_in'] = False
                return indexpage()
            else:
                session['logged_in'] = True
                userId = str(userdata[0][0])
                session['userdata'] = userdata[0]
                #session['classesdata'] = GetBookingInfo(userId)
                # return render_template('profile.html', userdata=userdata[0], classesdata=classesdata)
        else:
            userId = session['userdata'][0]
        session['classesdata'] = GetBookingInfo(userId)
        return render_template('profile.html', userdata=session['userdata'], classesdata=session['classesdata'])

    else:
        if NoActiveSession():
            return indexpage()
        else:
            return render_template('profile.html', userdata=session['userdata'], classesdata=session['classesdata'])


@app.route('/beginner.html')
def beginner():
    return render_template('beginner.html')


@app.route('/trainer.html')
def trainer():
    con = get_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM trainer;")
    rows = cur.fetchall()
    return render_template('trainer.html', rows=rows)


@app.route('/classType.html')
def classType():
    rows = GetClassSchedule()
    return render_template('classType2.html', rows=rows)


@app.route('/bookclass',  methods=['GET', 'POST'])
def bookClass():
    if NoActiveSession():
        return signup()
    if not NoActiveSession():
        userId = str(session['userdata'][0])
        classesdata = GetBookingInfo(userId)
        if request.method == 'POST':
            result = request.form
            if result['classId'] not in classesdata:
                con = get_db()
                cur = con.cursor()
                cur.execute("INSERT INTO booking (classScheduleId, userID) VALUES (?, ?)",
                            (result['classId'], str(session['userdata'][0])))
                con.commit()
                session['classesdata'] = classesdata
                return profile()
            else:
                return classType()


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('userdata', None)
    session['logged_in'] = False
    return render_template('index.html')


# main
if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host="0.0.0.0", port=8888, debug=True)
