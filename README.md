# Somebody Put Something In My Ring

My colleague Michael Selvidge made a service called [Callin'
Oates](http://www.callinoates.com).
[It](http://newsfeed.time.com/2011/12/23/callin-oates-for-when-the-hall-oates-urge-strikes/)
[became](http://techcrunch.com/2011/12/29/600000-calls-later-callin-oates-developers-share-their-code/)
[pretty](http://www.tmz.com/2011/12/25/hall-and-oates-callin-oates/?adid=recentlyupdatedstories#.TwNuXkTT3hs)
[popular](http://espn.go.com/blog/los-angeles/lakers/post/_/id/25033/podkast-wbeto-duran-kobes-wrist-wing-depth-and-hall-and-oates).

I ported his code to Python, but something happened in the translation.


## Usage

Call this number - (646)606-2607.

Or go to the [website](http://www.somethinginmyring.com).


## Hacking

### Installation

Requires Python 2.5 or greater.

1) Clone repo:

<pre>
git clone git@github.com:RobSpectre/Somebody-Put-Something-In-My-Ring.git
</pre>

2) Install dependencies:

<pre>
cd Somebody-Put-Something-In-My-Ring
pip install -r requirements.txt
</pre>

3) Login to [Twilio](https://www.twilio.com/login) (or [signup for
account](https://www.twilio.com/try-twilio?g=)).

4) [Create new TwiML App](https://www.twilio.com/user/account/apps/add) for Somebody Put Something In My Ring.

5) Configure local_settings.py with your Twilio account details or use
environment variables.

<pre>
export ACCOUNT_SID='ACxxxxxxxxxxxxxxxxx'
export AUTH_TOKEN='yyyyyyyyyyyyyyyyyyyy'
export RAMONES_APP_SID='APzzzzzzzzzzzzz'
export RAMONES_CALLER_ID='+17778889999'
</pre>

6) Launch dev server.

<pre>
python web.py
</pre>

Note - a Procfile is included if you would prefer to use Foreman.

### Structure

* app.py - Core Flask app.
* templates/index.html - Main webpage with [Twilio Client](http://www.twilio.com/api/client) integration.
* static/ - Root of all static files, including JS and CSS.

### Deployment

This app is currently running on [Heroku](http://www.heroku.com), but can be
deployed to any WSGI compliant hosting provider.  If it runs Python, it should
be able to run this project.

### Testing

Use nose or simply run from root:

<pre>
python tests
</pre>


## Technologies

* [Flask](http://flask.pocoo.org/) - Python microframework.  Makes all this go.
* [Skeleton](http://www.getskeleton.com) - Easy CSS framework for responsive design (resize the browser window and marvel!)
* [Heroku](http://www.heroku.com) - Uber easy cloud hosting for Python (and lesser) apps.
* [Twilio](http://www.twilio.com), of course.


## Credits

* License: [Mozilla Public License](http://www.mozilla.org/MPL/)
* Author: [Rob Spectre](http://www.brooklynhacker.com)
* Inspiration: [Michael Selvidge](http://www.twitter.com/selviano) and [Reid Butler](http://www.twitter.com/rbutlersf)'s [Callin' Oates](http://www.callinoates.com)
* Powered by [Twilio](http://www.twilio.com).

[![githalytics.com
alpha](https://cruel-carlota.pagodabox.com/ac8f215760eead42d1b456d5b419d0fe
"githalytics.com")](http://githalytics.com/RobSpectre/Somebody-Put-Something-In-My-Ring)
