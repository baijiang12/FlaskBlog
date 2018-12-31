from flask import Flask
from app.web import web_blue


def create_app():
    theapp = Flask(__name__)
    # 注册蓝图web_blue
    theapp.register_blueprint(web_blue)

    return theapp