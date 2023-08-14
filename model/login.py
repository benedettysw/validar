from db import db, app, ma 



class validar(db.Model):
    __tablename__ = "login"
    
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(111))
    clave = db.Column(db.String(111))
    
    def __init__(self, correo, clave):
        self.correo = correo
        self.clave = clave
      
    
with app.app_context():
    db.create_all()