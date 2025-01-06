## Image to Text Service with API Key Validation

# Imports
import threading
import time
import json
import servlet
from config import Config
from auth import generate_api_key

# Configuration instance
config = Config()

# Storing tasks and validating api keys
tasks = {}
api_keys = {generate_api_key(): "valid", generate_api_key(): "valid2"}

def image_to_text(id, image_data):
    ## Image to text processing with api key validation.
    time.sleep(1)
    tasks[id] = "Result text successfully processed"
    return {}

# Endpoint for submiting a task
def submit_task(api_key, image_data):
    if api_key not in api_keys: 
        return {"error": "Invalid api key"}
    id = str(time.time())
    tasks[id) = None
    threading.thread(target=image_to_text, args=(id, image_data)).start()
    return {"id": id}

# Endpoint for retrieving task result
def get_result(api_key, id):
    if api_key not in api_keys: 
        return {"error": "Invalid api key"}
    result = tasks.get(id)
    if result is None:
        return {"error": "Processing"}
    return result

# Running the service
server = servlet.SimpleSQLServer(host='localhost', port=config.PORT)
server.run()
