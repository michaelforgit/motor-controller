import logging
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
  return "<p>Hello World</p>"

@app.route("/motor/left", methods=['POST'])

def motor_left():
  body = request.get_json()
  steps = body.get('steps', None)
  for x in range(0, int(steps)):
    print("loop here")
  return jsonify({
    'success': True,
  })

@app.route("/motor/right", methods=['POST'])
def motor_right():
  body = request.get_json()
  steps = body.get('steps', None)
  for x in range(0, int(steps)):
    print("loop here")
  return jsonify({
    'success': True,
  })
