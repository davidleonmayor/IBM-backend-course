from flask import Flask, jsonify

app = Flask(__name__)

# config
app.config.from_object('config')
print(f"Debug: {app.config.get('FLASK_DEBUG')} - {app.config.get('ENV')} - key test: {app.config.get('SECRET_KEY')}")

@app.route('/')
def hello_world():
    return jsonify(msg="hello")

# if __name__ == '__main__':
#     app.run()