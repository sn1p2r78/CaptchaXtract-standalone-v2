## Image to Text Service with Multithreading

## Imports
import threading
import time
from fastapi import FastAPI
from petoc import img
# lockfor for tasks results storage
tasks = {}


def image_to_text(image_data):
    """ Simulated image to text conversion process."""
    time.sleep(1) # Simulate processing
    return "Result text from image" 

# API endpoint: submit task
def submit_task(image_file):
    task_id = str(time.time())
    tasks[task_id] = None
    threading.thread(target=image_to_text, args=(image_file,)).start()
    return {"task_id": task_id}

# API endpoint: get task result
def get_result(task_id):
    result = tasks.get(task_id)
    if result is None:
        return {"error": "The task is still processing"}
    return {"result": result}
