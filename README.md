# SQLite Docker Setup

This repository contains a Docker setup for running SQLite with persistent storage.

## Usage

### Build and run with Docker Compose

```bash
docker-compose up -d
```

### Connect to the SQLite container

```bash
docker exec -it sqlite-container sh
```

### Access the SQLite database

Once inside the container:

```bash
sqlite3 /data/sqlite/database.db
```

### Connect from Python

Create a Python script (`connect.py`) with the following content:

```python
import sqlite3

# Connect to the SQLite database in the mounted volume
conn = sqlite3.connect('/path/to/mounted/volume/database.db')
cursor = conn.cursor()

# Example: Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE
)
''')

# Example: Insert data
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
               ("John Doe", "john@example.com"))

# Commit changes and close
conn.commit()
conn.close()
```

Replace `/path/to/mounted/volume/database.db` with the actual path where the Docker volume is mounted on your host system.

