from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 ZENNIX</h1>
    <p>Сайт работает!</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
