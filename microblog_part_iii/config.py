# Flask extension configuration file

# Setting 'WTF_CSRF_ENABLED' True activates the cross-site request forgery
# prevention
WTF_CSRF_ENABLED = True

# The 'SECRET_KEY' key is only needed when CSRF is enabled
SECRET_KEY = 'grosse-limace'

# Just to illustrate a point
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]
