# Story Summarizer

# Installation Guide
## Testing Locally
### Cloning the repository 

Using SSH

```git clone git@github.com:Nedu/summarizer.git```

Using HTTPS

```git clone https://github.com/Nedu/summarizer.git```

### Changing Directories
```cd summarizer```

### Installing Pipenv

```pip install pipenv```

### Installing required Requirements

```pipenv install```

### Activating virtual environment

```pipenv shell```

### Changing the host

Change the last line of app.py from ```app.run(host='0.0.0.0', debug=True, port=5000)``` to ```app.run(host='localhost', debug=True, port=5000)``` 

### Running the App

```python app.py```

### Summarizing a Story

To summarize a story, make a POST request to ```http://127.0.0.1:5000``` using this body format ``` { "story": "your story here"}```.
You should get a response in this format ```{ "summary": "your story summary here" }```
