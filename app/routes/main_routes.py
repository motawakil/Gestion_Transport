# routes/main_routes.py
from flask import Blueprint, render_template
from utils.utils import login_required  # Import the custom login_required decorator

# Create the Blueprint for the main routes
main_bp = Blueprint('main', __name__)

# Define main routes here
@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/about')

def about():
    return render_template('about.html')

@main_bp.route('/feedback')

def feedback():
    return render_template('feedback.html')


@main_bp.route('/rapport')

def rapport():
    return render_template('rapport.html')

@main_bp.route('/reservation')

def reservation():
    return render_template('reservation.html')

@main_bp.route('/suivi_vehicule')

def visualization():
    return render_template('suivi_vehicule.html')

@main_bp.route('/vehicule')
def vehicule():
    return render_template('vehicule.html')

# account setting + employes 

@main_bp.route('/account')
def account():
    return render_template('account.html')

@main_bp.route('/employes')
def employes():
    return render_template('employe.html')


@main_bp.route('/chauffeur')
def chauffeur():
    return render_template('chauffeur.html')