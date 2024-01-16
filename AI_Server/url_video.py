from flask import Flask, request, jsonify
from flask_cors import CORS

import sys
sys.path.append('./AI_HandSign')
from media_main import textDetection

app = Flask(__name__)
CORS(app, origins="*")

@app.route('/text_detection', methods=['POST'])
def result():
    if request.method == 'POST':
        # Use request.get_json() to get JSON data
        data = request.get_json()

        # Extract data from JSON
        urlVideo = data.get('urlVideo', '')

        # Process video => text use AI
        text = textDetection(urlVideo)

        message_response = {
            'message': 'Processed the data successfully!',
            'status': '200',
            'text': text
        }

        return jsonify(message_response)

if __name__ == '__main__':
    app.run(debug=True)
    app.run("localhost", 5000)
