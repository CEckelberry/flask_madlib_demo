from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config["SECRET_KEY"] = "chickenzarecooll21837"

debug = DebugToolbarExtension(app)


@app.route("/")
def home_page():
    return render_template("base.html")


@app.route("/form")
def form_page():
    """Passes through prompts from the story methods in stories.py, loop is in the HTML"""
    prompts = story.prompts
    return render_template("form.html", prompts=prompts)


@app.route("/story")
def create_story():
    """Story page that generates the story based on arguments from the form page"""
    text = story.generate(request.args)
    return render_template("story.html", text=text)
