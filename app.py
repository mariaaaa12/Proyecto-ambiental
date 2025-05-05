from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para almacenar los testimonios
testimonios = [
    {"texto": "Gracias a este proyecto, ahora comprendemos mejor cómo cuidar nuestros ríos y bosques.", "autor": "María, residente de San Pablo"},
    {"texto": "La siembra de árboles fue una experiencia increíble con toda la comunidad unida.", "autor": "Juan, voluntario ambiental"}
]

# Listas temporales

actividades = [
    {'fecha': '15 de marzo 2025', 'descripcion': 'Caminata ecológica por el bosque'},
    {'fecha': '22 de noviembre 2024', 'descripcion': 'Jornada de siembra de árboles'},
    {'fecha': '28 de abril 2025', 'descripcion': 'Taller de reciclaje para niños'},
    {'fecha': '3 de mayo 2025', 'descripcion': 'Limpieza comunitaria del río'}
]


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        texto = request.form.get('texto')
        autor = request.form.get('autor')

        if texto and autor:
            testimonios.append({"texto": texto, "autor": autor})
            return redirect(url_for('home'))

    datos = {
        'dias': ['Lun', 'Mar', 'Mié', 'Jue', 'Vie'],
        'temperaturas': [14, 15, 13, 14.5, 14],
        'humedades': [81, 79, 85, 82, 80]
    }

    return render_template("panel.html",
        datos=datos,
        temperatura=14,
        humedad=81,
        aire='Buena',
        agua='Aceptable',
        testimonios=testimonios,
        actividades=actividades 
    )

@app.route('/agregar_actividad', methods=['POST'])
def agregar_actividad():
    fecha = request.form.get('fecha')
    descripcion = request.form.get('descripcion')

    if fecha and descripcion:
        actividades.append({'fecha': fecha, 'descripcion': descripcion})
    return redirect('/')


@app.route('/actividad1')
def actividad1():
    return render_template('actividad1.html')

@app.route('/actividad2')
def actividad2():
    return render_template('actividad2.html')

@app.route('/actividad3')
def actividad3():
    return render_template('actividad3.html')







if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
