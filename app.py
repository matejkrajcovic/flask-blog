from flask import Flask
app = Flask(__name__)

articles = ["First Article", "Second Article"]

@app.route("/")
def list():
    return '<br>'.join(articles)

if __name__ == "__main__":
    app.run()
