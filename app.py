from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/sobre-mim')
def sobre_mim():
    return render_template('sobre-mim.html')

@app.route('/download_curriculo')
def download_curriculo():
    return send_from_directory(directory='static', filename='Curriculum_GiovannaLASouza.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
