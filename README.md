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

## Installation Steps

Follow these steps to setup the project:

1. Clone the repository: 
```
git clone https://github.com/sn1p2r78/CaptchaXtract-standalone-v2
```

2. Virtual environment: 
```
create virtual env
source venv/bin/activate ``
conda env 

3. Install Tesseract: 
```
For more information, see Tesseract Wiki: https://github.com/UB-Mannheim/tesseract/wiki 
```
4. Install dependencies: 
```
python3 -m requirements.exe -e requirements.txt ``

5. Run the application: 
```
python3 src/image_to_text_service.py ``

Now you're set up and ready to run the service!
