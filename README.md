# InvolveaiTask1
Open this project to your vscode and open terminal and run python app.py. Then, open postman, to GET all the descriptions and sales pitches select GET method and http://127.0.0.1:5000/sales-pitches. To add a new description and sales-pitch use POST method and http://127.0.0.1:5000/sales-pitches. To delete all the descriptions use DELETE option with http://127.0.0.1:5000/sales-pitches.

STEP 1: Set up the Project

Create a new directory for project and navigate to it.
Initialize a virtual environment using following command:
python3 -m venv venv
source venv/bin/activate (Linux/Mac)
venv\Scripts\activate (Windows)
Install Flask and required dependencies:
pip install Flask pymongo openai

STEP 2: Add app.py file which is uploaded on this repo.

STEP 3: start the mongo server using mongod command then run python app.py

STEP 4: Test API using Postman

#How project was created.
Firtst of all I get API key from OpenAi account. Also created a database using MongoDb to store data. I used that API key with my app.py file and Postman API to get,update and delete data from Mongodb using Postman.


Screenshorts of Working API
1. POST method: It will get an information from OpenAi and store it to MongoDb.

![Screenshot (16)](https://github.com/shreya-0603/InvolveaiTask1/assets/97119040/26b4bb40-65e7-4f3b-9012-e4b24eacac4b)

2. GET Method: It will get all the information from the Mongodb.
![Screenshot (17)](https://github.com/shreya-0603/InvolveaiTask1/assets/97119040/18314da5-8ca8-4ff5-97e9-68fabc1da23c)

3. DEL Method: It will delete all the information from MongoDB.
![Screenshot (18)](https://github.com/shreya-0603/InvolveaiTask1/assets/97119040/c3dc74c1-556b-4763-9e7f-4870864d7285)

