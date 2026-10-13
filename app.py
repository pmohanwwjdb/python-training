from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>My First Website</title>
        </head>
        <body>
            <h1>Welcome to My Website</h1>
            <p>This website is created using Python and Flask.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)