from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    """
    Translates from English to French
    """

    return translator.english_to_french(request.args.get("textToTranslate"))

@app.route("/frenchToEnglish")
def french_to_english():
    """
    Translates from French to English
    """

    return translator.french_to_english(request.args.get("textToTranslate"))

@app.route("/")
def render_index_page():
    """
    Render index page
    """

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
