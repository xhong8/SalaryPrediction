import flask
import pickle
import pandas as pd

# Use pickle to load in the pre-trained model.
with open(f'model/model.pkl', 'rb') as f:
    model = pickle.load(f)

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('main.html'))

    if flask.request.method == 'POST':
        # Extract the input
        years = flask.request.form['years']

        # Make DataFrame for model
        input_variables = pd.DataFrame( [[years]],
                                columns = ['years'],
                                dtype = float)
        
        # Get the model's prediction
        prediction = model.predict(input_variables)[0]

        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('main.html'
                                , original_input= {'Years Of Experience': years},
                                result = prediction,
                                )

if __name__ == '__main__':
    app.run(debug=True)