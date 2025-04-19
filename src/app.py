from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from llm.llm_interface import send_to_llm
from utils.tool_executor import execute_tool
from utils.mission_log import load_mission_log, save_mission_log
from utils.game_state import load_game_state, save_game_state

app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


GAME_STATE = load_game_state()
print("Game state loaded:", GAME_STATE["current_mission"])
print("Tasks to complete:", GAME_STATE["tasks"])
first_message = True
context = f"""
The user is a secret agent, you are the agent's handler. They are on a mission to gather information and complete tasks: {GAME_STATE["tasks"]}.
The user can ask for help with various tools. If a tool is required, the user should specify the tool and its parameters.
The available tools are:
1. lat_long_lookup: Get the country name from latitude and longitude.
2. decrypt: Decrypt a message using a specific decryption method.
3. translate: Translate a message to English.
Keep the conversation focused on the mission and avoid unnecessary details. Respond with clear and actionable information.
"""


@socketio.on("message")
def handle_message(message):
    global first_message
    global context
    # Step 1: Log or validate the incoming message
    if first_message:
        # Log the first message
        print("First message received.")
        print(f"Received message: {message}")
        first_message = False
        # Step 2: Send the message to the LLM
        llm_response = send_to_llm(
            message, first_message=True, context=context)
        print(f"LLM response: {llm_response}")
    else:
        print(f"Received message: {message}")
        llm_response = send_to_llm(message, first_message=False)
        print(f"LLM response: {llm_response}")

    # Step 3: Perform actions based on the LLM response
    if "action" in llm_response:
        action_result = execute_tool(llm_response["action"])
        llm_response["action_result"] = action_result

    # Step 4: Update the mission log
    mission_log = load_mission_log()
    if "conversation" not in mission_log or not isinstance(mission_log["conversation"], list):
        # Ensure the conversation key exists and is a list
        mission_log["conversation"] = []
    mission_log["conversation"].append(
        {"message": message, "response": llm_response})
    save_mission_log(mission_log)

    # Step 5: Emit the response back to the client
    emit("response", llm_response)
    return


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8080, debug=True)
