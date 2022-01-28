import random
import data.db_connector
import random

from flask import Flask

app = Flask(__name__)

total_elements = None

@app.route('/update')
def setup():
    # GET TOTAL ELEMENTS
    global total_elements

    print("Setting up the application...")
    total_elements = data.db_connector.get_total_elements()
    if total_elements == 0:
        return "No elements found. Please, check Database..."
    return str(total_elements)

@app.route('/get')
def get_question():
    global total_elements

    if not total_elements:
        setup()
    question = data.db_connector.fetch_question(random.randint(0, total_elements))    
    print(dict(question.items()))
    return dict(question.items())
@app.after_request
def add_headers(response):
    response.headers.add('Content-Type', 'application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'PUT, GET, POST, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Expose-Headers', 'Content-Type,Content-Length,Authorization,X-Pagination')
    return response
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=443)
