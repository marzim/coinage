from flask import Flask
app = Flask(__name__)

import admin

@app.route("/")
def hello():
    return "hello world!"

admin.add_routes(app)

if __name__ == "__main__":
    app.run()