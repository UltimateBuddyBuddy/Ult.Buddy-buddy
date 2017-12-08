from flask import Flask, render_template, request
app = Flask(__name__)
from datetime import datetime


@app.route('/')
def main():
	return render_template("main.html")

@app.route('/team')
def bio():
	return render_template('team.html')

buddyRequests = []
@app.route('/reserve', methods=['GET','POST'])
def reserve():
	global buddyRequests
	if request.method == 'POST':

		user = request.form['user']
		weekday = request.form['wkday']
		activity = request.form['act']
		location = request.form['loc']
		start = request.form['shr'] + ":" + request.form['smin']
		end = request.form['ehr'] + ":" + request.form['emin']
		time = datetime.now()

		buddyForm = {
			'user':user,
			'act':activity,
			'loc':location,
			'wkD': weekday,
			'start':start,
			'end':end,
			'time':time
		}

		# messages
		buddyRequests.insert(0, buddyForm) # add form object to the front of the list

		return render_template("reserve.html", buddyRequests=buddyRequests)

	else:
		return render_template("reserve.html", buddyRequests=buddyRequests)

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
