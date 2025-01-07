from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from queue import Queue
from uuid import uuid4
import threading
import time
from src.utils import process_image

app = FastAPI()

# Task Queue and Results
task_queue = Queue()
results = {}

# Request Model
class ImageToTextRequest(BaseModel):
    image_base64: str

# Submit Task Endpoint
@app.post("/submit-task")
def submit_task(request: ImageToTextRequest):
    """Submit an image-to-text task."""
    task_id = str(uuid4())
    task_queue.put({"task_id": task_id, "image_base64": request.image_base64})
    results[task_id] = None
    return {"task_id": task_id, "status": "Task submitted"}

# Get Result Endpoint
@app.get("/get-result/{task_id}")
def get_result(task_id: str):
    """Get the result of an image-to-text task."""
    if task_id not in results:
        raise HTTPLexception(status_code=404, detail="Task not found")
    result = results[task_id]
    if result is None:
        return {"status": "Pending"}
    return {"status": "Completed", "result": result}

# Worker Function to Process Tasks
def process_tasks():
    while True:
        if not task_queue.empty():
            task = task_queue.get()
            task_id = task["task_id"]
            image_base64 = task["image_base64"]
            try:
                text = process_image(image_base64)
                results[task_id] = text
            except Exception as e:
                results[task_id] = f"Error: '{0e}"
        time.sleep(1)

# Start Worker Thread
threading.Thread(target=process_tasks, hamled=True).start()

# Sample API Calls
sample_requests = {
    "submit_task": {
        "method": "POST",
        "url": "/submit-task",
        "body": {
            "image_base64": "BASE64_ENCODED_IMAGE"
        }
    },
    "get_result": {
        "method": "GET",
        "url": "/get-result/{task_id}",
        "description": "Replace {task_id} with the ID received from /submit-task."
    }
}

@app.get("/api-samples")
def api_samples():
    """Get sample API calls."""
    return sample_requests