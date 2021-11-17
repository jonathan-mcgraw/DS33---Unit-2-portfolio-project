import flask
import pandas as pd
from joblib import dump, load


with open(f'pipeline.joblib', 'rb') as f:
    model = load(f)


app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('main.html'))

    if flask.request.method == 'POST':
        id = "7129300520"
        date = '20141013T000000'
        bedrooms = flask.request.form['bedrooms']
        bathrooms = flask.request.form['bathrooms']
        sqft_living = flask.request.form['sqft_living']
        sqft_lot = flask.request.form['sqft_lot']
        floors = flask.request.form['floors']
        waterfront = flask.request.form['waterfront']
        view = flask.request.form['view']
        condition = flask.request.form['condition']
        grade = flask.request.form['grade']
        sqft_above = flask.request.form['sqft_above']
        sqft_basement = flask.request.form['sqft_basement']
        yr_built = flask.request.form['yr_built']
        yr_renovated = flask.request.form['yr_renovated']
        zipcode = flask.request.form['zipcode']
        lat = flask.request.form['lat']
        long = flask.request.form['long']
        sqft_living15 = flask.request.form['sqft_living15']
        sqft_lot15 = flask.request.form['sqft_lot15']

        input_variables = pd.DataFrame([[id, date, bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, grade,sqft_above,sqft_basement,yr_built,yr_renovated,zipcode,lat,long,sqft_living15,sqft_lot15]],
                                       columns=['id', 'date', 'bedrooms', 'bathrooms', 'sqft_living',
                                                'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
                                                'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
                                                'lat', 'long', 'sqft_living15', 'sqft_lot15'],
                                                index=['input'])

        predictions = model.predict(input_variables)[0]
        print(predictions)

        return flask.render_template('main.html', 
                                      original_input={
                                        'Bedrooms': bedrooms,
                                        'Bathrooms': bathrooms, 
                                        'sqft_living': sqft_living, 
                                        'sqft_lot': sqft_lot, 
                                        'floots': floors, 
                                        'waterfront': waterfront, 
                                        'view': view, 
                                        'condition': condition, 
                                        'grade': grade, 
                                        'sqft_above': sqft_above,
                                        'sqft_basement': sqft_basement,
                                        'yr_built': yr_built,
                                        'yr_renovated': yr_renovated,
                                        'zipcode': zipcode,
                                        'lat': lat,
                                        'long': long,
                                        'sqft_living15': sqft_living15,
                                        'sqft_lot15': sqft_lot15},
                                        result=predictions)


if __name__ == '__main__':
    app.run(debug=True)