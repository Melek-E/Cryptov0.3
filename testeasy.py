from flask import Flask, redirect, url_for, render_template, request
from main import Y #import the blockchain


app= Flask(__name__)



@app.route("/")
def home():
    return render_template("login.html")
"""
@app.route("/login", methods=['GET', 'POST'])
def rimmed():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index.html'))
    return render_template('login.html')
"""

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/error")
def error():
    return render_template("404.html")

@app.route("/reg")
def reg():
    return render_template("reg.html")

@app.route("/registerpage")
def registerpage():
    return render_template("registerpage.html")


@app.route("/login")
def login():
    login=True
    if login:
        return render_template("index.html", var="temp lol")
    return render_template('login.html')

@app.route("/forgor")
def forgor():
    return render_template("forgot-password.html")

@app.route("/waiting")
def waiting():
    return render_template("temp.html")


chain=['numba1', 'numba2']
@app.route('/testing')
def loopies():
    return render_template("testing.html",len = len(chain), chain = chain)
#https://www.geeksforgeeks.org/python-using-for-loop-in-flask/
#does     return redirect(url_for("admin")) make it loop forever

@app.route('/blocks')
def blocks():
    return render_template('blockchain.html', title = "Blockchain", blockchain = Y);

app.run(debug=True, threaded=True)





string="""<li class="list-group-item">
					  <div class="collapse" id="collapse{{loop.index}}">
					  	{% if loop.index == 1 %}
					  		<span class="">No Transactions</span>
					  	{% else %}
						  	{% for transaction in block.transactions %}
						  		<span class="">Transaction {{loop.index}}:</span>
						  		<br>
						  		<small>Sender: {{ transaction.sender }}</small>
						  		<br>
						  		<small>Reciever: {{ transaction.reciever }}</small>
						  		<br>
						  		<small>Amount: {{ transaction.amt }}</small>
						  		<br>
						  		<small>Time: {{ transaction.time }}</small>
						  		<br>
						  	{% endfor %}
						{% endif %}
					  </div>
				  </li>"""












temp=""" <div class="card mb-3">
          <div class="card-header">
            <i class="fas fa-chart-area"></i>
            Area Chart Example</div>
          <div class="card-body">
            <canvas id="myAreaChart" width="100%" height="30"></canvas>
          </div>
          <div class="card-footer small text-muted">Updated yesterday at 11:59 PM</div>
        </div> """