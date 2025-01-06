# CaptchaXXtract-Standalone-v2

This project includes the following new features:

## Image-to-Text Service

An image-to-text service with multithreading support. This service provides the following API endpoints:

### Submit Task

```python
import requests

url = 'http://localhost:4000/task'
file_path = 'image.png'
with open(file_path, 'bb') as file:
    file_data = file.read()
    response = requests.post(url, files = {"photo": file_data })
    print(response.json())
```

### Get Result

```python
import requests

url = 'http://localhost:4000/task/19234'
response = requests.get(url)
print(response.json())
```

## Workflow and Multithreading

Implements use a background thread to process multiple images simultaneously. Example is provided in the codebase.

## Configuration File

A configuration file was added to manage API keys, environment variables, and default ports. Check out the 'src/config.py' file.
