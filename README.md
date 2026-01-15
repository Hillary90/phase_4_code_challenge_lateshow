# LateShow Podcast API

This is a Flask RESTful API for managing podcast episodes, guests, and their appearances on the LateShow. It allows you to view episodes, guests, and add guest appearances with ratings.



## Technologies

- Python 3.12
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite (default)
- sqlalchemy-serializer

---
## Installation & Setup
1. Clone the Repository

```bash
git clone https://github.com/Hillary90/phase_4_code_challenge_lateshow.git
cd phase_4_code_challenge_lateshow/
```
2. Create Virtual Environment

```bash
pipenv install
```

3. Activate virtual environment
```bash
pipenv shell
```

4. Install Dependencies
```bash
pipenv install -r requirements.txt
```


5. Initialize Database
```bash
python seed.py
```

6. Run the Application
```bash
python app.py
```

### The API will be available at: http://localhost:5555

Testing the API

## Deployment
Local Deployment
Follow installation steps above

Run: python run.py

Access at: http://localhost:5555

Production Deployment (Example with Gunicorn)
bash
pipenv install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 run:app
Environment Variables
Create a .env file in the root directory:

env
DATABASE_URL=sqlite:///podcast.db
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
Troubleshooting
Common Issues
"No such table" error


## Contributing
- Fork the repository
- Create a feature branch
- Commit your changes
- Push to the branch
- Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Acknowledgments
- Flask documentation and community
- SQLAlchemy ORM 
- All contributors and testers


