from google.cloud import pubsub_v1
import os, json, pandas as pd, time
from tabulate import tabulate


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="credentials.json"

def start():

    subscription=_attache_subscription_to_topic()
    _start_listening_to_topic(subscription)


def _attache_subscription_to_topic():
    
    publisher = pubsub_v1.PublisherClient()
    subscriber = pubsub_v1.SubscriberClient()
    topic_path = publisher.topic_path("projectagora-codecamp-workshop", "webinar-workshop-output")
    subscription_path = subscriber.subscription_path("projectagora-codecamp-workshop", "argy_subscription")
    
    try:
        # Wrap the subscriber in a 'with' block to automatically call close() to
        # close the underlying gRPC channel when done.
        with subscriber:
            subscription = subscriber.create_subscription( name=subscription_path, topic=topic_path)
            print(f"Subscription created: {subscription}")
    except Exception as e:
       if "already exists" in str(e.message).lower(): print(str(e.message))
       else: raise Exception (str(e))

    
    return subscription_path


def _start_listening_to_topic(subscription):

    def callback(message):  
        try:
           data = json.loads(message.data)
        except json.JSONDecodeError:    
           print("Json Parsing Error")

        df=pd.DataFrame(data)
        total_revenue_df=pd.DataFrame()
        total_revenue_df["total_revenue_euro"]=df["total_revenue_euro"]
        total_revenue_df["total_revenue_usd"]=df["total_revenue_usd"]
        df.drop(['total_revenue_euro', 'total_revenue_usd'], axis=1, inplace=True)
        total_revenue_df.drop_duplicates(inplace=True)
        print()
        print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
        print(tabulate(total_revenue_df, headers = 'keys', tablefmt = 'psql'))
        print()
        message.ack()
        
        
    
    subscriber = pubsub_v1.SubscriberClient()
    subscriber.subscribe(subscription, callback=callback)

    print('Listening for messages on {}'.format(subscription))
    while True:
        time.sleep(60)


start()