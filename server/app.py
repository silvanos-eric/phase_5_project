from flask import Flask, render_template

app = Flask(__name__,
            static_url_path='',
            template_folder='../client/dist',
            static_folder='../client/dist')


@app.route('/api/hello')
def hello():
    import time
    time.sleep(5)
    return {'message': 'Hello, from Flask!'}


@app.errorhandler(404)
def not_found(e):
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=5555)
