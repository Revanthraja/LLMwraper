# Language Model Wrapper Demo

This is a simple demo project that demonstrates how to create a web-based interface to interact with a language model using Flask and the Transformers library.

## Overview

This project showcases a web interface that allows users to have conversations with a language model. The frontend is built using HTML, CSS, and JavaScript, while the backend is implemented using Flask. The language model is powered by the `transformers` library.

## Setup

1. Install the required Python packages using the following command:
   

2. Run the Flask app:


3. Open your web browser and navigate to `http://127.0.0.1:5000/` to interact with the language model.

## Project Structure

- `app.py`: This is the main Flask application that serves the HTML frontend and handles user interactions.
- `templates/index.html`: The HTML template for the frontend.
- `static/style.css`: The CSS stylesheet for styling the frontend.
- `static/script.js`: The JavaScript code for adding interactivity to the frontend.

## Usage

1. Enter a message in the input box and click the "Send" button.
2. The conversation history will be displayed above, including both user and model responses.
3. The frontend sends user messages to the backend via an AJAX request.
4. The backend processes the user message, generates a response using the language model, and sends it back to the frontend.
5. The frontend updates the conversation history with the new message.

## Notes

- This demo uses a simplified language model wrapper for demonstration purposes. In a production environment, consider implementing more advanced error handling, security measures, and optimization.
- This is not a complete project but serves as a starting point for building more complex language model-powered applications.

## Credits

- The `transformers` library by Hugging Face: [https://github.com/huggingface/transformers](https://github.com/huggingface/transformers)
- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
