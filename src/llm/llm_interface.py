import ollama
import json


def send_to_llm(prompt, first_message=False, context=None):
    # TODO: Change the model name to the correct model or swap the Ollama API for another LLM API
    client = ollama.Client()
    model_name = "llama3.1"  # Use the correct model name

    # TODO: Construct the prompt with explicit finalization instructions
    # Reminder: The prompt should include the available tools, instructions for how to respond, and the user's prompt
    context_text = json.dumps(
        context) if context else "No additional context provided."
    first_prompt = f"""
    We are going to play a Secrete Agent game. Here is the context: {context_text}
    Here is the user's first message: {prompt}
    Respond with clear and actionable information. If tools are required, specify the tool and parameters.
    """
    followup_prompt = f"""
    Considering the prior conversation, here is the user's next prompt: {prompt}
    Respond with clear and actionable information. If tools are required, specify the tool and parameters.
    """

    try:
        # Send the prompt to the LLM
        if first_message:
            response = client.generate(model=model_name, prompt=first_prompt)
        else:
            response = client.generate(
                model=model_name, prompt=followup_prompt)
        # Debugging: Print the raw response
        print(f"Raw LLM response: {response.response}")
        # Remove "Rate this interaction:" from the response
        cleaned_response = response.response.split(
            "Rate this interaction:")[0].strip()

        return {"message": cleaned_response}

    except Exception as e:
        print(f"Error communicating with the LLM: {e}")
        return {"message": "Failed to communicate with the LLM server."}
