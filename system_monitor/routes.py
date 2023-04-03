import werkzeug.exceptions
from flask import render_template, jsonify
from system_monitor import app
import json

with open('system_monitor/config.json') as f:
    data = json.load(f)

interval = data["SystemMonitor"]["interval_time_sec"]


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', title="Home Page")


@app.route('/system')
def my_system():
    with open("system_data.csv") as file:
        return render_template('system_page.html', data=file, number=interval, title='Machine Monitor Page')


@app.route('/docker')
def my_docker():
    with open("docker.csv") as file:
        return render_template('docker_page.html', data=file, number=interval, title='Docker Monitor Page')


@app.route("/config")
def config_page():
    return render_template('config.html', title='Config')


@app.route("/log")
def Log_page():
    return render_template('log.html', title='Log Page')


# Reboot the system
@app.route("/rebooting")
def reboot():
    # subprocess.run("sudo reboot", shell=True, check=True)
    return render_template('reboot.html')


# Error Handler
@app.errorhandler(werkzeug.exceptions.NotFound)
def Notfound(e):
    return jsonify(error=str(e)), e.code
