from flask import Blueprint, render_template

form_route = Blueprint('form_route', __name__, template_folder='../templates')

@form_route.route('/') 
def form_page():
    return render_template('index.html')