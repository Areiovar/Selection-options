from flask import Flask, url_for

app = Flask(__name__)


@app.route('/choice/<planet_name>')
def planet_choice(planet_name):
    html_content = f'''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet"
              href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
              integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
              crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
    </head>
    <body>
    <div class="all">
        <p class="lead">Мое предложение: {planet_name}.</p>
        <h1>Эта планета близка к земле;</h1><br>
        <div class="alert alert-dark" role="alert" id="phrase1">
            На ней много необходимых ресурсов;
        </div>
        <div class="alert alert-success" role="alert" id="phrase2">
            На ней есть вода и атмосфера;
        </div>
        <div class="alert alert-secondary" role="alert" id="phrase3">
            На ней есть большое магнитное поле;
        </div>
        <div class="alert alert-warning" role="alert" id="phrase4">
            Наконец, она просто красива!
        </div>
    </div>
    </body>
    </html>
    '''
    return html_content


if __name__ == '__main__':
    app.run('127.0.0.1', 8080)
