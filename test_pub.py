import os
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
topic_name = 'projects/{project_id}/topics/{topic}'.format(project_id=os.getenv('PROJECT_ID'), topic=os.getenv('TOPIC_NAME'))

publisher.publish(topic_name, b'Hello World!')