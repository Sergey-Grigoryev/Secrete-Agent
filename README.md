# Secret Agents

"Secret Agents" is a web-based text game where players solve spy missions and puzzles through a chat interface. The game leverages an LLM (Language Learning Model) to manage user inputs, invoke relevant tools, and provide context-aware responses. The project is divided into two phases:

1. **The Quartermaster**: A tool-using agent.
2. **The Taskmaster**: A game-manager agent.

## Features

- **Interactive Chat Interface**: Players interact with the game through a web-based chat interface.
- **Tool Integration**: Tools like weather lookup, decryption, translation, and more are available to assist players in completing missions.
- **LLM Orchestration**: The LLM acts as the central controller, determining actions and providing responses based on user input.
- **Mission-Based Gameplay**: Players complete spy missions involving tasks like traveling to locations, decoding messages, and more.

---

## Project Structure

```plaintext
Secrete-Agent/
├── [mission_log.json](http://_vscodecontentref_/0)          # Log of interactions
├── [secret_agents.ipynb](http://_vscodecontentref_/1)       # Jupyter Notebook with project overview and setup
├── src/
│   ├── app.py                # Main Flask application
│   ├── [mission_log.json](http://_vscodecontentref_/2)      # Log of interactions (used by the app)
│   ├── requirements.txt      # Dependencies
│   ├── templates/            # HTML templates (chat interface)
│   ├── gadgets/              # Tools for APIs and non-LLM tasks
│   │   ├── decryptor.py      # Decryption tool
│   │   ├── lat_long_lookup.py# Latitude/Longitude lookup tool
│   │   ├── translate.py      # Translation tool
│   │   ├── weather.py        # Weather lookup tool
│   └── utils/                # Utility functions
│       ├── game_state.py     # Game state management
│       ├── mission_log.py    # Mission log utilities
│       ├── tool_executor.py  # Tool execution logic
│   └── llm/                  # LLM interaction logic
│       ├── llm_interface.py  # Manages communication with the LLM
```
