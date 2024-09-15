from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/transaction', methods=['POST'])
def transaction():
    return jsonify({"message": "Transaction Successful"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)