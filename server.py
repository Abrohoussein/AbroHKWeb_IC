from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    photo_data = request.form['photo_data']
    
    # Traiter la photo et renvoyer le résultat (par exemple, renvoyer un entier)
    # ...
    
    return 'Résultat du traitement : {}'.format(result)

if __name__ == '__main__':
    app.run(debug=True)
