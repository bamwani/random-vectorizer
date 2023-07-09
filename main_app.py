from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import html
import bleach

app = Flask(__name__)
CORS(app)


@app.after_request
def add_security_headers(response):
    """
    Adds security headers to the HTTP response.

    Args:
        response: The HTTP response object.

    Returns:
        The modified HTTP response object with added security headers.
    """
    # Add security headers
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains; preload'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Content-Security-Policy'] = "default-src 'self'"

    return response


@app.route('/random_vector', methods=['POST'])
def random_vector():
    """
    Generates a random vector and returns it as a JSON response.

    Inputs (via POST form field):
        - sentence (str): The sentence provided by the client.

    Returns:
        A JSON response containing the randomly generated vector.

    Example Request:
        POST /random_vector
        Form Data: {'sentence': 'This is a sample sentence.'}

    Example Response:
        {'vector': [0.123, 0.456, 0.789, ...]}
    """
    sentence = request.form.get('sentence')

    if not sentence:
        return jsonify({'error': 'No sentence provided.'}), 400

    sanitized_sentence = bleach.clean(
        sentence, tags=[], attributes={}, protocols=[], strip=True)

    vector = generate_random_vector()

    return jsonify(vector)


def generate_random_vector():
    """
    Generates a random vector.

    Returns:
        A list representing the randomly generated vector.

    Example Output:
        [0.123, 0.456, 0.789, ...]
    """
    return [random.random() for _ in range(500)]


if __name__ == '__main__':
    # Assuming the SSL certificate is used in the LB. Else SSL .crt and .key will be added below and in gunicorn.
    app.run(debug=True)
