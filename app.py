from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    mermaid_code = None

    if request.method == 'POST':
        file = request.files.get("file")
        if file:
            content = file.read().decode()
            mermaid_code = content.strip()

    return render_template("viewer.html", mermaid=mermaid_code)

if __name__ == '__main__':
    app.run(debug=True)
