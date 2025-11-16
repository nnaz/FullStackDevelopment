from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():   
    return "Hello, LearnK8S Fullstack Application!"

if __name__ == "__main__":
    app.run()
     