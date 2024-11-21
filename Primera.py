from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'clave_secreta'

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/matematica', methods=['GET'])
def matematica():
    return render_template('retos_matematicas.html')

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        telefono = request.form['telefono']
        curso = request.form['curso']

        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            cursor.execute("INSERT INTO Estudiantes (nombre, correo, telefono, curso) VALUES (?, ?, ?, ?)", 
                           (nombre, correo, telefono, curso))
            conn.commit()
            flash('¡Estudiante registrado exitosamente!', 'success')
        except Exception as e:
            flash(f'Error al guardar los datos: {e}', 'error')
        finally:
            conn.close()

        return redirect(url_for('formulario'))

    return render_template('form.html')

@app.route('/formulario_do', methods=['GET', 'POST'])
def formulario_do():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        telefono = request.form['telefono']
        especialidad = request.form['especialidad']

        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            cursor.execute("INSERT INTO Docentes (nombre, correo, telefono, especialidad) VALUES (?, ?, ?, ?)", 
                           (nombre, correo, telefono, especialidad))
            conn.commit()
            flash('¡Docente registrado exitosamente!', 'success')
        except Exception as e:
            flash(f'Error al guardar los datos: {e}', 'error')
        finally:
            conn.close()

        return redirect(url_for('formulario_do'))

    return render_template('formsma.html')

@app.route('/nosotros', methods=['GET'])
def about():
    return render_template('nosotros.html')

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL,
            telefono TEXT NOT NULL,
            curso TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Docentes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL,
            telefono TEXT NOT NULL,
            especialidad TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
