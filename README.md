# CaptchaXtract-Standalone-V2

This is version 2 of the CaptchaXtract standalone application.

## Features

- User management (edit, block, remove)
- API key generation and validation
- Asynchronous Task queue for processing with new submit-task and get-result endpoints
- User friendly web-based panel with statistics and task monitoring


## Usage

````sh
pip install captchakxtract-standalone-v2
```

## User API:


```curl
-- request with sample request body

   "api_key": "api-key-sample",
   "image_base64": "base64 image"
```