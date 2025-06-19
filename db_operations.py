import sqlite3

class database:
    """
    Handles SQLite DB operations for alerts.
    """
    def __init__(self, DB_PATH):
        self.db_path = DB_PATH
        connect = sqlite3.connect(self.db_path)
        conn = connect.cursor()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS alerts (
                frame_id INTEGER,
                timestamp TEXT,
                description TEXT,
                alert TEXT
            )
        ''')
        connect.commit()
        connect.close()



    def save_alert(self, frame_id, timestamp, description, alert):
        """
        Inserts a new alert record into the database.
        """
        connect = sqlite3.connect(self.db_path)
        conn = connect.cursor()
        conn.execute('''
            INSERT INTO alerts (frame_id, timestamp, description, alert)
            VALUES (?, ?, ?, ?)
        ''', (frame_id, timestamp, description, alert))
        connect.commit()
        connect.close()

    def list_alert(self):
        """
        Retrieves all stored alerts from databse.
        """
        connect = sqlite3.connect(self.db_path)
        conn = connect.cursor()
        conn.execute('SELECT * FROM alerts')
        rows = conn.fetchall()
        connect.close()

        alerts = []
        for row in rows:
            alerts.append({
                "frame_id": row[0],
                "timestamp": row[1],
                "description": row[2],
                "alert": row[3],
            })

        return alerts
