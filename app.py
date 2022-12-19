from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route("/")
def welcome():
    """This is a welcome page."""

    return render_template("welcome.html")


@app.route("/home")
def home():
    """This is a home page."""

    return render_template("home.html")


@app.route("/about")
def about():
    """This is a about page"""

    return render_template("about.html")


@app.route("/argan")
def argan_spa():
    """This is a product page for: Argan Spa"""

    return render_template("argan_spa.html")


@app.route("/clarifying")
def clarifying_shampoo():
    """This is a product page for: Clarifying Shampoo"""

    return render_template("clarifying_shampoo.html")


@app.route("/dtan")
def dtan():
    """This is a product page for: D Tan"""

    return render_template("dtan.html")


@app.route("/hairmask")
def hair_mask():
    """This is a product page for: Hair Care Mask"""

    return render_template("hair_mask.html")


@app.route("/hairserum")
def hair_serum():
    """This is a product page for: Hair Serum"""

    return render_template("hair_serum.html")


@app.route("/haircareshampoo")
def haircare_shampoo():
    """This is a product page for: Hair Care Shampoo"""

    return render_template("haircare_shampoo.html")


@app.route("/homecaremask")
def homecare_mask():
    """This is a product page for: Home Care Mask"""

    return render_template("homecare_mask.html")


@app.route("/homecareshampoo")
def homecare_shampoo():
    """This is a product page for: Home Care Shampoo"""

    return render_template("homecare_shampoo.html")


@app.route("/neutralizing")
def neutralizing():
    """This is a product page for: Neutralizing"""

    return render_template("neutralizing.html")


@app.route("/smoothing")
def smoothing():
    """This is a product page for: Smoothing"""

    return render_template("smoothing.html")


@app.route("/treatment")
def treatment():
    """This is a product page for: Hair Treatment"""

    return render_template("treatment.html")


@app.route("/contact")
def contact():
    """This is a contact info page."""

    return render_template("contact.html")
