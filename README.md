# CaptchaXXtract-Standalone-v2

This project includes the following new features:

## Image-to-Text Service

An image-to-text service with multithreading support. This service provides the following API endpoints:

** /submit-task - Submit an image to process. Syntax:
```json
"/task": "post",
"data": "<string>" #Image file or base64 encoded data
```

** /get-result - Fetch the result of submitted task. Syntax:
```json
"/task/{task_id}": "get"
```

## Workflow and Multithreading

Implements use a background thread to process multiple images simultaneously. Example:

## Admin Panel

The admin panel now includes management features for the image-to-text service, as well as settings and status.

Please see the [admin panel](link) file for details.
