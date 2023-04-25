# AI Card Generator

This app lets you get customized card designs and message based on user input.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes

### Prerequisites

Make sure to have python and pip installed on your system.

Run this command : 

```
pip install -r requirements.txt
```

Add your api keys and aws info in the const.py file.

```python
BUCKET_NAME = ""
ACCESS_KEY_ID = ""
SECRET_ACCESS_KEY = ""

SD_API_KEY = ""
MODEL_ID = ""

OPENAI_API_KEY = ""
```

### Booting Up
Run the main file in you cmd.
```
python app.py
```

## Built With

- [flask](https://flask.palletsprojects.com/en/2.2.x/ "link") - The python framework used
