from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        # Use request.get_json() to get JSON data
        data = request.get_json()

        # Extract data from JSON
        name = data.get('Name', '')
        physics = data.get('Physics', '')
        chemistry = data.get('chemistry', '')
        mathematics = data.get('Mathematics', '')

        # In thông tin ra console
        print(f"Name: {name}")
        print(f"Physics: {physics}")
        print(f"Chemistry: {chemistry}")
        print(f"Mathematics: {mathematics}")

        # Có thể thực hiện các xử lý khác ở đây nếu cần

        # Trả về một đối tượng JSON chứa thông báo
        response_data = {
            'message': 'Data received successfully',
            'name': name,
            'physics': physics,
            'chemistry': chemistry,
            'mathematics': mathematics
        }

        return jsonify(response_data)
    
    # if request.method == 'GET':
    #     custom_data = {
    #         'message': 'Hello, this is a custom JSON object!',
    #         'status': 'success',
    #         'data': {
    #             'key1': 'value1',
    #             'key2': 'value2',
    #             'key3': 'value3'
    #         }
    #     }
    #     return jsonify(custom_data)

    # Trả về một phản hồi mặc định nếu không phải là yêu cầu POST
    return jsonify({'message': 'Invalid Request'})

@app.route('/api/get_data', methods=['GET'])
def get_data():
    # Define your custom JSON object
    custom_data = {
        'message': 'Hello, this is a custom JSON object!',
        'status': 'success',
        'data': {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'value3'
        }
    }

    # Return the JSON object as the response
    return jsonify(custom_data)

if __name__ == '__main__':
    app.run(debug=True)
