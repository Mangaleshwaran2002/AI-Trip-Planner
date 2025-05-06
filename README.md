# AI Trip Planner Streamlit App

This project is a web-based application designed to help users plan their trips by interacting with an AI assistant. The app uses the Streamlit framework for the frontend, and the OpenAI API for generating personalized travel recommendations. The assistant provides suggestions for destinations, activities, accommodations, transportation, and other travel-related needs based on user preferences.
## Features
AI-powered Travel Planning: Interact with an AI assistant to get personalized travel suggestions tailored to your preferences.

Real-Time Chat: Chat with the assistant in real-time, asking for recommendations on destinations, activities, accommodations, and more.

Weather and Local Events: Get up-to-date information on weather forecasts and local events to help you plan your trip.

Budget-Friendly: The AI provides options for activities, flights, hotels, and itineraries that fit within the user's budget and interests.

Streaming Responses: The assistant responds with streaming content, making the conversation feel natural and interactive.

# Screenshots
![AI Trip Planner-s1](https://raw.githubusercontent.com/Mangaleshwaran2002/AI-Trip-Planner/refs/heads/master/Screenshot/AI-Trip-planner-s1.png)
![AI Trip Planner-s2](https://raw.githubusercontent.com/Mangaleshwaran2002/AI-Trip-Planner/refs/heads/master/Screenshot/AI-Trip-planner-s2.png)
![AI Trip Planner-gif](https://raw.githubusercontent.com/Mangaleshwaran2002/AI-Trip-Planner/refs/heads/master/Screenshot/AI-Trip-planner-gif.gif)
## Requirements

To run this application, you'll need to install the following Python packages:

 * streamlit: Framework for creating the web app.
 * openai: To interact with the OpenAI API.
 * python-dotenv: To manage environment variables securely.

You can install them using pip:

```bash
pip install streamlit openai python-dotenv
```

### Setup
Step 1: Clone the Repository

Start by cloning this repository to your local machine:
```bash
git clone https://github.com/your-username/ai-trip-planner.git
cd ai-trip-planner
```
Step 2: Configure Environment Variables

Create a .env file in the root directory of the project, and add your OpenAI API key and other necessary environment variables.
```bash
OPENAI_APIKEY=your_openai_api_key_here
OPENROUTER_APIKEY=your_openrouter_api_key_here
OPENROUTER_BASE_URL=https://api.openai.com/v1
```
Replace your_openai_api_key_here and your_openrouter_api_key_here with your actual API keys.
Step 3: Run the Application

Once the environment variables are set, you can run the app using Streamlit:
```bash
streamlit run app.py
```
This will open the app in your default browser, where you can start chatting with the AI assistant and receive travel recommendations.
Code Walkthrough
 * Environment Variables: The dotenv package loads the .env file to securely access the API keys (OPENAI_APIKEY, OPENROUTER_APIKEY). These are used to authenticate and communicate with OpenAI's API.
 * Streamlit: The app uses Streamlit to create a simple and interactive chat interface. Users can input their travel-related queries, and the assistant responds with recommendations based on the given context.
 * OpenAI API: The app communicates with the OpenAI API to generate travel recommendations. The assistant model is configured to provide tailored suggestions based on the user’s preferences and budget.
 * Session State: The st.session_state is used to store the conversation history, so the assistant can maintain context between different user inputs.
 * Chat Streaming: The app uses streaming responses to provide a real-time conversational experience. The assistant’s replies are displayed progressively as they are generated, simulating a natural flow.


## Contributing

Feel free to open issues, fork the repository, and submit pull requests if you have any improvements or bug fixes!
License

This project is licensed under the MIT License - see the LICENSE file for details.
