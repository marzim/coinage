from flask import Flask, render_template
app = Flask(__name__)

import admin

@app.route("/")
def hello():
    return render_template("admin.html")

admin.add_routes(app)

if __name__ == "__main__":
    app.run()
