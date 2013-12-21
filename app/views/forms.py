from flask.ext.wtf import Form
from wtforms import TextField, HiddenField
from wtforms.validators import Required

class Welcome(Form):
    network         = HiddenField('network')
    name            = HiddenField('name')
    username        = HiddenField('username')
    profile_image   = HiddenField('profile_image')
    network_url     = HiddenField('network_url')
    network_id      = HiddenField('network_id')
    email           = TextField('email', validators = [Required()])

class Profile(Form):
    user_id         = HiddenField('id')
    handle          = TextField('handle', validators = [Required()])
    display_name    = TextField('display_name', validators = [Required()])
    email           = TextField('email', validators = [Required()])
    status          = TextField('status')
