from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    t = request.args.get('type') or "1"  # 1-male & 0-female
    p = request.args.get('p') or "1"  # payed 1-payed & 0-free

    get_params = "?type={}&p={}".format(t, p)

    if t == "1":  # male
        if p == "1":  # male payed
            return render_template('payed_9_99.html', get_params=get_params, images_type="girl")
        else:  # male free
            return render_template('free.html', get_params=get_params, images_type="girl")
    else:  # female
        if p == "1":  # female payed
            return render_template('payed_9_99.html', get_params=get_params, images_type="man")
        else:  # female free
            return render_template('free.html', get_params=get_params, images_type="man")


@app.route('/download/')
def download():
    t = request.args.get('type') or 1  # 1-male & 0-female
    p = request.args.get('p') or 1  # payed 1-payed & 0-free

    get_params = "?type={}&p={}".format(t, p)

    return render_template('success.html', get_params=get_params)


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=8000)
