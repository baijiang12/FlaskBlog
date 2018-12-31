from . import web_blue

@web_blue.route('/index')
def index():
    return 'this is index'
