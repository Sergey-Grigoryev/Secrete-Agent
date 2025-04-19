import json
import os
import random

# Dynamically construct the absolute path to game_state.json
GAME_STATE_FILE = os.path.join(
    os.path.dirname(__file__), "game_state.json"
)
COUNTIRES_FILE = os.path.join(
    os.path.dirname(__file__), "countries.json"
)


def load_game_state():
    try:
        with open(GAME_STATE_FILE, "r", encoding="utf-8") as file:
            game_state = json.load(file)

        # Randomly select a country from the countries_list
        if "countries_list" in game_state and game_state["countries_list"]:
            selected_country = random.choice(game_state["countries_list"])
            # Set the selected country's details in current_mission
            game_state["current_mission"]["target_country"] = selected_country["country"]
            game_state["current_mission"]["lat_long"] = (
                selected_country["latitude"],
                selected_country["longitude"]
            )
            game_state["current_mission"]["message_to_decrypt"] = selected_country["translation"]

        return game_state
    except FileNotFoundError:
        return {"current_mission": {}}
    except json.JSONDecodeError:
        return {"current_mission": {}}


def save_game_state(state):
    with open(GAME_STATE_FILE, "w") as file:
        json.dump(state, file, indent=4)
