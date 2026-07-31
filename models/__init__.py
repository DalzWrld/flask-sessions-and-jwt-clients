from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .journal_entry import JournalEntry