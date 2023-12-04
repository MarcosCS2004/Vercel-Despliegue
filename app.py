from flask import Flask, render_template, flash, request, Response, jsonify, redirect, url_for
from database import app, db, MascotaSchema
from mascotas import Mascota

mascota_schema = MascotaSchema()
mascotas_schema = MascotaSchema(many=True)

@app.route('/')
def home():
    mascotas = Mascota.query.all()
    mascotas_leidas = mascotas_schema.dump(mascotas)
    return render_template('index.html', mascotas=mascotas_leidas)

@app.route('/mascotas', methods=['POST'])
def addMascota():
    nombre = request.form['nombre']
    especie = request.form['especie']
    raza = request.form['raza']
    duenio = request.form['duenio']

    if nombre and especie and raza and duenio:
        nueva_mascota = Mascota(nombre, especie, raza, duenio)
        db.session.add(nueva_mascota)
        db.session.commit()
        flash('Mascota agregada correctamente')
        return redirect(url_for('home'))
    else:
        return notFound()

@app.route('/delete/<id>')
def deleteMascota(id):
    mascota = Mascota.query.get(id)
    db.session.delete(mascota)
    db.session.commit()
    flash(f'Mascota {id} eliminada correctamente')
    return redirect(url_for('home'))

@app.route('/edit/<id>', methods=['POST'])
def editMascota(id):
    nombre = request.form['nombre']
    especie = request.form['especie']
    raza = request.form['raza']
    duenio = request.form['duenio']

    if nombre and especie and raza and duenio:
        mascota = Mascota.query.get(id)
        mascota.nombre = nombre
        mascota.especie = especie
        mascota.raza = raza
        mascota.duenio = duenio
        db.session.commit()
        flash(f'Mascota {id} actualizada correctamente')
        return redirect(url_for('home'))
    else:
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)
