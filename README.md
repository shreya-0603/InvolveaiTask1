# InvolveaiTask1
Open this project to your vscode and open terminal and run python app.py. Then, open postman, to GET all the descriptions and sales pitches select GET method and http://127.0.0.1:5000/sales-pitches. To add a new description and sales-pitch use POST method and http://127.0.0.1:5000/sales-pitches. To delete all the descriptions use DELETE option with http://127.0.0.1:5000/sales-pitches.

#How project was created.
Firtst of all I get API key from OpenAi account. Also created a database using MongoDb to store data. I used that API key with my app.py file and Postman API to get,update and delete data from Mongodb using Postman.

Screenshorts of Working API
1. POST method: It will get an information from OpenAi and store it to MongoDb.

![Screenshot (16)](https://github.com/shreya-0603/InvolveaiTask1/assets/97119040/26b4bb40-65e7-4f3b-9012-e4b24eacac4b)

2. GET Method: It will get all the information from the Mongodb.
