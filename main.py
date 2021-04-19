import lichess.api
from lichess.format import SINGLE_PGN

pl = "mawyien"
max = 200

pgn = lichess.api.user_games(pl, max=max, format=SINGLE_PGN)
with open('last200.pgn', 'w') as f:
  f.write(pgn)
