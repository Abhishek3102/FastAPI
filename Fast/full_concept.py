from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import List, Optional
import random
import time

# Basic Setup - Creating a FastAPI app
app = FastAPI()

# Sample data (Simulating a "Database")
players = {}
matches = []

# Models - Pydantic Classes for Validation
class Player(BaseModel):
    id: int
    name: str
    position: str
    nationality: str
    goals_scored: int = 0  # Default value of 0 goals for new players

class Match(BaseModel):
    id: int
    date: str
    opponent: str
    result: str
    goals_for: int
    goals_against: int

# Dependency to simulate a DB fetch, showing how to use dependency injection
def get_player_by_id(player_id: int):
    player = players.get(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

# Route for Home page
@app.get("/")
def read_root():
    return {"message": "Welcome to the Manchester United 'Fergie Era' API!"}

# Route to retrieve all players
@app.get("/players", response_model=List[Player])
def get_players():
    return list(players.values())

# Route to retrieve a specific player by ID (Dependency injection to simulate a database query)
@app.get("/players/{player_id}", response_model=Player)
def get_player(player_id: int, player: Player = Depends(get_player_by_id)):
    return player

# Route to create a new player
@app.post("/players", response_model=Player)
def create_player(player: Player):
    if player.id in players:
        raise HTTPException(status_code=400, detail="Player with this ID already exists")
    players[player.id] = player
    return player

# Route to update an existing player
@app.put("/players/{player_id}", response_model=Player)
def update_player(player_id: int, player: Player, player_db: Player = Depends(get_player_by_id)):
    players[player_id] = player
    return player

# Route to delete a player
@app.delete("/players/{player_id}")
def delete_player(player_id: int, player_db: Player = Depends(get_player_by_id)):
    del players[player_id]
    return {"message": f"Player with ID {player_id} has been deleted."}

# Route to retrieve all matches
@app.get("/matches", response_model=List[Match])
def get_matches():
    return matches

# Route to create a new match (Adding a match with opponent details)
@app.post("/matches", response_model=Match)
def create_match(match: Match):
    matches.append(match)
    return match

# Route to calculate and update player statistics (e.g., goals scored)
@app.put("/players/{player_id}/update-goals")
def update_goals(player_id: int, goals: int, player: Player = Depends(get_player_by_id)):
    player.goals_scored += goals  # Update goals scored
    players[player_id] = player  # Update player in database
    return {"message": f"{player.name}'s goal tally has been updated!"}

# Example of background tasks - Updating match statistics after a match (simulating delay)
def update_match_statistics(match_id: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(simulate_match_result, match_id)
    return {"message": "Match statistics are being updated in the background..."}

def simulate_match_result(match_id: int):
    time.sleep(2)  # Simulating a delay in updating match stats
    # Random result for match simulation
    result = random.choice(["Win", "Loss", "Draw"])
    goals_for = random.randint(0, 5)
    goals_against = random.randint(0, 5)
    matches[match_id].result = result
    matches[match_id].goals_for = goals_for
    matches[match_id].goals_against = goals_against
    print(f"Match {match_id} stats updated: {result} ({goals_for}-{goals_against})")

# Endpoint to simulate a match, and update statistics in the background
@app.post("/matches/{match_id}/simulate")
def simulate_match(match_id: int, background_tasks: BackgroundTasks):
    return update_match_statistics(match_id, background_tasks)
