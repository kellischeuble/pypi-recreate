import flask

app = flask.Flask(__name__)

# For debug mode
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

<style>
</style>

def get_latest_packages():
    return[
        {'name': 'flask', 'version': '1.2.3'},
        {'name': 'sqlalchemy', 'version': '2.2.0'},
        {'name': 'passlib', 'version': '3.0.0'},
    ]

@app.route('/')
def index():
    test_packages = get_latest_packages()
    return flask.render_template('index.html', packages=test_packages)

if __name__ == '__main__':
    app.run(debug=True)