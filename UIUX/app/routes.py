from app import app, mongo
from flask import render_template, request, redirect
from app.forms import PostForm
from Mutator import mutator
from VirusTotalAPI import vtapi
import json


def report_form(report: dict):

    pass


@app.route('/')
@app.route('/main')
def main():
    return render_template('main.html', title="About Project")


@app.route('/history')
def history():
    collection = mongo["file"]
    file = collection["file"]
    reportFile = []
    for post in file.find():
        reportFile.append({
            "id": post["_id"],
        })
    return render_template('history.html', title="History", reportFile=reportFile)


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = PostForm()
    if request.method == "GET":
        return render_template('form.html', title="Form", form=form)
    elif request.method == "POST":
        collection = mongo["file"]
        file = collection.file
        report1 = vtapi.api('virus/' + request.form["virus"])
        if request.form["type_mutator"] != '1':
            mutated = mutator.mutator(request.form["virus"], request.form["type_mutator"])
        else:
            mutated = mutator.mutator(request.form["virus"], request.form["type_mutator"], request.form['file'])
        report2 = vtapi.api(mutated)
        buffer = {
            "_id": str(file.count() + 1),
            str(file.count() + 1): {
                "report": [report1, report2],
                "type_mutator": request.form["type_mutator"],
                "virus": request.form["virus"]
            }
        }
        if int(request.form['type_mutator']) == 1:
            buffer[str(file.count() + 1)]["file"] = request.form['file']
        else:
            buffer[str(file.count() + 1)]["file"] = None
        file.save(buffer)

        return redirect("/main")


@app.route("/show/<id>")
def show(id):
    virus = {
        "Stealer.exe": "Stealer",
        "Trojan.exe": "Trojan",
        "Winlocker.exe": "WinLocker",
        "RAT.exe": "RAT",
    }
    mutation = {
        1: "Joiner",
        2: "Cryptor",
        3: "WinRAR"
    }
    collection = mongo["file"]
    files = collection["file"]
    file = files.find_one({"_id": id})
    print(file)
    reportFile = {
        "report": {
            "before": {
                "undetected": file[file["_id"]]['report'][0]['data']['attributes']['stats']['undetected'],
                "malicious": file[file["_id"]]['report'][0]['data']['attributes']['stats']["malicious"],
                "suspicious": file[file["_id"]]['report'][0]['data']['attributes']['stats']["suspicious"],
                "link": "http://virustotal.com/gui/file/" + file[file["_id"]]['report'][0]['meta']['file_info']['sha256']
            },
            "after": {
                "undetected": file[file["_id"]]['report'][1]['data']['attributes']['stats']['undetected'],
                "malicious": file[file["_id"]]['report'][1]['data']['attributes']['stats']["malicious"],
                "suspicious": file[file["_id"]]['report'][1]['data']['attributes']['stats']["suspicious"],
                "link": "http://virustotal.com/gui/file/" + file[file["_id"]]['report'][1]['meta']['file_info']['sha256']
            },
        },
        "mutation": mutation[int(file[file["_id"]]["type_mutator"])],
        "virus": virus[file[file["_id"]]["virus"]],
        "id": file["_id"]
    }
    if mutation[int(file[file["_id"]]["type_mutator"])] == 1:
        reportFile['file'] = file[file["_id"]]['file']
    return render_template('show.html', title="History", file=reportFile)
