from flask import Flask, render_template
win=Flask(__name__)

win.add_url_rule('/css/<path:filename>', endpoint='css', view_func=win.send_static_file)

@win.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    win.run(debug=True)