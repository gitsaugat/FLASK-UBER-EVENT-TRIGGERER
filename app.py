import os
import json
from flask import Flask, request, jsonify, render_template
from azure.eventhub import EventHubProducerClient, EventData
from dotenv import load_dotenv
import sys

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configuration for Azure Event Hub
EVENT_HUB_CONNECTION_STR = os.getenv("EVENT_HUB_CONNECTION_STR")
EVENT_HUB_NAME = os.getenv("EVENT_HUB_NAME")

# Initialize the Event Hub Producer Client
producer = None
if EVENT_HUB_CONNECTION_STR and EVENT_HUB_NAME:
    producer = EventHubProducerClient.from_connection_string(
        conn_str=EVENT_HUB_CONNECTION_STR,
        eventhub_name=EVENT_HUB_NAME
    )

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send_event():
    if not producer:
        return jsonify({
            "error": "Event Hub producer is not initialized. Please check your .env file."
        }), 500

    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        # Create a batch
        event_data_batch = producer.create_batch()
        
        # Add event to the batch
        event_data_batch.add(EventData(json.dumps(data)))

        # Send the batch of events to the event hub
        producer.send_batch(event_data_batch)
        
        return jsonify({
            "message": "Event sent successfully to Azure Event Hub",
            "data": data
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = 5500
    app.run(host="0.0.0.0", port=port, debug=True)
