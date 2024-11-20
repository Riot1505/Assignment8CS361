from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('password')
        return redirect(url_for('success', name='Bob'))


if __name__ == '__main__':
    app.run(debug=True)
