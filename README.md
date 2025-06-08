# 🌍 Global Foodie Tour Generator

An interactive Gradio chat app that generates personalized one-day foodie tours for any cities in the world—powered by a Julep AI agent.

**🚀 Try it live**: [https://huggingface.co/spaces/arittrabag/Foodie_Tour_Planner-Julep](https://huggingface.co/spaces/arittrabag/Foodie_Tour_Planner-Julep)

## Features

- **Chat Interface**: Simple, intuitive Gradio-based chat UI
- **Flexible Input**: Enter any combination of cities, separated by commas
- **Detailed Foodie Tours**: For each city, the agent generates:
  - Plausible weather with indoor/outdoor dining recommendations
  - Three iconic local dishes (breakfast, lunch, dinner)
  - Top-rated restaurants for each meal (LLM-generated)
  - Creative foodie tour narratives factoring in weather and local culture

## How It Works

1. Enter one or more cities in the chat interface
2. The app sends a prompt to the Julep AI agent, which uses its general world knowledge (no live data)
3. The agent reasons about the weather, local dishes, and restaurants, and writes a full narrative itinerary
4. Results are shown instantly in the chat interface

## Setup & Running

1. Install required packages:
   ```
   pip install julep gradio python-dotenv
   ```

2. Set up your environment variables in a `.env` file:
   ```
   JULEP_API_KEY=your_julep_api_key
   JULEP_AGENT_ID=your_julep_agent_id
   ```

3. Run the app:
   ```
   python app.py
   ```

4. Open the link shown in your terminal to access the chat interface

## Example Inputs

- "Mumbai, Rome, Tokyo"
- "Paris, New York"
- "Bangkok, Seoul, Istanbul"

## Notes

- Tour generation may take 1–2 minutes depending on the number of cities
- All outputs are based on the AI's reasoning and world knowledge; no live API calls or real-time data are used
- API credentials are safely loaded from your ```.env``` file 
