from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def main():
	return render_template("main.html")

@app.route('/team')
def bio():
	return render_template('team.html')

@app.route('/reserve')
def reserve():
	return render_template('reserve.html')

@app.route('/buddy')
def buddy():
	return render_template('buddy.html')

@app.route('/formdemo')
def formdemo():
	return render_template('formdemo.html')

@app.route('/keefa')
def keefa():
	return render_template('keefa.html')

@app.route('/agnes')
def agnes():
	return render_template('agnes.html')

@app.route('/kareem')
def kareem():
	return render_template('kareem.html')

@app.route('/ali')
def ali():
	return render_template('ali.html')

@app.route('/raven')
def raven():
	return render_template('raven.html')

if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
