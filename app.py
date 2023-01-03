import flask
from flask import request, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET'])
def predict():
    import joblib
    model = joblib.load('marriage_age_predic_model.ml')
    age_predict = model.predict([[int(request.args['gender']),
    int(request.args['religion']),
    int(request.args['caste']),
    int(request.args['mother_tongue']),
    int(request.args['country']),
    int(request.args['height_cms']),
    ]])

    return str(round(age_predict[0],2))

if __name__ == "__main__":
    app.run(debug=True)
