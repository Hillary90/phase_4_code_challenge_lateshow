from app import app
from models import db, Episode, Guest, Appearance

with app.app_context():
    db.drop_all()
    db.create_all()

    ep1 = Episode(date="1/11/99", number=1)
    ep2 = Episode(date="1/12/99", number=2)

    db.session.add_all([ep1, ep2])
    db.session.commit()

    guest1 = Guest(name="Michael J. Fox", occupation="actor")
    guest2 = Guest(name="Sandra Bernhard", occupation="Comedian")
    guest3 = Guest(name="Tracey Ullman", occupation="television actress")

    db.session.add_all([guest1, guest2, guest3])
    db.session.commit()

    app1 = Appearance(rating=4, episode_id=1, guest_id=1)
    app2 = Appearance(rating=5, episode_id=2, guest_id=3)

    db.session.add_all([app1, app2])
    db.session.commit()
