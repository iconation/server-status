from flask import render_template
from app import app
from app import constants

from app.models import server_status as model
from app.views import server_status as view

@app.route('/')
@app.route('/index')
def index():

    servers = []
    servers.append (view.status (model.status ("http://iconation.team:9100", "https://ctz.solidwallet.io"), "ICONation Mainnet Citizen Node"))
    servers.append (view.status (model.status ("http://iconation.team:9000", "https://test-ctz.solidwallet.io"), "ICONation Testnet Citizen Node"))
    # servers.append (view.status (model.status ("http://35.181.101.42:9000", "https://preptest.net.solidwallet.io"), "ICONation Testnet P-Rep Node"))

    return render_template ('index.html', constants=constants, servers=servers)
