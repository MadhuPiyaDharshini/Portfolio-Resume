from flask import Flask, render_template, url_for

#instantiate the flask app
app = Flask(__name__)

#create each of the routes. The home page route
@app.route("/")
@app.route("/home")
def home():
    return render_template('portfolio_home.html')

#about page route
@app.route("/about")
def about():
    return render_template('about.html')
#portfolio page route
@app.route("/portfolio", methods= ['GET', 'POST'])
def portfolio():
    return render_template('portfolio.html')

#contact me page route
@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug= True)
