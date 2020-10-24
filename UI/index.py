import socketserver
import http.server
import logging
import cgi
import json
from flask import Flask, request, send_from_directory
from flask import render_template


# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

#logging.basicConfig(filename='flask.log', filemode='w', level=logging.WARNING)

@app.route('/', methods = ['GET', 'POST'])
def root():

    if request.method == "POST":

        logging.info("in root method")

        with open("form_data.json", "w") as file:
            logging.info("in with open")
            form = request.form
            form_dict = form.to_dict(flat=False)
            json.dump(form_dict, file)

        return render_template('success.html')

    elif request.method == "GET":
        return render_template('index.html')

@app.route('/data/<path:path>', methods = ['GET', 'POST'])
def send_data(path):
    return send_from_directory('data', path)

@app.route('/css/<path:path>', methods = ['GET', 'POST'])
def send_css(path):
    return send_from_directory('css', path)

@app.route('/js/<path:path>', methods = ['GET', 'POST'])
def send_js(path):
    return send_from_directory('js', path)

@app.route('/test', methods = ['GET', 'POST'])
def test():
    data=None
    if request.method == "POST":
        data=request.json['data']
    return render_template('test.html')

if __name__ == "__main__":
    app.run(idebug=True)
