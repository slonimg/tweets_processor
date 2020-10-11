### Api

A Flask application that consumes a static endpoint
~~~
source venv/bin/activate
pip install requirements.txt
cd api
flask run
~~~

#### Notes
###### Server Workings
 The server applications connects to a streaming source and processes texts into Counters
- a more sustainable solution would be to put the streams into a queue/message broker and 
process them in a different application

- This processor could then put the results in an outer storage such a redis
and the results could be read by the Flask application     
###### Ignoring words for the counter
There is an *ignore_dictionary.txt* file that contains words to ignore. 
- It is probably better to use TFIDF algorithm but this Quick and Dirty solution works as well.

######



---
 
### App
~~~
cd app
npm install
npm start
~~~

#### Notes
###### The web applications pulls data from the API every 5 seconds   