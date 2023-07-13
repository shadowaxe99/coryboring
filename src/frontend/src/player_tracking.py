import requests
import sqlite3

def retrieve_game_data(game_id):
    api_key = 'YOUR_API_KEY'
    url = f'https://api.example.com/games/{game_id}/stats?api_key={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        game_data = response.json()
        return game_data
    else:
        return None

def extract_player_stats(game_data, player_id):
    player_stats = {}
    
    for player in game_data['players']:
        if player['id'] == player_id:
            player_stats['points'] = player['stats']['points']
            player_stats['rebounds'] = player['stats']['rebounds']
            # Extract other relevant statistics
            
    return player_stats

def update_player_performance(player_id, player_stats):
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    
    # Assuming you have a 'players' table with columns 'id', 'points', 'rebounds', etc.
    update_query = f"UPDATE players SET points = {player_stats['points']}, rebounds = {player_stats['rebounds']} WHERE id = {player_id}"
    cursor.execute(update_query)
    
    conn.commit()
    conn.close()

# Example usage

# Retrieve real-time game data
game_data = retrieve_game_data(123)

# Extract player stats
player_stats = extract_player_stats(game_data, 456)

# Update player performance in the database
update_player_performance(456, player_stats)