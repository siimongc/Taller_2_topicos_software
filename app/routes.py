from flask import Blueprint, jsonify, render_template
from app.pokeneas import pokeneas
from app.utils import get_container_id
import random

routes = Blueprint('routes', __name__)

@routes.route('/pokenea')
def get_pokenea_json():
    p = random.choice(pokeneas)
    return jsonify({
        "id": p["id"],
        "nombre": p["nombre"],
        "altura": p["altura"],
        "habilidad": p["habilidad"],
        "container_id": get_container_id()
    })

@routes.route('/filosofia')
def get_filosofia():
    p = random.choice(pokeneas)
    return render_template('filosofia.html', pokenea=p, container_id=get_container_id())
