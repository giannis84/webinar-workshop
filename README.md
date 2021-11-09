# Project Agora Workshop - Patras Codecamp #

This workshop's purpose is the familiarization with serverless and scalable technologies for big data processing.
More specific in this workshop you are going to ingest data in our Big Data processing system through a pub/sub topic, then our system will process your data and finally will reply to you with a message that will give you the latest updated contest's results every time a change is occurred. 

## Publisher App ##
You are given a publisher application. A publisher is the code that is responsible for publishing messages to a pub/sub topic. In our case the publisher application
will read raw data from a csv file and then it will publish those data as message to a topic.

Before you start the publisher docker, you will need first to find the spots in its code (publisher/app/main.py) and fill the gaps with with the needed parameters.
More specific you need to find the line:

    1. and set "credentials.json" (cloud credentials for publishing persmissions) as environment variable
    2. where the csv file is loaded and set the input parameter as "raw_data.csv"
    3. where the "participant_name" is being set and fill it with your name
    4. where the topic path is being composed and set the project id as "projectagora-codecamp-workshop"
    5. where the topic path is being composed and set the topic name as "webinar-workshop-input"


## Subscriber App ##
You are given a subscriber application. A subscriber is the code that is responsible for listening to a subscription fow new messages. That is achieved by attaching a subscription to a pub/sub topic. Then every time a new message is being publsihed to that topic, the subscriber will receive it. In our case the subscriber application will print the messages to console stdout as soon as they received. That messages will contain all participants' revenue contribution so far and the sum of revenues per participant ordered ascending by the faster ones.

Before you start the subscriber docker, you will need first to find the spots in its code (subscriber/app/main.py) and fill the gaps with with the needed parameters.
More specific you need to find the line:

    1. and set "credentials.json" (cloud credentials for creating and listening to a subscription persmissions) as environment variable
    2. where the topic path is being composed and set the project id as "projectagora-codecamp-workshop"
    3. where the topic path is being composed and set the topic name as "webinar-workshop-output"
    4. where the subscription path is being composed and set the project id as "projectagora-codecamp-workshop"
    5. where the subscription path is being composed and set the subscription as "{your_name}_subscription"


## Start The Services ##

   # Subscriber #
   1. open a terminal
   2. cd to /your path/to/subscriber
   3. docker build -t subscriber -f docker/dockerfile .
   4. docker run subscriber

   # Publisher #
   1. open a terminal
   2. cd to /your path/to/publisher
   3. docker build -t publisher -f docker/dockerfile .
   4. docker run publisher
