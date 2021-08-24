# Web app that shows current time in Los Angeles (America)

from flask import Flask
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)


@app.route('/')


def hello_world():
    la_timezone = ZoneInfo('America/Los_Angeles')
    return datetime.now(tz = la_timezone).time().__str__()

# Use if __name__ == '__main__' (explained in Python best practices file)
if __name__ == '__main__':
    app.run()