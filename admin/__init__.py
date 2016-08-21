from flask import Blueprint, render_template

def add_routes(app=None):
    blueprint = Blueprint('admin', __name__, static_url_path='/admin/static', static_folder='./static',
                          template_folder='./templates')

    @blueprint.route("/admin")
    def admin():
        return render_template('admin.html')

    @blueprint.route("/admin/register")
    def register():
        return render_template("register.html")

    app.register_blueprint(blueprint)