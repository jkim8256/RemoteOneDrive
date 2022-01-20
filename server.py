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

    return render_template("index.html")

@app.route("/upload")
def upload():
    return OD.upload()



#big categories
@app.route("/packaging")
def packaging():
    return render_template("html/packaging.html")

@app.route("/manufacturing")
def manufacturing():
    return render_template("html/manufacturing.html")

@app.route("/inspection")
def inspection():
    return render_template("html/inspection.html")

@app.route("/PO")
def po():
    return render_template("html/PO.html")



# tasks under packaging
@app.route("/packaging/peek_anchor")
def peek_anchor():
    return render_template("html/packaging/peek_anchor.html")

@app.route("/packaging/twist_anchor")
def twist_anchor():
    return render_template("html/packaging/twist_anchor.html")

@app.route("/packaging/threadstone_suture")
def TS_suture():
    return render_template("html/packaging/threadstone_suture.html")

@app.route("/packaging/nitnol_wire")
def nitnol_wire():
    return render_template("html/packaging/nitnol_wire.html")



# tasks under manufacturing
@app.route("/manufacturing/request_form")
def request_form():
    return render_template("html/manufacturing/request_form.html")

@app.route("/manufacturing/production_sheet")
def production_sheet():
    return render_template("html/manufacturing/production_sheet.html")



# tasks under insepction
@app.route("/inspection/IS")
def inspection_sheet():
    return render_template("html/inspection/IS.html")



# tasks under purchase order
@app.route("/PO/PO_Sheet")
def PO_sheet():
    return render_template("html/PO/PO_Sheet.html")



# functions under peek anchor
@app.route("/peek_anchor_upload/<string:filename>", methods = ['POST'])
def new_uplaod(filename):
    fileName = json.loads(filename)
    print(fileName)
    return OD.new_upload(fileName)


if __name__ == '__main__':
    app.run(debug= True)
