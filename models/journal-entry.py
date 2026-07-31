from datetime import datetime

from . import db

class JournalEntry(db.Model):
    __tablename__ = "journal_entries"