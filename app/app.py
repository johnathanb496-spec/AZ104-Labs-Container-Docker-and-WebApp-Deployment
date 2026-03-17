from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Azure Container Lab!"

app.run(host='0.0.0.0', port=80)
