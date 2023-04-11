"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from datetime import datetime
from app.models import Movie
from app import app, db
from flask import redirect, render_template, request, jsonify, send_file, send_from_directory
from werkzeug.utils import secure_filename
from app.forms import MovieForm
import os
from flask_wtf.csrf import generate_csrf

###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


@app.route('/api/v1/movies', methods=['POST'])
def movies():
    form = MovieForm(request.form)

    if request.method == "POST" and form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        poster = request.files['poster']
        created_at = datetime.now()
        postername = secure_filename(poster.filename)
        
        
        poster.save(os.path.join(app.config['UPLOAD_FOLDER'], postername))


        # add the movie to database
        movie = Movie(title=title, description=description, poster=postername, created_at=created_at)
        db.session.add(movie)
        db.session.commit()



        # return a JSON response with the movie data
        response_data = {
            "message": "Movie Successfully added",
            "title": title,
            "poster": postername,
            "description": description
        }
        return jsonify(response_data)

    else:
        # return a JSON response with the form errors
        errors = form_errors(form)
        response_data = {
            "response": errors
        }
        return jsonify(response_data)



@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})


@app.route('/api/v1/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify({
        'movies': [{
            'id': movie.id,
            'title': movie.title,
            'description': movie.description,
            'poster': f'/posters/{movie.poster}'
        } for movie in movies]
    })



@app.route('/posters/<filename>', methods=['GET'])
def get_poster(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)



###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404