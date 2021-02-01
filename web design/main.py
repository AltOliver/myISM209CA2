from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return '''My name is Nri Oliver. This is my CA2 work. 
    My Github URL is https://github.com/AltOliver''', render_template('home.html', title="Home")


@app.route("/products-and-services/")
def products_and_services():
    return render_template('products-and-services.html', title="Products and Services")


@app.route("/about-us/")
def about_us():
    return render_template('about-us.html', title="About Us")


if __name__ == "__main__":
    app.run(port=5005)
