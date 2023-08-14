from flask import  render_template
from db import  app


# #importar los model en orden
from model.login import validar

from rutas.home import routes_home



# importacion del home
from rutas.validar import routes_validar
app.register_blueprint(routes_validar, url_prefix="/fronted")
app.register_blueprint(routes_home, url_prefix="/fronted")









    
    
@app.route("/")
def index():
    return render_template('/main/index.html')




#esto para que corra el server y ayuda con el puerto
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
    
    
    
    
    
    
    


