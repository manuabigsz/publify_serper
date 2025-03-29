from flask import Flask, request, jsonify
import http.client
import json
import os

app = Flask(__name__)

API_KEY =  os.getenv("APIKEY") 

@app.route('/search', methods=['GET'])
def search_news():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Missing query parameter 'q'"}), 400
    
    conn = http.client.HTTPSConnection("google.serper.dev")
    payload = json.dumps({"q": query})
    headers = {
        'X-API-KEY': API_KEY,
        'Content-Type': 'application/json'
    }
    
    conn.request("POST", "/news", payload, headers)
    res = conn.getresponse()
    data = res.read()
    
    return jsonify(json.loads(data.decode("utf-8")))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
