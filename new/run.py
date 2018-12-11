from flask import Flask, render_template as render
from news.new.home import home
from news.new.admin import admin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'QD_SYSTEM'


app.register_blueprint(home)
app.register_blueprint(admin, url_prefix='/admin')


@app.errorhandler(404)
def _404(e):
    return render('home/404.html', msg=e)


@app.errorhandler(405)
def _405(e):
    return render('home/405.html', msg=e)


@app.errorhandler(500)
def _500(e):
    return render('home/500.html', msg=e)


if __name__ == '__main__':
    app.run(debug=True, port=81)
 