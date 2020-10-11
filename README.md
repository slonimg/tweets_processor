### Api

A Flask application that consumes a streaming endpoint and maintains counters.
The 10 most common items for each counter are calculated every 50 messages that are processed.
The reason for this is to enable quick response to a react consumer application.
 
~~~
source venv/bin/activate
cd api
flask run
~~~

#### Notes
###### Server Workings
1.The server applications connects to a streaming source and processes texts into Counters
- a more sustainable solution would be to put the streams into a queue/message broker and 
process them in a different application

- This processor could then put the results in an outer storage such a redis
and the results could be read by the Flask application     
###### Ignoring words for the counter
2.There is an *[ignore_dictionary.txt](https://github.com/slonimg/tweets_processor/blob/main/api/ignore_dictionary.txt)* file that contains words to ignore. 
- It is probably better to use TFIDF algorithm but this Quick and Dirty solution works as well.

######



---
 
### App

A react consumer application that shows the streaming consumer data. 
~~~
cd app
npm install
npm start
~~~

#### Notes
1.The web applications pulls data from the API every 5 seconds   



#### General Notes
The python venv was pushed for simplicity
