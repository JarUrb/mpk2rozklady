from flask import Flask, redirect, render_template, request, url_for

from mapping import MAPPING


URL_FMT = 'http://rozklady.lodz.pl/Home/TimeTableReal?busStopId={}'


app = Flask(__name__)


def get_and_redir(mpk_stop_id):
    rozklady_stop_id = MAPPING.get(mpk_stop_id)
    if rozklady_stop_id:
        return redirect(URL_FMT.format(rozklady_stop_id))
    return redirect(url_for('index'))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mpk_stop_id = request.form.get('mpk_stop_id', '')
        if mpk_stop_id.isdigit():
            return get_and_redir(int(mpk_stop_id))
    return render_template('index.html')


@app.route('/<int:mpk_stop_id>/')
def redir(mpk_stop_id):
    return get_and_redir(mpk_stop_id)


if __name__ == '__main__':
    app.run()
