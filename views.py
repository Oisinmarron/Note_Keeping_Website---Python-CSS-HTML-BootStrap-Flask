from flask import Blueprint, render_template, request, flash, jsonify
from flask.globals import request
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST']) # Whenever you go to wesite it calls home()
@login_required
def home():
    if request.method == "POST":
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId'] # Access noteId from index.js file
    note = Note.query.get(noteId) # Look for note with that id
    if note: # if exists
        if note.user_id == current_user.id: # And if signed in user owns note
            db.session.delete(note)
            db.session.commit()
    return jsonify({}) # Return empty response