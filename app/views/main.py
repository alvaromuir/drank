from flask import flash, render_template

from app.controllers import utils, users
from app.controllers.auth import twitter, github, linkedin

import forms


def index(user):
    date = utils.get_date()
    return render_template('index.html',
                            user = user,
                            current_date = date)


def oauth_req(network):
    if network == 'twitter':
        return twitter.auth_url()
        
    if network == 'github':
        return github.auth_url()

    if network == 'linkedin':
        return linkedin.auth_url()


def get_profile_by_id(user_id):
    if(users.get_user(user_id) != None):
        user = users.get_user(user_id)
        social_info = users.get_user_socialinfo(user)
        form = forms.Profile()
        return render_template('profile.html', 
                                user = user, 
                                user_social_info = social_info,
                                form = form)
    else:
        return render_template('404.html')

def get_profiles():
    return render_template('profiles_list.html', profiles = users.get_users())


def get_profile_by_handle(handle):
    if(users.get_user_by_handle(handle) != None):
        user = users.get_user_by_handle(handle)
        social_info = users.get_user_socialinfo(user)

        form = users.gen_profle_form(user)
        return render_template('profile.html', 
                                user = user, 
                                user_social_info = social_info,
                                form = form)
    else:
        return render_template('404.html')


def internal_error(error):
    if(error.code == 404):
        return render_template('404.html')

    if(error.code == 500):
        return users.internal_error()