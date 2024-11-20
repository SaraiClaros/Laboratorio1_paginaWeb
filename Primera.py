from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    print("La ruta /index fue accedida")
    return render_template('index.html')  


@app.route('/nosotros')
def about():
    print("La ruta /nosotros fue accedida")
    return render_template('nosotros.html')

if __name__ == '__main__':
    app.run(debug=True)


