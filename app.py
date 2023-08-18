from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

class LLMWrapper:
    def __init__(self, model_name, max_tokens=1024, rate_limit_retries=3):
        self.generator = pipeline('text-generation', model=model_name)
        self.max_tokens = max_tokens
        self.rate_limit_retries = rate_limit_retries
        self.conversation_history = []

    def add_to_history(self, text):
        self.conversation_history.append(text)

    def format_prompt(self):
        prompt = "\n".join(self.conversation_history[-3:])  # Considering the last 3 inputs for context
        return prompt

    def handle_errors(self, response):
        # Adjust error handling logic based on the actual response structure
        if 'Rate limit' in response:
            print("Rate limit exceeded. Retrying...")
            return True
        return False

    def generate_response(self, prompt):
        for _ in range(self.rate_limit_retries + 1):
            response = self.generator(prompt, do_sample=True, min_length=10, max_length=self.max_tokens)[0]['generated_text']
            if not self.handle_errors(response):
                return response
        return "Rate limit error. Please try again later."

# Initialize your LLMWrapper instance
gpt_neo_model_name = "EleutherAI/gpt-neo-125M"
wrapper = LLMWrapper(gpt_neo_model_name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    user_input = data['seed_word']
    
    # Add user input to the conversation history
    wrapper.add_to_history(f"You: {user_input}")
    prompt = wrapper.format_prompt()
    response = wrapper.generate_response(prompt)
    
    # Add LLM response to the conversation history
    wrapper.add_to_history(f"LLM: {response}")
    
    return jsonify({'generated_text': response})

if __name__ == "__main__":
    app.run(debug=True)
