from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        telefono = request.form['telefono']
        curso = request.form['curso']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO Estudiantes (nombre, correo, telefono, curso) VALUES (?, ?, ?, ?)", 
                       (nombre, correo, telefono, curso))
        conn.commit()
        conn.close()

        print("Datos guardados en la tabla Estudiantes")
        return redirect(url_for('formulario'))  

    return render_template('form.html')

@app.route('/formulario_do', methods=['GET', 'POST'])
def formulario_do():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        telefono = request.form['telefono']
        especialidad = request.form['especialidad']

        # Mostrar los datos recibidos para depuración
        print("Datos del docente recibidos:", nombre, correo, telefono, especialidad)

        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()

            # Inserción en la tabla Docentes
            cursor.execute("INSERT INTO Docentes (nombre, correo, telefono, especialidad) VALUES (?, ?, ?, ?)", 
                           (nombre, correo, telefono, especialidad))
            conn.commit()
            print("Datos del docente guardados correctamente.")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")
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

    # Crear tabla de Estudiantes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL,
            telefono TEXT NOT NULL,
            curso TEXT NOT NULL
        )
    ''')

    # Crear tabla de Docentes
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
