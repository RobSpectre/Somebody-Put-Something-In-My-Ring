import os
from flask import Flask
from flask import request
from flask import url_for
from twilio import twiml


app = Flask(__name__)


@app.route('/voice', methods=['POST'])
def voice():
    resp = twiml.Response()
    resp.say("Hey. Ho. Let's go.")
    resp.say("I'm going to put something in your ring.")
    with resp.gather(action="/play") as g:
        g.say("For The K K K Took My Baby Away, press 1.")
        g.say("For Blitzkrieg Bop, press 2.")
        g.say("For Sheena Is A Punk Rocker, press 3.")
        g.say("For Outsider, press 4.")
    resp.pause(length="3")
    path = url_for('.voice')
    resp.redirect(path)
    return str(resp)


@app.route('/play', methods=['POST'])
def play():
    resp = twiml.Response()
    if request.form['Digits'] == '1':
        song = url_for('static', filename='the_kkk_took_my_baby_away.mp3')
    elif request.form['Digits'] == '2':
        song = url_for('static', filename='blitzkrieg_bop.mp3')
    elif request.form['Digits'] == '3':
        song = url_for('static', filename='sheena_is_a_punk_rocker.mp3')
    elif request.form['Digits'] == '4':
        song = url_for('static', filename='outsider.mp3')
    else:
        resp.say("I'm sorry - I did not understand your request.")
        path = url_for('.voice')
        resp.redirect(path)
        return resp
    resp.say("1.  2.  3.  4.")
    resp.play(song)
    return str(resp)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)
