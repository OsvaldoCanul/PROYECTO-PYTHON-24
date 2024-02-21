from flask import Flask, render_template #Es para importar flask

app = Flask(__name__) 

@app.route('/')
def Hola(): 
    return '<h1>Bienvenido al sitio Web de Osvaldo Ignacio Canul Cauich</h1>' 
@app.route('/plantilla')
def plantilla():
    data={
        'titulo':'Página plantilla',
        'mensaje':'Hola'
    } 
    return render_template('pagina1.html',data=data) 
app.run(debug=True) 