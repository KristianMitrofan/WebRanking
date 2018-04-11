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
6. urllib3

The easiest way to test this project is by installing the latest edition of python 3 and PyCharm Professional:
1. Clone the repository
2. Open the project with Pycharm
3. Run the project and go to localhost to view it


