import flask, frolic, importlib
importlib.reload(frolic)

app = flask.Flask(__name__)

@app.route('/')
def main():
    return flask.render_template('main.html')

@app.route('/predict')
def predict():
    form_features = [['Title Length', 'title_len'], 
                     ['Body Length', 'body_len'],
                     ['Answer Count', 'answer_count'],
                     ['Comment Count', 'comment_count'],
                     ['Score', 'score']]
    
    dt_predict = {}
    show_prediction = False
    prediction = None
    
    if 'title_len' in flask.request.args:
        show_prediction = True
        for f in frolic.bm_features: dt_predict[f] = float(flask.request.args[f])
        prediction = round(frolic.predict([dt_predict]),1)
        
    return flask.render_template('predict.html', form_features=form_features, show_prediction=show_prediction,
                                 prediction=prediction, dt_predict=dt_predict)

if __name__ == '__main__':
    app.run(port=80, debug=True, host='0.0.0.0')
