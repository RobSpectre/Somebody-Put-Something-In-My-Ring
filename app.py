import os
from flask import Flask
from flask import request
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
        g.say("For I Wanna Be Your Boyfriend, press 4.")
    resp.pause(length="3")
    resp.redirect("/voice")
    return str(resp)


@app.route('/play', methods=['POST'])
def play():
    if request.form['Input'] == '1':
        song = "/music/the_kkk_took_my_baby_away.mp3"
    elif request.form['Input'] == '2':
        song = "/music/blitzkrieg_bop.mp3"
    elif request.form['Input'] == '3':
        song = "/music/sheena_is_a_punk_rocker.mp3"
    elif request.form['Input'] == '4':
        song = "/music/i_wanna_be_your_boyfriend.mp3"
    else:
        resp.say("I'm sorry - I did not understand your request.")
        resp.redirect("/voice")
        return resp
    resp.say("1.  2.  3.  4.")
    resp.play(song)
    return str(resp)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)
