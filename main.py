# main.py

from app import app
from app.models import User
from app import db

# Create a shell context
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)