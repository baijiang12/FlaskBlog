from flask import Blueprint

#创建一个蓝图
web_blue = Blueprint('web',__name__)

from . import user