from flask import g, redirect, request, session
from flask.ext.login import current_user

from app import app, db, lm
from app.models import User
from app.views import forms, main
from app.controllers import users, utils

from datetime import datetime

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated():
        g.user.last_login = datetime.utcnow()
        db.session.add(g.user)
        db.session.commit()


@app.route('/')
@app.route('/index')
def index():
    return main.index(g.user)


@app.route('/login/<social_network>')
def get_login(social_network):
    oauth_req = main.oauth_req(social_network)
    try:
        session['state'] = oauth_req['state']
    except:
        pass
    return redirect(oauth_req['url'])


@app.route('/auth/<social_network>', methods = ['GET', 'POST'])
def get_auth_req(social_network):
    form = forms.Welcome()
    if form.validate_on_submit():
        return users.complete_user_setup(request.values)
    return users.get_or_create_login(social_network)


@app.route('/users/<int:id>')
def get_profile_by_id(id):
    return main.get_profile_by_id(id)


@app.route('/profiles')
def get_profiles():
    return main.get_profiles()


@app.route('/profiles/<handle>', methods = ['GET', 'POST'])
def get_profile_by_handle(handle):
    form = forms.Profile()
    if form.validate_on_submit():
        return users.update_profile(request.values)
    return main.get_profile_by_handle(handle)


@app.route('/logout')
def logout():
    return users.logout()


@app.errorhandler(404)
def internal_error(error):
    return main.internal_error(error)


@app.errorhandler(500)
def internal_error(error):
    return main.internal_error(error)