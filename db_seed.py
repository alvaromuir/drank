#!flask/bin/python
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from datetime import datetime
import os.path

from app import db
from app.models import User, SocialUser
from app.controllers import utils


import seed_data

seeds = seed_data.USERS


def seed_data():
    try:
        for el in seeds:
            joined_date = utils.randomDate(datetime(2013,01,01), 
                                    datetime(2013,12,05))

            # user accounts
            acct = seeds[el]['account']
            user = User( acct['email'],
                    acct['display_name'], 
                    acct['image_url'])

            user.handle = acct['handle']
            user.status = acct['status']
            user.joined_date = joined_date
            user.last_login = utils.randomDate(joined_date, datetime.utcnow())
            db.session.add(user)
            db.session.commit()

            # social accounts
            social = seeds[el]['social']
            for ntwrk in social:
                sn = social[ntwrk]
                suser = SocialUser(sn['network'],
                                    sn['network_id'],
                                    sn['username'],
                                    sn['network_url'])

                db.session.add(suser)
                suser.user = User.query.filter_by(display_name = acct['display_name']).first()
                db.session.commit()

           print 'DB seeded with development data.'

    except:
            print 'An error has occured.'


seed_data()