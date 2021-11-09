from google.cloud import pubsub_v1
import pandas as pd, json, os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="credentials.json"

def start(c):

    array_of_recs=_load_csv("raw_data.csv")
    message_attributes={"participant_name": f"argy{c}"}
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path("projectagora-codecamp-workshop", "webinar-workshop-input") 
    resp=_publish_message(publisher, topic_path, array_of_recs,message_attributes)
    print(f"message successfully published with message_id:{resp}")


def _load_csv(file):
    df=pd.read_csv(file)
    return df.to_dict(orient="records")


def _publish_message(publisher, topic_path, data, attributes: dict):        
    future=publisher.publish(topic_path, json.dumps(data).encode("utf-8"), **attributes)
    message_id=future.result()

    return message_id


for i in range(1,30):
   start(i)