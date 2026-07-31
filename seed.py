import random

from faker import Faker

from app import app
from models import JournalEntry, User, db

fake = Faker()


with app.app_context():
    db.drop_all()
    db.create_all()

    users = []

    for _ in range(10):

        user = User(
            username=fake.user_name(),
            email=fake.unique.email()
        )

        user.password = "password123"

        users.append(user)

    db.session.add_all(users)
    db.session.commit()

    entries = []

    for _ in range(50):
        entry = JournalEntry(
            title=fake.sentence(nb_words=5),
            content=fake.paragraph(nb_sentences=5),
            user_id=random.choice(users).id
        )

        entries.append(entry)

    db.session.add_all(entries)
    db.session.commit()

    print("Database seeded successfully!")