from flask import Flask, request, jsonify

default_data = {}
all_data = []
app = Flask(__name__)


@app.route('/received_email', methods=['POST'])
def generate_auth_device_key():
    html = request.form["html"]
    temp_pass = html.split("</strong>")[1].split("<br>")[0].strip()
    to = request.form["to"]
    uid = to.split("<")[1].split("@")[0]
    default_data[uid] = temp_pass
    all_data.append(request.form)
    return "ok"


@app.route('/', methods=['GET'])
def app_index():
    str_ = "<h2><font color=\"green\">emails API.</font></h2>" \
           "<p>/received_email POST</p>" \
           "<p>/get_email GET all</p>" \
           "<p>/get_email/<uuid> GET by id</p>" \
           "<p>/get_all_data GET all incoming data</p>" \
           "<p>/delete_email DELETE</p>"

    return str_


@app.route('/get_email', methods=['GET'])
def get_all_email():
    return jsonify(default_data)


@app.route('/get_all_data', methods=['GET'])
def get_all_email():
    return jsonify(all_data)


@app.route('/get_email/<uuid>', methods=['GET'])
def get_email_by_id(uuid):
    return default_data.get(uuid)


@app.route('/delete_email', methods=['DELETE'])
def delete_emails():
    default_data.clear()
    return jsonify("all emails deleted. ")
