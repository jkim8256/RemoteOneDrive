from flask import Flask, render_template
import OD
import json

app = Flask(__name__)

#client = OD.auth

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/output")
def output():
    OD.create_folder()

    return "success"

@app.route("/download")
def download():
    OD.download()

    #return render_template("index.html")
    return "success"

@app.route("/upload")
def upload():
    return OD.upload()



#big categories
@app.route("/packaging")
def packaging():
    return render_template("html/packaging.html")


# tasks under packaging
@app.route("/packaging/peek_anchor")
def peek_anchor():
    return render_template("html/packaging/peek_anchor.html")


# functions under peek anchor
@app.route("/peek_anchor_upload/<string:filename>", methods = ['POST'])
def new_uplaod(filename):
    fileName = json.loads(filename)
    print(fileName)
    return OD.new_upload(fileName)


if __name__ == '__main__':
    app.run(debug= True)
