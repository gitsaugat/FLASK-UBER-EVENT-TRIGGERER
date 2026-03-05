# Flask Uber Event Triggerer

A Flask-based web application that simulates a ride-booking interface (Uber-like) and sends ride request events to **Azure Event Hubs**.

## Features

- **Uber-like UI**: A premium, responsive interface for requesting rides.
- **Azure Event Hubs Integration**: Uses the `azure-eventhub` Python SDK to send JSON payloads to an Event Hub.
- **Environment Configuration**: Easy setup using `.env` files.
- **Event Schema**: Sends structured data including pickup, destination, ride type, and timestamps.

## Prerequisites

- Python 3.8+
- An [Azure Event Hubs Namespace](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-create) and an **Event Hub**.
- Connection String for the namespace.

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/gitsaugat/FLASK-UBER-EVENT-TRIGGERER.git
cd FLASK-UBER-EVENT-TRIGGERER
```

### 2. Set up a virtual environment (Optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy the template and fill in your Azure details:
```bash
cp .env.example .env
```
Edit `.env`:
```env
EVENT_HUB_CONNECTION_STR="Endpoint=sb://..."
EVENT_HUB_NAME="your-event-hub-name"
```

### 5. Run the application
```bash
python app.py
```
The application will start on `http://localhost:5500`.

## How it Works

1. The frontend (`templates/index.html`) captures ride details.
2. When "Book Ride" is clicked, a POST request is sent to the `/send` endpoint.
3. The Flask backend (`app.py`) transforms the data into an `EventData` object.
4. The `EventHubProducerClient` sends the event batch to Azure Event Hubs.

## Project Structure

```text
├── app.py              # Flask backend & Event Hub producer
├── templates/
│   └── index.html      # Uber-like booking UI
├── .env.example        # Environment variable template
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```
