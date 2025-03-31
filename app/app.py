from flask import Flask

app = Flask(__name__)

@app.route('/hola')
def hola_mudno():
    return '<h1>Hola </h1>'

@app.route('/add_contac')
def add_contac():
    return '<h1>Add contac</h1>'

@app.route('/edit_contac')
def edit_contac():
    return '<h1>Edit contac</h1>'

@app.route('/delete_contac')
def delete_contac():
    return '<h1>Delete contac</h1>'

if __name__ == '__main__':
    app.run(debug=True , port=5001)
