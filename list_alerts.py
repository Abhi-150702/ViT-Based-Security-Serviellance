import os
from db_operations import database

DB_PATH = 'alerts.db'

db = database(DB_PATH)

alerts = db.list_alert()

for alert in alerts:
    print(alert)