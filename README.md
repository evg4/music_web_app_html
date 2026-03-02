# Music web app

This is a basic Flask website which connects with a database to display related album and artist data. The purpose of this was to combine several new learnings, namely Flask, pytest, PostgreSQL database, and HTML templates. <br> It was cloned from the Makers repo as part of my coding bootcamp and contained some starter code; I took a TDD approach to add the tests and working code for the routes and repositories, as well as the HTML.

## How to use (mac)

### Requirements
- Python 3.10+
- PostgreSQL
- Playwright

```bash
# Clone the repository to your local machine
git clone https://github.com/evg4/music_web_app_html.git

# Enter the directory
cd music_web_app_html

# Set up and activate a virtual environment
python -m venv venv
source venv/bin/activate 

# Install dependencies
pip install -r requirements.txt

# Install Playwright
playwright install

# Create a test and development database
createdb music_html
createdb music_html_test

# Seed the development database
python seed_dev_database.py

# Run the tests
pytest 

# Run the app 
python app.py
# Now visit http://localhost:5001/
```

## Areas for improvement
I would love to add CSS to make this look more visually appealing but the focus of this project was getting to grips with Flask and connecting a database, which is why the appearance is basic.

## Credits
Thanks to [Makers](https://github.com/makersacademy) for providing the starter code and guidance during the build.

## Licence
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
 
