# main.py

from flask import Flask, render_template, request
import openai
from configparser import ConfigParser

app = Flask(__name__)
config = ConfigParser()
config.read('config.ini')

# Set your OpenAI API key (replace 'YOUR_OPENAI_API_KEY' with your actual key)
openai.api_key = config.get('OpenAI', 'api_key')

# Define the route to render the form


@app.route('/')
def index():
    return render_template('index.html')

# Define the route to process the form data and generate script ideas


@app.route('/process_form', methods=['POST'])
def process_form():
    if request.method == 'POST':
        # Handle the form submission and generate script ideas
        product_name = request.form.get('product_name')
        product_description = request.form.get('product_description')

        # Call a function to generate script ideas or perform desired actions
        script_ideas = generate_script_ideas(product_name, product_description)

        return render_template('result.html', script_ideas=script_ideas)
    else:
        # In case a GET request is made to /process_form, redirect to the home page or handle accordingly
        return render_template('index.html')


def generate_script_ideas(product_name, product_description):
    # Construct a prompt for the OpenAI API
    prompt = f"Generate a script idea starting with the word Script idea: then an empty line for a testimonial video ad for {product_name}. The product is {product_description}."

    # Make a request to the OpenAI API
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # You may use a different engine if available
            prompt=prompt,
            max_tokens=400,  # Adjust as needed
            temperature=0.7,  # Adjust for creativity vs. accuracy
            n=3  # Number of completions to generate
        )

        # Extract script ideas from the OpenAI API response
        script_ideas = [choice['text']
                        for choice in response['choices']]
        print(script_ideas)
        return script_ideas
    except Exception as e:
        # Handle exceptions, e.g., API rate limits
        print(f"Error: {e}")
        return ["An error occurred while generating script ideas. Please try again later."]


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
