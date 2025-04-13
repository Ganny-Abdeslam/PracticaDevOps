from flask import request, jsonify
from . import db
from .models import Patient
from flask import current_app as app

@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    new_patient = Patient(name=data['name'], email=data['email'])
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({'message': 'Patient added successfully'})
