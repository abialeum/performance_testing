# Performance API Testing
Learning unit testing with python

## Setup
Install python on windows
- [Python Installation Guide](https://www.digitalocean.com/community/tutorials/install-python-windows-10)

Install python on MacOS
```
brew install python
```

Install python lib
```
pip3 install -r requirements.txt
pip3 install --upgrade urllib3
```

## How to Run
Run our application
```
python3 app/app.py
```

Run our locust
```
locust --host=http://127.0.0.1:5000
```