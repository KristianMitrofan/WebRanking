# WebRanking
The Elo rating system is a way of calculating the level of skill of a player in games such as chess. 
The Elo rating of a player takes the form of a number that is recalculated every time that player plays a 
match against another Elo ranked player. After a match the winning player's takes rating points from the 
losing player, with the amount of points taken determined by the difference between the two players' rating 
before the match. (see https://en.wikipedia.org/wiki/Elo_rating_system)

I migrated the database with the current top players by scraping https://www.prochessleague.com/players.html

The interface supports the following functionality:
1. Recalculate and store the Elo rating of players by entering the results of a single match.
2. Retrieve a summary of current players and their ranking in the league based on their Elo rating.

Instructions to run the project:
1. Clone the project from github (git clone https://github.com/ChristianMitrofan/WebRanking.git)
2. Create a virtual environment (virtualenv env --no-site-packages) in the project's folder
3. Start the virtual environment (Linux:source env/bin/activate Windows:venv\Scripts\activate.bat)
4. Install requirements (pip install -r requirements.txt)
5. Create a file named "secrets.sh" (Linux:touch secrets.sh Windows:type nul>secrets.sh)
6. Obtain a secret from MiniWebTool key and add export SECRET_KEY='<secret_key>' to secrets.sh 
7. Create a postgres db and add the credentials to settings.py
   
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'NAME': 'db_name',
           'USER': 'name',
           'PASSWORD': '',
           'HOST': 'localhost',
           'PORT': '',
       }
   }
   
8. Migrate the database (python manage.py migrate)
9. And finally to start the development server
               
               python manage.py runserver
               
    and open localhost:8000 on your browser to view the app.


