# WebRanking
The Elo rating system is a way of calculating the level of skill of a player in games such as chess. The Elo rating of a player takes the form of a number that is recalculated every time that player plays a match against another Elo ranked player. After a match the winning player's takes rating points from the losing player, with the amount of points taken determined by the difference between the two players' rating before the match. (see https://en.wikipedia.org/wiki/Elo_rating_system)

The interface supports the following functionality:
1. Recalculate and store the Elo rating of players by entering the results of a single match.
2. Retrieve a summary of current players and their ranking in the league based on their Elo rating.

This Django project was developed using PyCharm with python 3.6.5 , other dependencies include:
1. Requests
2. Certifi
3. Chardet
4. Idna
5. Pytz

To test the project you will need to have python 3 and preferably PyCharm (it has db.sqlite by default) installed and then:
1. Clone the project
2. Install any dependencies(File->Settings->Project:WebRanking->Project Interpreter)
3. Run python manage.py migrate
4. Run python manage.py createsuperuser
5. Run python manage.py migrate rankings
6. Run project and then open localhost to view the app


