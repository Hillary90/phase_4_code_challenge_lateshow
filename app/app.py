from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Episode, Guest, Appearance

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///podcast.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def index():
    return {"message": "flask app running"}

@app.route("/episodes")
def get_episodes():
    return jsonify([episode.to_dict() for episode in Episode.query.all()])

@app.route("/episodes/<int:id>")
def get_episode(id):
    episode = Episode.query.get(id)
    if episode:
        return jsonify(episode.to_dict())
    return jsonify({"error": "Episode not found"}), 404

@app.route("/guests")
def get_guests():
    return jsonify([guest.to_dict() for guest in Guest.query.all()])

@app.route("/guests/<int:id>")
def get_guest(id):
    guest = Guest.query.get(id)
    if guest:
        return jsonify(guest.to_dict())
    return jsonify({"error": "Guest not found"}), 404

@app.route("/appearances", methods=["POST"])
def create_appearance():
    data = request.get_json()

    appearance = Appearance(
        rating=data["rating"],
        episode_id=data["episode_id"],
        guest_id=data["guest_id"]
    )

    db.session.add(appearance)
    db.session.commit()

    return jsonify(appearance.to_dict()), 201

@app.route("/episode/<int:id>", methods=["DELETE"])
def delete_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    db.session.delete(episode)
    db.session.commit()

    return jsonify({"message": "Episode deleted successfully"}), 200



if __name__ == "__main__":
    app.run(port=5555, debug=True)