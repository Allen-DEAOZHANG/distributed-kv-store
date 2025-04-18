from flask import Flask, request, jsonify
import hashlib
import sys

app = Flask(__name__)
store = {}

@app.route('/kv/<key>', methods=['GET', 'PUT', 'DELETE'])
def kv_store(key):
    if request.method == 'GET':
        return jsonify({key: store.get(key, None)})
    elif request.method == 'PUT':
        store[key] = request.form['value']
        return jsonify({'status': 'stored', 'key': key})
    elif request.method == 'DELETE':
        store.pop(key, None)
        return jsonify({'status': 'deleted', 'key': key})

if __name__ == '__main__':
    port = int(sys.argv[1].split('=')[-1]) if '--port=' in sys.argv[1] else int(sys.argv[1])
    app.run(port=port)
