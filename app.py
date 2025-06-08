import time
import gradio as gr
import os
from dotenv import load_dotenv
from julep import Julep

# Load environment variables from .env file
load_dotenv()

# Get API key and agent ID from environment variables
api_key = os.environ.get("JULEP_API_KEY")
agent_id = os.environ.get("JULEP_AGENT_ID")

# Initialize Julep client
client = Julep(api_key=api_key)

def generate_foodie_tour(cities):
    """Generate a foodie tour for the given cities."""
    # Compose the prompt for the agent
    user_prompt = (
        f"Build a one-day foodie tour for these cities: {cities}. "
        "For each city, check today's weather and suggest indoor or outdoor dining, "
        "pick 3 iconic local dishes, find top-rated restaurants serving these dishes, "
        "and create a delightful foodie tour with breakfast, lunch, and dinner narratives that factor in weather conditions."
    )

    # Create a task for your agent with the prompt as input
    task = client.tasks.create(
        agent_id=agent_id,
        name="Interactive Foodie Tour",
        description=f"Generate foodie tour for: {cities}",
        main=[
            {
                "prompt": [
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ]
            }
        ]
    )

    # Start execution
    execution = client.executions.create(
        task_id=task.id,
        input={}
    )

    # Poll for result
    while (result := client.executions.get(execution.id)).status not in ['succeeded', 'failed']:
        time.sleep(1)

    if result.status == "succeeded":
        # Extract the main text content from the output
        return result.output["choices"][0]["message"]["content"]
    else:
        return f"Error generating tour: {result.error}"

def chat_interface(message, history):
    """Chat interface function for Gradio."""
    if not message.strip():
        return "Please enter one or more cities separated by commas."
    
    response = f"🍽️ Generating foodie tour for: {message}...\n\nThis may take a minute or two, please wait."
    yield response
    
    # Generate the actual foodie tour
    cities = message.strip()
    tour_response = generate_foodie_tour(cities)
    
    yield tour_response

# Create Gradio interface
demo = gr.ChatInterface(
    chat_interface,
    title="🌍 Global Foodie Tour Generator",
    description="Enter one or more cities separated by commas (e.g., 'Paris, Tokyo, New York') to get a personalized one-day foodie tour for each city!",
    examples=["Mumbai, Rome, Tokyo", "Paris, New York", "Bangkok, Seoul, Istanbul"],
    theme="soft"
)

if __name__ == "__main__":
    demo.launch(share=True)  # set share=False if you don't want a public link
