import os
import berserk
from datetime import datetime

API_TOKEN = os.environ.get('lichess_API_KEY')

session = berserk.TokenSession(API_TOKEN)
client = berserk.Client(session=session)

start = berserk.utils.to_millis(datetime(2023, 12, 8))
end = berserk.utils.to_millis(datetime(2024, 12, 9))
print(start, end)

try:
    games = client.games.export_by_player('blissnull', since=start, until=end, max=2)
    print("api_token", API_TOKEN)
    for game in games:
        print(game)
except berserk.exceptions.ResponseError as e:
    print("HTTP Error:", e)
