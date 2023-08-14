from db import db, app, ma
from flask import Blueprint, request 
# from model.login import pacientes
from model.login import validar



routes_validar = Blueprint("routes_validar", __name__)



# @routes_validar.route('/guardar_usuario', methods=['POST']) 
# def guardar_usuario():
#     usuario = request.form['usuario']
#     Email = request.form['Correo']
#     contraseña = request.form['contraseña']
#     sexo = request.form['sexo']
#     fecha_nacimiento = request.form['fecha']

#     # Check if the patient already exists in the database
#     existing_patient = validar.query.filter(
#         (validar.usuario == usuario) | (validar.Email == Email)
#     ).first()
#     if existing_patient:
#         return "Paciente already exists in the database"

#     new_reg = validar( usuario, Email,contraseña,sexo, fecha_nacimiento)
#     db.session.add(new_reg)
#     db.session.commit()
#     return "Record saved successfully" 


@routes_validar.route('/validar', methods=['POST'])
def validar_login():
    usuarios = request.json["usuario"]
    contraseña = request.json["contraseña"]
   

    verificacion = db.session.query(validar).filter(validar.correo == usuarios, validar.clave == contraseña).first()

    print(verificacion)

    if verificacion:
            return {"status": "Correcto", "message": "Inicio de sesión exitoso"}
    else:
        return {"status": "Error", "message": "Credenciales incorrectas"}

  

 

      
                

           


    

