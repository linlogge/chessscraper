import lichess.api
from lichess.format import SINGLE_PGN
from openpyxl import load_workbook

""" wb = load_workbook(filename = 'players.xlsx') """

""" sheet_ranges = wb['Tabelle1'] """

players = ["mawyien"]

for player in players:
  pgn = lichess.api.user_games(player, format=SINGLE_PGN)
  with open('games/' + player + '.pgn', 'w') as f:
    f.write(pgn)
