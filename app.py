from flask import Flask, jsonify
import docker

app = Flask(__name__)
client = docker.from_env()

@app.route('/')
def home():
    return "Flask Docker Info App is running!"

@app.route('/containers')
def list_containers():
    containers = client.containers.list()
    container_info = [
        {"id": c.short_id, "name": c.name, "status": c.status}
        for c in containers
    ]
    return jsonify(container_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)