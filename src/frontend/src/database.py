import sqlite3

# Create a connection to the database
conn = sqlite3.connect('sports_agent.db')
c = conn.cursor()

# Create tables for players, teams, games, and statistics
c.execute('''
    CREATE TABLE IF NOT EXISTS players (
        player_id INTEGER PRIMARY KEY,
        name TEXT,
        position TEXT,
        team_id INTEGER,
        FOREIGN KEY (team_id) REFERENCES teams(team_id)
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS teams (
        team_id INTEGER PRIMARY KEY,
        name TEXT,
        league TEXT
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS games (
        game_id INTEGER PRIMARY KEY,
        date TEXT,
        home_team_id INTEGER,
        away_team_id INTEGER,
        FOREIGN KEY (home_team_id) REFERENCES teams(team_id),
        FOREIGN KEY (away_team_id) REFERENCES teams(team_id)
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS statistics (
        stat_id INTEGER PRIMARY KEY,
        player_id INTEGER,
        game_id INTEGER,
        points INTEGER,
        rebounds INTEGER,
        assists INTEGER,
        FOREIGN KEY (player_id) REFERENCES players(player_id),
        FOREIGN KEY (game_id) REFERENCES games(game_id)
    )
''')

# Function to insert player data into the database
def insert_player(player_id, name, position, team_id):
    c.execute("INSERT INTO players (player_id, name, position, team_id) VALUES (?, ?, ?, ?)", (player_id, name, position, team_id))
    conn.commit()

# Function to insert team data into the database
def insert_team(team_id, name, league):
    c.execute("INSERT INTO teams (team_id, name, league) VALUES (?, ?, ?)", (team_id, name, league))
    conn.commit()

# Function to insert game data into the database
def insert_game(game_id, date, home_team_id, away_team_id):
    c.execute("INSERT INTO games (game_id, date, home_team_id, away_team_id) VALUES (?, ?, ?, ?)", (game_id, date, home_team_id, away_team_id))
    conn.commit()

# Function to insert statistics data into the database
def insert_statistics(stat_id, player_id, game_id, points, rebounds, assists):
    c.execute("INSERT INTO statistics (stat_id, player_id, game_id, points, rebounds, assists) VALUES (?, ?, ?, ?, ?, ?)", (stat_id, player_id, game_id, points, rebounds, assists))
    conn.commit()

# Function to retrieve player data from the database
def get_player(player_id):
    c.execute("SELECT * FROM players WHERE player_id = ?", (player_id,))
    return c.fetchone()

# Function to retrieve team data from the database
def get_team(team_id):
    c.execute("SELECT * FROM teams WHERE team_id = ?", (team_id,))
    return c.fetchone()

# Function to retrieve game data from the database
def get_game(game_id):
    c.execute("SELECT * FROM games WHERE game_id = ?", (game_id,))
    return c.fetchone()

# Function to retrieve statistics data from the database
def get_statistics(stat_id):
    c.execute("SELECT * FROM statistics WHERE stat_id = ?", (stat_id,))
    return c.fetchone()

# Function to update player data in the database
def update_player(player_id, name, position, team_id):
    c.execute("UPDATE players SET name = ?, position = ?, team_id = ? WHERE player_id = ?", (name, position, team_id, player_id))
    conn.commit()

# Function to update team data in the database
def update_team(team_id, name, league):
    c.execute("UPDATE teams SET name = ?, league = ? WHERE team_id = ?", (name, league, team_id))
    conn.commit()

# Function to update game data in the database
def update_game(game_id, date, home_team_id, away_team_id):
    c.execute("UPDATE games SET date = ?, home_team_id = ?, away_team_id = ? WHERE game_id = ?", (date, home_team_id, away_team_id, game_id))
    conn.commit()

# Function to update statistics data in the database
def update_statistics(stat_id, player_id, game_id, points, rebounds, assists):
    c.execute("UPDATE statistics SET player_id = ?, game_id = ?, points = ?, rebounds = ?, assists = ? WHERE stat_id = ?", (player_id, game_id, points, rebounds, assists, stat_id))
    conn.commit()

# Function to delete player data from the database
def delete_player(player_id):
    c.execute("DELETE FROM players WHERE player_id = ?", (player_id,))
    conn.commit()

# Function to delete team data from the database
def delete_team(team_id):
    c.execute("DELETE FROM teams WHERE team_id = ?", (team_id,))
    conn.commit()

# Function to delete game data from the database
def delete_game(game_id):
    c.execute("DELETE FROM games WHERE game_id = ?", (game_id,))
    conn.commit()

# Function to delete statistics data from the database
def delete_statistics(stat_id):
    c.execute("DELETE FROM statistics WHERE stat_id = ?", (stat_id,))
    conn.commit()

# Close the database connection
conn.close()