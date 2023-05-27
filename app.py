from flask import Flask, jsonify, request
from pymongo import MongoClient
import openai

#create a new flask project
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['sales_tool']
collection = db['sales_pitches']

# Configure OpenAI API
openai.api_key = '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'

#to GET all the informations from MongoDb
@app.route('/sales-pitches', methods=['GET'])
def get_sales_pitches():
    sales_pitches = list(collection.find({}, {'_id': 0}))
    return jsonify(sales_pitches)

#Add an information to mongoDb
@app.route('/sales-pitches', methods=['POST'])
def generate_sales_pitch():
    data = request.get_json()
    description = data.get('description')

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"Product description: {description}\nGenerate a compelling sales pitch:",
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
    )
    sales_pitch = response.choices[0].text.strip()

    # Save sales pitch to MongoDB
    collection.insert_one({'description': description, 'sales_pitch': sales_pitch})

    return jsonify({'sales_pitch': sales_pitch})

#Delete all the data from mongoDb
@app.route('/sales-pitches', methods=['DELETE'])
def delete_sales_pitches():
    collection.delete_many({})
    return jsonify({'message': 'All sales pitches deleted'})

if __name__ == '__main__':
    app.run(debug=True)