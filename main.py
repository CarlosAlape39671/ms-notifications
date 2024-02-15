from flask import Flask, request, jsonify
from test import Test

app = Flask(__name__)

@app.route('/send_email', methods=['POST'])
def send_email():
    info_request = request.get_json()
    tt = Test(info_request['message'], info_request['recipient'], info_request['subject_line'])
    if tt.send_the_email():
        respuesta = {
            "mensaje": "the message has been sent"
        }
    else:
        respuesta = {
            "mensaje": "the message could not be sent"
        }
    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True)