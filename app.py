from flask import Flask, render_template, request
import os
from painpoint_agent import match_features

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    keyword = ''
    if request.method == 'POST':
        keyword = request.form.get('keyword', '')
        if keyword:
            results = match_features(keyword, top_k=5)
    return render_template('index.html', results=results, keyword=keyword)

if __name__ == '__main__':
    app.run(debug=True) 