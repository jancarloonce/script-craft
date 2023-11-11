# main.py


from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key (replace 'YOUR_OPENAI_API_KEY' with your actual key)
openai.api_key = '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'

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
    prompt = f"Generate three script ideas for a testimonial video ad for {product_name}. The product is {product_description}."

    # Make a request to the OpenAI API
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",  # Adjust the engine based on your preference
            prompt=prompt,
            max_tokens=150,  # Adjust the max_tokens based on your desired script length
            n=1,  # Generate three script ideas
        )

        # Extract script ideas from the OpenAI API response
        script_ideas = [choice['text'].strip()
                        for choice in response['choices']]

        return script_ideas
    except Exception as e:
        # Handle exceptions, e.g., API rate limits
        print(f"Error: {e}")
        return ["An error occurred while generating script ideas. Please try again later."]


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
