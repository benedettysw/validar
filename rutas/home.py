from db import db , ma , app
from flask import Blueprint , render_template 

routes_home = Blueprint("routes_home",__name__)


@routes_home.route("/segunda" , methods=["GET"])
def index2():
    return render_template('/main/index2.html')