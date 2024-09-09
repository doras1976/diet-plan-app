from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# Use the API key from the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route('/', methods=['POST'])
def generate_plan():
    data = request.json
    goal = data.get('goal')
    exercise = data.get('exercise')
    diet = data.get('diet')

    prompt = f"Generate a diet plan for someone whose goal is to {goal}, exercises {exercise}, and follows a {diet} diet. Include meals, water intake, supplements, and caffeine advice."

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )

    return jsonify({"plan": response['choices'][0]['text']})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
